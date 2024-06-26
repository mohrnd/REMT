import sys
import os
import csv
from PyQt5 import QtWidgets, QtCore
from REMTMainInterface import main  # Ensure this is correctly imported
from PyQt5.QtGui import *
from MasterPasswordInput.FirstLoginInterface.Ui_FirstLogin import Ui_Form as Ui_FirstLoginForm
from MasterPasswordInput.LoginInterface.Ui_LoginMasterPasswordInput import Ui_Form as Ui_LoginForm
from MainInterface.adding_machines.cipher_decipher_logic.CipherDecipher import check_password, create_password_file
from qfluentwidgets import (NavigationItemPosition, MessageBox, setTheme, setThemeColor, Theme, FluentWindow,
                            NavigationAvatarWidget, SubtitleLabel, setFont, InfoBadge,
                            InfoBadgePosition, CheckBox, PushButton, IndeterminateProgressRing)
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication

machines_file_path = 'machines.csv'

def create_vault_file_and_REMT_folder():
    file_path = 'C:\\ProgramData\\.Vault1851320.txt'
    folder_path = 'C:\\ProgramData\\REMT'
    Trap_logs = 'TrapsReceived.log'

    # Check if REMT folder exists, create if it doesn't
    if not os.path.exists(folder_path):
        try:
            os.makedirs(folder_path)
            print(f"Folder '{folder_path}' created successfully.")
        except Exception as e:
            print(f"Error occurred while creating folder: {e}")
    if not os.path.exists(file_path):
        try:
            with open(file_path, 'w'):
                pass
            os.system(f'attrib +H "{file_path}"')
            print(f"File '{file_path}' created and hidden successfully.")
        except Exception as e:
            print(f"Error occurred while setting file attributes: {e}")
            
    if not os.path.exists(Trap_logs):
        with open(Trap_logs, 'w'):
            pass
        print(f"File '{Trap_logs}' created successfully.")

def create_machines_file():
    """Check if machines.csv file exists; if not, create an empty file."""
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
    if not os.path.exists(machines_file_path):
        with open(machines_file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(columns)
        print(f"Created {machines_file_path} with columns: {columns}")

class FirstLoginWindow(QtWidgets.QWidget, Ui_FirstLoginForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.MasterPWDContinue.clicked.connect(self.save_password)

    def save_password(self):
        password = self.PasswordInput.text()
        password_confirm = self.PasswordInput2.text()
        if password == password_confirm:
            create_password_file(password)
            create_machines_file()
            create_vault_file_and_REMT_folder()
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Passwords do not match!")

class LoginWindow(QtWidgets.QWidget, Ui_LoginForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.MasterPWDContinue_login.clicked.connect(self.check_password)
        create_machines_file()

    def check_password(self):
        password = self.MasterPassword_login.text()
        if check_password(password):
            self.close()
            main(password)
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Your master password is incorrect!")

def show_first_login_interface():
    color = QColor('#351392')
    setThemeColor(color, Qt.GlobalColor, '') 
    app = QtWidgets.QApplication(sys.argv)
    first_login_window = FirstLoginWindow()
    first_login_window.show()
    sys.exit(app.exec_())

def show_login_interface():
    color = QColor('#351392')
    setThemeColor(color, Qt.GlobalColor, '') 
    app = QtWidgets.QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())

hash_file_path = 'C:\\ProgramData\\.Hash1851320.txt'

if __name__ == '__main__':
    # QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    # QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    # QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    if not os.path.exists(hash_file_path):
        show_first_login_interface()
    else:
        show_login_interface()
        
