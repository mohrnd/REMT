import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox, QAbstractItemView
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import *
from qfluentwidgets import (TimePicker, NavigationItemPosition, MessageBox, setTheme, setThemeColor, Theme, FluentWindow,
                            NavigationAvatarWidget, SubtitleLabel, setFont, InfoBadge,
                            InfoBadgePosition, CheckBox, PushButton, PrimaryPushButton)
from .Ui_Dashboard import Ui_Form
from PyQt5.QtWidgets import QMainWindow
import json, os, csv, time, threading
import re
from .Machine_Details.Main import main as OpenMachineDetails

class MainWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.MainTable.setStyleSheet("QTableWidget { border: 1px solid gray; selection-background-color: #AF9BE5;  }")
        self.MainTable.setEditTriggers(QAbstractItemView.NoEditTriggers) 
        self.start_thread()
        self.FillData()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.FillData)
        self.timer.start(10000)


        
    def start_thread(self):
        def thread_function():
            from .data_fetcher import main
            masterpassword = 'MASTERPASSWORD'
            main(masterpassword)
        # Create and start the thread
        self.thread = threading.Thread(target=thread_function)
        self.thread.start()
        
    def start_thread2(self, machine_name, ip_address):
        def thread_function2(machine_name, ip_address):
            OpenMachineDetails(machine_name, ip_address)
        # Create and start the thread
        self.thread = threading.Thread(target=thread_function2, args=(machine_name, ip_address))
        self.thread.start()

    def FillData(self):
        log_file = r"..\REMT\TrapsReceived.log"
        latest_trap, latest_shutdown, latest_startup = parse_log_file(log_file)
        self.LatestShutdown.setText(str(latest_shutdown))
        self.LatestStartup.setText(str(latest_startup))
        self.Total_Machines = 0
        self.Machines_Online = 0
        self.MainTable.clearContents()
        self.MainTable.setRowCount(0)
        csv_file = r'machines.csv'
        with open(csv_file, 'r') as file:
            csv_reader = csv.DictReader(file) 
            for row in csv_reader:
                ip_address = row['ip_add']
                machine_name = row['Machine_Name']
                self.Total_Machines += 1
                json_file = fr"C:\ProgramData\REMT\{machine_name}.json"
                with open(json_file, 'r') as f:
                    data = json.load(f)
                    Latest_line = data[-1]
                    Status = online_Check(ip_address)
                    if Status == '🟢Online':
                        self.Machines_Online = self.Machines_Online + 1
                        CpuUsage = Latest_line['CPUusage']
                        print(CpuUsage)
                        RamUsage = Latest_line['RAMusage']
                        print(RamUsage)
                        DiskUsage = Latest_line['DISKusage']
                        print(DiskUsage)
                        Uptime = Latest_line['UPTIME']
                        Uptime = convert_uptime(Uptime)
                        print(Uptime)
                    else:
                        CpuUsage = None
                        RamUsage = None
                        DiskUsage = None
                        Uptime = None
                    self.addRow(machine_name, ip_address, Status, Uptime, CpuUsage, RamUsage, DiskUsage)
                    print(machine_name, ip_address)
        self.TotalMachines.setText(str(self.Total_Machines))
        self.MachinesOnline.setText(str(self.Machines_Online))

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
        more_button = PushButton('More')
        more_button.clicked.connect(lambda _, machine=machine_name, ip=ip_address: self.onMoreClicked(machine, ip))
        self.MainTable.setCellWidget(rowPosition, 7, more_button)

    def onMoreClicked(self, machine_name, ip_address):
        self.start_thread2(machine_name, ip_address)

def convert_uptime(uptime_hundredths):
    uptime_seconds = int(uptime_hundredths) / 100  # Convert to seconds
    if uptime_seconds < 60:
        return f"{uptime_seconds:.2f} seconds"
    elif uptime_seconds < 3600:
        uptime_minutes = uptime_seconds / 60
        return f"{uptime_minutes:.2f} minutes"
    elif uptime_seconds < 86400:
        uptime_hours = uptime_seconds / 3600
        return f"{uptime_hours:.2f} hours"
    else:
        uptime_days = uptime_seconds / 86400
        return f"{uptime_days:.2f} days"
    
def parse_log_file(log_file):
    latest_trap = None
    latest_shutdown = None
    latest_startup = None

    with open(log_file, 'r') as file:
        lines = file.readlines()
        for line in lines:  
            timestamp = re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', line).group() 
            ip_match = re.search(r'"(.*?)"', line)  
            if ip_match:
                ip_address = ip_match.group(1)
            else:
                ip_address = None
            
            latest_trap = f"{timestamp}\n{ip_address}"
            if "SystemShutdown" in line:
                latest_shutdown = f"{timestamp}\n{ip_address}"
            elif "SystemStartup" in line:
                latest_startup = f"{timestamp}\n{ip_address}"
            if latest_shutdown and latest_startup and latest_trap:
                break
    
    return latest_trap, latest_shutdown, latest_startup

def online_Check(ip_address):
    param = '-n' if os.name.lower() == 'nt' else '-c'
    response = os.system(f"ping {param} 1 -w 100 {ip_address} > NUL 2>&1")   # 100 ms wait time, might change it later
    if response == 0:
        return '🟢Online'
    else:
        return '🔴Offline'

# def main():
#     color = QColor('#351392')
#     setThemeColor(color ,Qt.GlobalColor , '') 
#     app = QApplication(sys.argv)
#     window = MainWindow() 
#     window.show()

#     sys.exit(app.exec_())

# if __name__ == "__main__":
#     main()
