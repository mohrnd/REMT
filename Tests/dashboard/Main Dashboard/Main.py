import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox, QAbstractItemView
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import *
from qfluentwidgets import (TimePicker, NavigationItemPosition, MessageBox, setTheme, setThemeColor, Theme, FluentWindow,
                            NavigationAvatarWidget, SubtitleLabel, setFont, InfoBadge,
                            InfoBadgePosition, CheckBox, PushButton, PrimaryPushButton)
from Ui_Dashboard import Ui_Form
from PyQt5.QtWidgets import QMainWindow
import json, os, csv, time, threading
import re

class MainWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.MainTable.setStyleSheet("QTableWidget { border: 1px solid gray; selection-background-color: #AF9BE5;  }")
        self.MainTable.setEditTriggers(QAbstractItemView.NoEditTriggers) 
        self.FillData()
        # monitor_params_threads_creator(r'../REMT/Tests/task_scheduling/snmp_users.csv')

    def FillData(self):
        log_file = r"C:\Users\BALLS2 (rip BALLS)\Desktop\REMT\TrapsReceived.log"
        latest_trap, latest_shutdown, latest_startup = parse_log_file(log_file)
        # self.LatestTrap.setText(str(latest_trap))
        self.LatestShutdown.setText(str(latest_shutdown))
        self.LatestStartup.setText(str(latest_startup))
        self.Total_Machines = 0
        self.Machines_Online = 0
        self.MainTable.clearContents()
        self.MainTable.setRowCount(0)
        csv_file = r'../REMT/Tests/task_scheduling/snmp_users.csv'
        with open(csv_file, 'r') as file:
            csv_reader = csv.DictReader(file)  # Use DictReader to treat rows as dictionaries
            for row in csv_reader:
                ip_address = row['ip_add']
                machine_name = row['Machine_Name']
                self.Total_Machines += 1
                Status = None
                Uptime = None
                self.addRow(machine_name, ip_address, Status, Uptime, CpuUsage, RamUsage, DiskUsage)
                print(machine_name, ip_address)
        self.MachinesOnline.setText(str(self.Total_Machines))

    def addRow(self, machine_name, ip_address, Status, Uptime, CpuUsage, RamUsage, DiskUsage):
        rowPosition = self.MainTable.rowCount()
        self.MainTable.insertRow(rowPosition)
        self.MainTable.setItem(rowPosition, 0, QTableWidgetItem(machine_name))
        self.MainTable.setItem(rowPosition, 1, QTableWidgetItem(ip_address))
        self.MainTable.setItem(rowPosition, 2, QTableWidgetItem(Status)) # status
        self.MainTable.setItem(rowPosition, 3, QTableWidgetItem(Uptime))
        self.MainTable.setItem(rowPosition, 4, QTableWidgetItem(CpuUsage))
        self.MainTable.setItem(rowPosition, 5, QTableWidgetItem(RamUsage))
        self.MainTable.setItem(rowPosition, 6, QTableWidgetItem(DiskUsage))
        DeleteButton = PushButton('More')
        self.MainTable.setCellWidget(rowPosition, 7, DeleteButton)

def parse_log_file(log_file):
    latest_trap = None
    latest_shutdown = None
    latest_startup = None

    with open(log_file, 'r') as file:
        lines = file.readlines()
        for line in lines:  
            timestamp = re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', line).group()  # Extract timestamp using regex
            ip_match = re.search(r'"(.*?)"', line)  # Extract IP address within double quotes using regex
            if ip_match:
                ip_address = ip_match.group(1)
            else:
                ip_address = None
            
            latest_trap = f"{timestamp}\n{ip_address}"
            if "SystemShutdown" in line:
                latest_shutdown = f"{timestamp}\n{ip_address}"
            elif "SystemStartup" in line:
                latest_startup = f"{timestamp}\n{ip_address}"
            # If all variables are found, exit loop
            if latest_shutdown and latest_startup and latest_trap:
                break
    
    return latest_trap, latest_shutdown, latest_startup

def monitor_machine_online(ip_address):
    param = '-n' if os.name.lower() == 'nt' else '-c'
    response = os.system(f"ping {param} 1 -w 100 {ip_address} > NUL 2>&1")   # 100 ms wait time, might change it later
    if response == 0:
        print(f"{ip_address} is online")
    else:
        print(f"{ip_address} is offline")

def monitor_params_threads_creator(csv_file):
    existing_params = set()
    while True:
        new_params = read_params_from_csv(csv_file)
        for params in new_params:
            ip_address = params['ip_add']  # Assuming 'ip_add' is the key for IP address in your CSV
            if ip_address not in existing_params:
                thread = threading.Thread(target=monitor_machine_online, args=(ip_address,))
                thread.start()
                existing_params.add(ip_address)
        time.sleep(60)  # checks the users file for any new changes

# Assuming you have a function to read params from CSV named read_params_from_csv

def read_params_from_csv(csv_file):
    params_list = []
    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            params_list.append(row)
    return params_list

def Check_ip(hostname):
    param = '-n' if os.name.lower() == 'nt' else '-c'
    response = os.system(f"ping {param} 1 -w 100 {hostname} > NUL 2>&1")   # 100 ms wait time, might change it later
    if response == 0:
        return True
    else:
        return False

def main():
    color = QColor('#351392')
    setThemeColor(color ,Qt.GlobalColor , '') 
    app = QApplication(sys.argv)
    window = MainWindow() 
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()