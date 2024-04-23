import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox, QAbstractItemView
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import *
from qfluentwidgets import (TimePicker, NavigationItemPosition, MessageBox, setTheme, setThemeColor, Theme, FluentWindow,
                            NavigationAvatarWidget, SubtitleLabel, setFont, InfoBadge,
                            InfoBadgePosition, CheckBox, PushButton, PrimaryPushButton)
from Ui_Main_data_viewer_window import Ui_Form
from PyQt5.QtWidgets import QMainWindow
import json

class MainWindow(QMainWindow, Ui_Form):
    def __init__(self, Machine_Name):
        super().__init__()
        self.setupUi(self)
        self.MachineName.setText("something")
        self.CPUusagering.setProperty("value", 50)




def convert_to_gb_or_mb(value):
    value = int(value)
    if value >= 1024 * 1024: 
        return f"{value / (1024 * 1024):.2f} GB"
    elif value >= 1024: 
        return f"{value / 1024:.2f} MB"
    else:
        return f"{value} KB"

def convert_uptime(uptime_hundredths):
    uptime_seconds = int(uptime_hundredths) / 100  # Convert to seconds
    if uptime_seconds < 60:
        return f"{uptime_seconds:.2f} seconds"
    elif uptime_seconds < 3600:
        uptime_minutes = uptime_seconds / 60
        return f"{uptime_minutes:.2f} minutes"
    elif uptime_seconds < 86400:
        uptime_hours = uptime_seconds / 3600
        return f"{uptime_hours:.2f} hours"
    else:
        uptime_days = uptime_seconds / 86400
        return f"{uptime_days:.2f} days"

def main():
    color = QColor('#351392')
    setThemeColor(color ,Qt.GlobalColor , '') 
    app = QApplication(sys.argv)
    window = MainWindow('SERVER1') 
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
