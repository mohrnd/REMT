import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox, QAbstractItemView, QDialog
from Ui_Add_machine import Ui_Form
from PyQt5.QtCore import Qt, QTimer, QThread, pyqtSignal, QRect
from PyQt5.QtGui import *
from qfluentwidgets import (NavigationItemPosition, MessageBox, setTheme, setThemeColor, Theme, FluentWindow,
                            NavigationAvatarWidget, SubtitleLabel, setFont, InfoBadge,
                            InfoBadgePosition, CheckBox, PushButton, IndeterminateProgressRing)
import os
import csv
import paramiko
from paramiko import SSHException
from fabric import Connection
from Ui_root_password_master_password_forms import *
from password_hash_storage import check_password 
from Ui_Config_progress import *
from pyqt_translucent_full_loading_screen_thread import LoadingThread, LoadingTranslucentScreen
from PyQt5.QtCore import QTimer, QThread

"""
TODO:
execute the config.py from the LOG folder

"""

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
        self.ADD_BUTTON.clicked.connect(self.show_root_password_form)  
        self.disable_snmp_form_fields()
        
        
        
    def show_root_password_form(self):
        self.root_password_form = QDialog()
        self.show_root_password_form_ui = Ui_Form2()
        self.show_root_password_form_ui.setupUi(self.root_password_form)
        self.show_root_password_form_ui.StartTheConf_config.clicked.connect(self.fetch_root_values)
        self.show_root_password_form_ui.CancelTheConf_config.clicked.connect(self.root_password_form.reject)
        self.show_root_password_form_ui.ProgressBar_2.hide()  
        self.show_root_password_form_ui.StrongBodyLabel_2.hide()
        self.root_password_form.exec_()
        

    def StartLoading(self, message, parent=None):
        self.__loadingTranslucentScreen = LoadingTranslucentScreen(parent=parent, description_text=message)
        self.__loadingTranslucentScreen.setDescriptionLabelDirection('Right')
        self.__thread = LoadingThread(loading_screen=self.__loadingTranslucentScreen)
        self.__thread.start()

    
    def show_config_progress(self):
        self.config_progress_form = QDialog()
        self.ui_config_progress = Ui_Form3() 
        self.ui_config_progress.setupUi(self.config_progress_form)
        self.ui_config_progress.failure.hide()
        self.ui_config_progress.machine_added.hide()
        self.ui_config_progress.configprogress_finish.clicked.connect(self.config_progress_form.reject)
        self.config_progress_form.show()

        
    def fetch_root_values(self):
        root_user = self.root_password_form.findChild(QtWidgets.QLineEdit, "RootUser_config").text()
        root_password = self.root_password_form.findChild(QtWidgets.QLineEdit, "RootPassword_config").text()
        master_password = self.root_password_form.findChild(QtWidgets.QLineEdit, "MasterPassword_config").text()
        output = check_password(master_password)
        if output == True:
            self.snmpconf_setup(root_user, root_password, master_password)
            self.root_password_form.hide()
        else:
            QMessageBox.warning(self, "Error", "Master password incorrect, this incident will be reported")

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
        
        port = self.PortForm.text()
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

    
    def snmpconf_setup(self, root_username, root_password, master_password):
        # self.show_root_password_form_ui.ProgressBar_2.show()
        # self.show_root_password_form_ui.StrongBodyLabel_2.show()  
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
            
        port = self.PortForm.text()
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
            num_lines = len(content_lines)
            unit = num_lines // 100
            current_progress = 0
            for line in content_lines:
                client = ssh_client_creation(hostname, port, root_username, root_password)
                stdin, stdout, stderr = client.exec_command(f"{line}", get_pty=True)
                output = stdout.read().decode().strip()
                print(output)
                current_progress += unit
                if current_progress > 100:
                    current_progress = 100

                self.show_root_password_form_ui.ProgressBar_2.setValue(current_progress)
            
                

                RefreshTime = self.SNMPTIMEOUT.text()
                if RefreshTime == '':
                    RefreshTime = 30

                if 'oldEngineID' in output:
                    substring_to_remove = "oldEngineID 0x"
                    security_engine_id = output.replace(substring_to_remove, "")
                    
            QMessageBox.information(self, "Info", f"Machine {hostname} added successfully.")
            create_or_update_csv(SNMPv3_username, auth_Protocole, Auth_password, Priv_Protocole, Priv_password, security_engine_id, hostname, password, username, port ,MachineName, RefreshTime)
        
        
def create_or_update_csv(SNMPv3_username, auth_Protocole, auth_password, Priv_Protocole, priv_password, security_engine_id, ip_add, password, linux_username, port ,Machine_Name, RefreshTime):
    columns = ['SNMPv3_username', 
               'auth_Protocole', 
               'auth_password',
               'Priv_Protocole',
               'priv_password',
               'security_engine_id',
               'ip_add', 
               'password',
               'linux_username',
               'port' ,
               'Machine_Name',
               'RefreshTime']
    data = [SNMPv3_username, auth_Protocole, auth_password, Priv_Protocole, priv_password, security_engine_id, ip_add, password, linux_username, port ,Machine_Name, RefreshTime]
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
    
    
    # TODO : FIX THE FREEZING ISSUE
            # ADD THE PASSWORD CIPHER