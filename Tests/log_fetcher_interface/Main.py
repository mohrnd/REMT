import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QHBoxLayout, QSpacerItem, QSizePolicy, QAbstractItemView, QMessageBox
from Ui_logfetcher_interface import Ui_Form
from qfluentwidgets import setTheme, setThemeColor, FluentWindow, CheckBox, PushButton, ToggleButton, TreeWidget, PrimaryPushButton
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QTimer
from LOGS.fetch_logs import fetch
from configparser import ConfigParser
import os
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
        config = ConfigParser()
        config.read(r"../REMT/Tests/log_fetcher_interface/settings.ini")
        config_data = config["DEFAULT"]
        DestinationPath = config_data['LogsDestinationPath']  
        
        items = [
    {
        'name': 'Machine1',
        'ip': '192.168.69.40',
        'latest_fetch': '2024-04-24',
        'sublines': ['2024-04-23:Open', '2024-04-22:Open']
    },
    {
        'name': 'Machine2',
        'ip': '192.168.1.2',
        'status': 'Offline',
        'latest_fetch': '2024-04-23',
        'sublines': ['2024-04-22:Open', '2024-04-21:Open', '2024-04-20:Open']
    }
        ]
        add_lines(self.TreeWidget, items)

def Check_ip(hostname):
    param = '-n' if os.name.lower() == 'nt' else '-c'
    response = os.system(f"ping {param} 1 -w 100 {hostname} > NUL 2>&1")   # 100 ms wait time, might change it later
    if response == 0:
        return True
    else:
        return False

def add_lines(tree_widget, items):
    for item in items:
        parent_item = QtWidgets.QTreeWidgetItem(tree_widget)
        parent_item.setText(0, item['name'])
        parent_item.setText(1, item['ip'])
        parent_item.setText(3, item['latest_fetch'])
        
        if Check_ip(item['ip']) is True:
            parent_item.setText(2, '🟢 Online') 
            button = PrimaryPushButton("Fetch", tree_widget)
            font = QtGui.QFont()
            font.setPointSize(7)
            font.setBold(False)
            font.setWeight(50)
            button.setFont(font)
            tree_widget.setItemWidget(parent_item, 4, button)
            button.clicked.connect(lambda checked, Machinename=item['name'], Ip= item['ip']: FetchLogs(Machinename, Ip))
        else:
            parent_item.setText(2, '🔴 Offline')
        if 'sublines' in item:
            for subline in item['sublines']:
                subline_parts = subline.split(':')
                if len(subline_parts) == 2:
                    date_text, button_text = subline_parts
                    child_item = QtWidgets.QTreeWidgetItem(parent_item)
                    child_item.setText(0, date_text)
                    child_item_button = PushButton("Open", tree_widget)
                    font = QtGui.QFont()
                    font.setPointSize(5)
                    font.setBold(True)
                    font.setWeight(40)
                    child_item_button.setFont(font)
                    tree_widget.setItemWidget(child_item, 1, child_item_button)
                    child_item_button.clicked.connect(lambda checked, date=date_text: OpenFolder(date))
                else:
                    child_item = QtWidgets.QTreeWidgetItem(parent_item)
                    child_item.setText(0, subline)
def FetchLogs(Machinename, Ip):
    print("Parent clicked:", Machinename, Ip)


def OpenFolder(date):
    print("Child clicked:", date)


def main():
    app = QApplication(sys.argv)
    color = QColor('#351392')
    setThemeColor(color.name(), Qt.GlobalColor, '') 
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
