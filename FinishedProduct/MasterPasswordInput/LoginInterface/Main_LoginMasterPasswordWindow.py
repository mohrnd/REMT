import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox, QAbstractItemView
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import *
from qfluentwidgets import (TimePicker, NavigationItemPosition, MessageBox, setTheme, setThemeColor, Theme, FluentWindow,
                            NavigationAvatarWidget, SubtitleLabel, setFont, InfoBadge,
                            InfoBadgePosition, CheckBox, PushButton, PrimaryPushButton)
from Ui_LoginMasterPasswordInput import Ui_Form
from PyQt5.QtWidgets import QWidget
import json

class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("REMT Master Password Form")
        self.setWindowIcon(QIcon("../REMT/FinishedProduct/MasterPasswordInput/FirstLoginInterface/black.png"))
        self.MasterPWDContinue_login.clicked.connect(self.FetchMasterPasswordLogin)
        self.CloseMasterPWDWindow_login.clicked.connect(self.close)
        
    def FetchMasterPasswordLogin(self):
        MasterPassword = self.MasterPassword_login.text()
        return MasterPassword

def main():
    color = QColor('#351392')
    setThemeColor(color ,Qt.GlobalColor , '') 
    app = QApplication(sys.argv)
    window = MainWindow() 
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()