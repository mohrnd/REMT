import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox, QAbstractItemView, QToolTip
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
from Ui_root_password_master_password_forms import show_widget_in_main_window


class StudentLogin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Student log in screen')
        self.show()


class Login(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('Login screen')
        btn = PushButton('Student Login', self)
        btn.setToolTip('This will log you in as a student')
        btn.move(10, 50)
        btn.clicked.connect(self.student_log)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Log in screen')
        self.show()

    def student_log(self):
        self.widget = StudentLogin()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Login()
    sys.exit(app.exec_())
