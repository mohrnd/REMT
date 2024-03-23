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
from fabric import Connection



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
        self.ADD_BUTTON.clicked.connect(self.snmpconf_setup)
        
        self.disable_snmp_form_fields()
        
    def disable_snmp_form_fields(self):
        for widget in self.findChildren(QWidget):
            if widget.geometry().top() > self.HorizontalSeparator.geometry().bottom():
                widget.setEnabled(False)
                
    def enable_snmp_form_fields(self):
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
                QMessageBox.information(self, "Success", f"SSH connection to '{MachineName}' successful!")
                self.enable_snmp_form_fields()
            
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
        
    def snmpconf_setup(self):
        with open('../REMT/tests/adding_machines/SNMPv3_Config_template.txt', 'r') as file:
            setup_script_content = file.read()
        hostname = self.IPAddress.text()
        username = self.MachineUsername.text()
        password = self.MachinePassword.text()
        MachineName = self.MachineName.text()
        SNMPv3_username = self.SNMPv3USERNAME.text()
        if self.ReadOnly.isChecked():
            UserType = 'rouser'
        elif self.ReadWrite.isChecked():
            UserType = 'rwuser'
        
        if self.MD5CheckBox.isChecked():
            auth_Protocole= 'MD5'
        elif self.SHACheckBox.isChecked():
            auth_Protocole = 'SHA'
        
        if self.DESCheckBoX.isChecked():
            Priv_Protocole = 'DES'
        elif self.AESCheckBox.isChecked():
            Priv_Protocole = 'AES'
            
        port = self.Port.text()
        if port == '':
            port = 22
        else:
            port = int(port) 
            
        Auth_password = self.SNMPv3PASSWORD.text()
        Priv_password = self.EncryptionKey.text()
        managerIP = self.ManagerIP.text()
        
        if SNMPv3_username == '' or UserType == '' or auth_Protocole == '' or Priv_Protocole == '' or Auth_password == '' or Priv_password == '' or hostname == '':
            QMessageBox.warning(self, "Error", "Please fill all of the forms.")
        else:
            setup_script_content = setup_script_content.format(SNMPv3_username=SNMPv3_username, UserType=UserType, 
                                                               auth_Protocole=auth_Protocole, Auth_password=Auth_password, 
                                                               Priv_Protocole=Priv_Protocole, Priv_password=Priv_password, ip=managerIP)

            content_lines = setup_script_content.split('\n')
            for line in content_lines:
                client = ssh_client_creation(hostname, port, username, password)
                stdin, stdout, stderr = client.exec_command(f"{line}", get_pty=True)
                output = stdout.read().decode().strip()
                print(output)
                Machine_Info = 'something'
                security_engine_id = ''
            create_or_update_csv(SNMPv3_username, auth_Protocole, Auth_password, Priv_Protocole, Priv_password, security_engine_id, hostname, password, username, MachineName, Machine_Info)
                
# the config only works using root, now i can either make a form to enter the root password and only use it for the initial config, or i will try to find a way to make it work

def create_or_update_csv(SNMPv3_username, auth_Protocole, auth_password, Priv_Protocole, priv_password, security_engine_id, ip_add, password, linux_username, Machine_Name, Machine_Info):
    columns = ['SNMPv3_username', 
               'auth_Protocole', 
               'auth_password',
               'Priv_Protocole',
               'priv_password',
               'security_engine_id',
               'ip_add', 
               'password',
               'linux_username',
               'Machine_Name',
               'Machine_Info']
    data = [SNMPv3_username, auth_Protocole, auth_password, Priv_Protocole, priv_password, security_engine_id, ip_add, password, linux_username, Machine_Name, Machine_Info]
    csv_file_path = 'machines.csv'
    if not os.path.exists(csv_file_path):
        with open(csv_file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(columns)
            
    with open(csv_file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

        
def Check_ip(hostname):
    param = '-n' if os.name.lower() == 'nt' else '-c'
    response = os.system(f"ping {param} 1 -w 100 {hostname}> NUL 2>&1")   # 100 ms wait time, might change it later
    if response == 0:
        return True
    else:
        return False
def ssh_client_creation(host, port, username, password):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=host, port=port, username=username, password=password)
    return ssh_client        

def main():
    color = QColor('#351392')
    setThemeColor(color ,Qt.GlobalColor , '') 
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()