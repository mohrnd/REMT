import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox, QAbstractItemView
from Ui_Add_machine import Ui_Form
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import *
from qfluentwidgets import (NavigationItemPosition, MessageBox, setTheme, setThemeColor, Theme, FluentWindow,
                            NavigationAvatarWidget, SubtitleLabel, setFont, InfoBadge,
                            InfoBadgePosition, CheckBox, PushButton)
import os
import csv
import paramiko
from paramiko import SSHException


class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.IPAddress.textChanged.connect(self.start_ip_check_timer)
        self.ipstatusONLINE.hide()
        self.ipstatusOFFLINE.hide()
        self.ip_check_timer = QTimer(self)
        self.ip_check_timer.timeout.connect(self.check_ip_status)
        
        self.VerifyMachineInfo.clicked.connect(self.verify_machine_data)
        self.disable_form_fields()
        
    def disable_form_fields(self):
        for widget in self.findChildren(QWidget):
            if widget.geometry().top() > self.HorizontalSeparator.geometry().bottom():
                widget.setEnabled(False)
                
    def enable_form_fields(self):
        for widget in self.findChildren(QWidget):
            if widget.geometry().top() > self.HorizontalSeparator.geometry().bottom():
                widget.setEnabled(True)

    def verify_machine_data(self):
        ip_address = self.IPAddress.text()
        
        if not Check_ip(ip_address):
            QMessageBox.warning(self, "Error", "Please verify the IP address.")
            return
        
        port = self.Port.text()
        if port == '':
            port = 22
        else:
            port = int(port) 
            
        hostname = ip_address
        username = self.MachineUsername.text()
        password = self.MachinePassword.text()
        MachineName = self.MachineName.text()
        
        if username == '' or password == '' or MachineName == '':
            QMessageBox.warning(self, "Error", "Please fill all of the forms.")
        else: 
            try:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(hostname, port, username, password)
                ssh.close()
                QMessageBox.information(self, "Success", f"SSH connection to {MachineName} successful!")
                self.enable_form_fields()
            
            except SSHException as e:
                QMessageBox.warning(self, "Error", f"SSH connection failed: {str(e)}")
                
            
            except Exception as e:
                QMessageBox.warning(self, "Error", f"An error occurred: {str(e)}")
        

    def start_ip_check_timer(self):
        self.ip_check_timer.start(1000) 
        
    def check_ip_status(self):
        ip_address = self.IPAddress.text()
        
        if ip_address:
            if Check_ip(ip_address):
                self.ipstatusONLINE.show()
                self.ipstatusOFFLINE.hide()
                return True
            else:
                self.ipstatusONLINE.hide()
                self.ipstatusOFFLINE.show()
                return False
        else:
            self.ipstatusONLINE.hide()
            self.ipstatusOFFLINE.hide()
            return False
        
def Check_ip(hostname):
    param = '-n' if os.name.lower() == 'nt' else '-c'
    response = os.system(f"ping {param} 1 -w 100 {hostname}> NUL 2>&1")   # 100 ms wait time, might change it later
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