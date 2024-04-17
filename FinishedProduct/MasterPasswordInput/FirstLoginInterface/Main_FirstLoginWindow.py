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

class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("REMT Initial Login")
        self.setWindowIcon(QIcon("../REMT/FinishedProduct/MasterPasswordInput/FirstLoginInterface/black.png"))

def main():
    color = QColor('#351392')
    setThemeColor(color ,Qt.GlobalColor , '') 
    app = QApplication(sys.argv)
    window = MainWindow() 
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()