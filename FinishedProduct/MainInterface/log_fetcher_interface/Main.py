import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QHBoxLayout, QSpacerItem, QSizePolicy, QAbstractItemView, QMessageBox
from Ui_logfetcher_interface import Ui_Form
from qfluentwidgets import setTheme, setThemeColor, FluentWindow, CheckBox, PushButton, ToggleButton, TreeWidget, PrimaryPushButton
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QTimer
# from LOGS.fetch_logs import fetch
from configparser import ConfigParser
import os
from pathlib import Path
import subprocess
import csv
from datetime import datetime
# self.fetch('localhost','192.168.1.21','../REMT/Tests/LOGS/var/')

class MainWindow(Ui_Form, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.hBoxLayout = QHBoxLayout(self)
        self.hBoxLayout.addWidget(self.TreeWidget)
        self.hBoxLayout.setContentsMargins(15, 15, 15, 15)
        self.TreeWidget.setBorderVisible(True)
        self.TreeWidget.setBorderRadius(5)

        csv_path = r'machines.csv'
        add_lines(self.TreeWidget, csv_path)

def OpenFolder(MachineName, FileName):
    config = ConfigParser()
    config.read(r"../REMT/Tests/log_fetcher_interface/settings.ini")
    config_data = config["DEFAULT"]
    DestinationPath = config_data['LogsDestinationPath']  
    path = Path(fr"{DestinationPath}\{MachineName}\{FileName}")
    print(path)
    subprocess.Popen(f'explorer "{path}"')

def Check_ip(hostname):
    param = '-n' if os.name.lower() == 'nt' else '-c'
    response = os.system(f"ping {param} 1 -w 100 {hostname} > NUL 2>&1")   # 100 ms wait time, might change it later
    if response == 0:
        return True
    else:
        return False

def add_lines(tree_widget, csv_path):
    with open(csv_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            parent_item = QtWidgets.QTreeWidgetItem(tree_widget)
            parent_item.setText(0, row['Machine_Name'])
            parent_item.setText(1, row['ip_add'])
            
            # Set bold font for parent item
            font = parent_item.font(0)
            font.setBold(True)
            parent_item.setFont(0, font)
            
            if Check_ip(row['ip_add']) is True:
                parent_item.setText(2, '🟢 Online') 
                button = PrimaryPushButton("Fetch", tree_widget)
                font = QtGui.QFont()
                font.setPointSize(7)
                font.setBold(False)
                font.setWeight(50)
                button.setFont(font)
                tree_widget.setItemWidget(parent_item, 4, button)
                button.clicked.connect(lambda checked, Machinename=row['Machine_Name'], Ip= row['ip_add']: FetchLogs(Machinename, Ip))
            else:
                parent_item.setText(2, '🔴 Offline')
                
            config = ConfigParser()
            config.read(r"../REMT/Tests/log_fetcher_interface/settings.ini")
            config_data = config["DEFAULT"]
            DestinationPath = config_data['LogsDestinationPath']  
            path = Path(fr"{DestinationPath}\{row['Machine_Name']}")
            contents = os.listdir(path)
            print(contents)
            
            latest_fetch_date = None  # Initialize outside the loop
            
            for file in contents:
                items = file.split('_')
                date = items[1]
                time = items[2].replace('-', ':')
                datetime_str = f"{date} {time}"
                datetime_obj = datetime.strptime(datetime_str, "%d-%m-%Y %H:%M")
                
                if latest_fetch_date is None or datetime_obj > latest_fetch_date:
                    latest_fetch_date = datetime_obj
                    
                child_item = QtWidgets.QTreeWidgetItem(parent_item)
                # child_item.setText(0, file)
                child_item.setText(0, f'{date} {time}')
                child_item_button = PushButton("Open", tree_widget)
                font = QtGui.QFont()
                font.setPointSize(5)
                font.setBold(True)
                font.setWeight(40)
                child_item_button.setFont(font)
                tree_widget.setItemWidget(child_item, 1, child_item_button)
                child_item_button.clicked.connect(lambda checked, MachineName=row['Machine_Name'], FileName=file: OpenFolder(MachineName, FileName))
            if latest_fetch_date is not None:
                latest_fetch_date_str = latest_fetch_date.strftime("%d-%m-%Y %H:%M")
                parent_item.setText(3, latest_fetch_date_str)
                
def FetchLogs(Machinename, Ip):
    print("Parent clicked:", Machinename, Ip)


def main():
    app = QApplication(sys.argv)
    color = QColor('#351392')
    setThemeColor(color.name(), Qt.GlobalColor, '') 
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
