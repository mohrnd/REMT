import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox, QAbstractItemView
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import *
from qfluentwidgets import (TimePicker, NavigationItemPosition, MessageBox, setTheme, setThemeColor, Theme, FluentWindow,
                            NavigationAvatarWidget, SubtitleLabel, setFont, InfoBadge,
                            InfoBadgePosition, CheckBox, PushButton, PrimaryPushButton)
from Ui_FirstLogin import Ui_Form
from PyQt5.QtWidgets import QWidget
import json
from password_hash_storage import *

class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("REMT Initial Login")
        self.setWindowIcon(QIcon("../REMT/FinishedProduct/MasterPasswordInput/FirstLoginInterface/black.png"))
        self.MasterPWDContinue.clicked.connect(self.FetchMasterPasswords)
        self.CloseMasterPWDWindow.clicked.connect(self.close)
        
    def FetchMasterPasswords(self):
        MasterPassword = self.PasswordInput.text()
        MasterPassword2 = self.PasswordInput.text()
        if MasterPassword == MasterPassword2 and len(MasterPassword) > 24:
            hashed_password = hash_password(MasterPassword)
            errOutput = create_password_file(hashed_password)

            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText(errOutput)
            msg_box.setWindowTitle("Info")
            msg_box.setStandardButtons(QMessageBox.Cancel)
            msg_box.setDefaultButton(QMessageBox.Cancel)
            result = msg_box.exec_()
            
        else:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Review your password, make sure it is over 24 characters")
            msg_box.setWindowTitle("Info")
            msg_box.setStandardButtons(QMessageBox.Cancel)
            msg_box.setDefaultButton(QMessageBox.Cancel)
            result = msg_box.exec_()
        
def main():
    color = QColor('#351392')
    setThemeColor(color ,Qt.GlobalColor , '') 
    app = QApplication(sys.argv)
    window = MainWindow() 
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()