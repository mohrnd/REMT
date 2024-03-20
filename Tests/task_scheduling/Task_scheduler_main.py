import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem
from Ui_CrontabGUI import Ui_Frame  
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from qfluentwidgets import (NavigationItemPosition, MessageBox, setTheme, setThemeColor, Theme, FluentWindow,
                            NavigationAvatarWidget, SubtitleLabel, setFont, InfoBadge,
                            InfoBadgePosition, CheckBox, PushButton)
from TaskScheduler import *
import os
import csv

class MainWindow(QWidget, Ui_Frame):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show_active_machines()
        self.show_active_crons()
        self.add_button.clicked.connect(self.test)
        self.Apply.clicked.connect(self.Apply_cron)

        
    def show_active_crons(self):
        CSV_File_Path = '../REMT/Tests/task_scheduling/snmp_users.csv'
        with open(CSV_File_Path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Check = row['ip_add']
                if Check_ip(Check) == True:
                    hostname = row['ip_add']
                    port  = 22
                    username = row['linux_username']
                    password = row['password']
                    ssh_client = ssh_client_creation(hostname, port, username, password)
                    lines = print_active_jobs(ssh_client)
                    if lines:
                        cron_list = lines.split('\n')
                        for cron_job in cron_list:
                            rowPositionMachines = self.TableWidget.rowCount()
                            self.TableWidget.insertRow(rowPositionMachines)
                            self.TableWidget.setItem(rowPositionMachines, 0, QTableWidgetItem(hostname))
                            self.TableWidget.setItem(rowPositionMachines, 1, QTableWidgetItem(cron_job))
                            DeleteButton = PushButton('Delete')
                            # DeleteButton.setText(_translate("Frame", "Daily"))  
    
                            self.TableWidget.setCellWidget(rowPositionMachines, 2, DeleteButton) 
                else:
                    pass

    
    def show_active_machines(self):
        CSV_File_Path = '../REMT/Tests/task_scheduling/snmp_users.csv'
        with open(CSV_File_Path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                MachineName = row['Machine_Name']
                hostname = row['ip_add']
                stat = Check_ip(hostname)
                if stat:
                    rowPositionMachines = self.Machines.rowCount()
                    self.Machines.insertRow(rowPositionMachines)
                    self.Machines.setItem(rowPositionMachines, 0, QTableWidgetItem(hostname))
                    self.Machines.setItem(rowPositionMachines, 1, QTableWidgetItem(MachineName))
                    checkbox = CheckBox()  
                    checkbox.setChecked(False)
                    self.Machines.setCellWidget(rowPositionMachines, 2, checkbox)  # Set the CheckBox widget in the table cell

    def Apply_cron(self):
        selectedIPS = []
        for row in range(self.Machines.rowCount()):
            checkbox_item = self.Machines.cellWidget(row, 2)
            if isinstance(checkbox_item, CheckBox) and checkbox_item.isChecked():
                ip_address_item = self.Machines.item(row, 0)
                if ip_address_item is not None:
                    selectedIPS.append(ip_address_item.text())
        print(selectedIPS)
        
        ### add the add_cron method
    

    def test(self):
        text = self.minute_input.text()
        if text == '':
            print('*')
        else: 
            print(text)
            
        # insert data in the machines table (get data from the csv file)
        rowPositionMachines = self.Machines.rowCount()
        self.Machines.insertRow(rowPositionMachines)
        # Set data for the new row in Machines table
        self.Machines.setItem(rowPositionMachines, 0, QTableWidgetItem(text))
        self.Machines.setItem(rowPositionMachines, 1, QTableWidgetItem('Machine 1'))
        
        checkbox = CheckBox()  
        checkbox.setChecked(False)
        self.Machines.setCellWidget(rowPositionMachines, 2, checkbox)  # Set the CheckBox widget in the table cell

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
    

