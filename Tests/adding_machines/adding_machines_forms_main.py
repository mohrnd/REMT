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

class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.IPAddress.textChanged.connect(self.start_ip_check_timer)
        self.ipstatusONLINE.hide()
        self.ipstatusOFFLINE.hide()
        self.ip_check_timer = QTimer(self)
        self.ip_check_timer.timeout.connect(self.check_ip_status)
        
    def start_ip_check_timer(self):
        self.ip_check_timer.start(1000) 
        
    def check_ip_status(self):
        ip_address = self.IPAddress.text()
        
        if ip_address:
            if Check_ip(ip_address):
                self.ipstatusONLINE.show()
                self.ipstatusOFFLINE.hide()
            else:
                self.ipstatusONLINE.hide()
                self.ipstatusOFFLINE.show()
        else:
            self.ipstatusONLINE.hide()
            self.ipstatusOFFLINE.hide()
        
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