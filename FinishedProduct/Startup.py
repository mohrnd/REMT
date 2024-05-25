import sys
import os
from PyQt5 import QtWidgets
from REMTMainInterface import main
from PyQt5.QtGui import *
from MasterPasswordInput.FirstLoginInterface.Ui_FirstLogin import Ui_Form as Ui_FirstLoginForm
from MasterPasswordInput.LoginInterface.Ui_LoginMasterPasswordInput import Ui_Form as Ui_LoginForm
from MainInterface.adding_machines.cipher_decipher_logic.CipherDecipher import check_password, create_password_file
from qfluentwidgets import (NavigationItemPosition, MessageBox, setTheme, setThemeColor, Theme, FluentWindow,
                            NavigationAvatarWidget, SubtitleLabel, setFont, InfoBadge,
                            InfoBadgePosition, CheckBox, PushButton, IndeterminateProgressRing)
from PyQt5.QtCore import Qt

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
            self.close()
            self.login_window = LoginWindow()
            self.login_window.show()
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Passwords do not match!")


class LoginWindow(QtWidgets.QWidget, Ui_LoginForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.MasterPWDContinue_login.clicked.connect(self.check_password)

    def check_password(self):
        password = self.MasterPassword_login.text()
        if check_password(password):
            self.close()
            main()
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Your masterpassword is incorrect !")

def show_first_login_interface():
    color = QColor('#351392')
    setThemeColor(color ,Qt.GlobalColor , '') 
    app = QtWidgets.QApplication(sys.argv)
    first_login_window = FirstLoginWindow()
    first_login_window.show()
    sys.exit(app.exec_())

def show_login_interface():
    color = QColor('#351392')
    setThemeColor(color ,Qt.GlobalColor , '') 
    app = QtWidgets.QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())


hash_file_path = 'C:\\ProgramData\\.Hash1851320.txt'

if __name__ == '__main__':
    if not os.path.exists(hash_file_path):
        show_first_login_interface()
    else:
        show_login_interface()
