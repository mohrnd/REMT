# coding:utf-8
import sys

from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QIcon, QDesktopServices
from PyQt5.QtWidgets import QApplication, QFrame, QHBoxLayout
from qfluentwidgets import (NavigationItemPosition, MessageBox, setTheme, Theme, FluentWindow,
                            NavigationAvatarWidget, qrouter, SubtitleLabel, setFont, InfoBadge,
                            InfoBadgePosition)
from PyQt5.QtWidgets import QPushButton, QHBoxLayout
from SSH_Widget import SSHWidget 

class Widget(QFrame):

    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.label = SubtitleLabel(text, self)
        self.button = QPushButton('Upload Button', self)
        self.hBoxLayout = QHBoxLayout(self)
        setFont(self.label, 24)
        self.label.setAlignment(Qt.AlignCenter)
        self.hBoxLayout.addWidget(self.label, 1, Qt.AlignCenter)
        self.setObjectName(text.replace('', '-'))

class Widget1(QFrame):
#SSH WIDGET 
    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.hBoxLayout = QHBoxLayout(self)
        self.ssh_widget = SSHWidget("192.168.69.38", "manager1", "Pa$$w0rd")  # Provide appropriate hostname, username, and password
        self.hBoxLayout.addWidget(self.ssh_widget)  # Add SSHWidget to layout
        self.setObjectName(text.replace('-', '-'))

class Window(FluentWindow):

    def __init__(self):
        super().__init__()

        # create sub interface
        self.Dashboard = Widget('Dashboard', self)
        self.RemoteExecInt = Widget('RemoteExecInt', self)
        self.SingleSSH = Widget1('Single Channel', self)
        self.MultiSSH = Widget('MultiSSH', self)
        self.Schedule = Widget('Schedule', self)
        self.Txteditor = Widget('Txteditor', self)
        self.FileTransfer = Widget('FileTransfer', self)
        self.Logs = Widget('Logs', self)
        self.ViewLogs = Widget('ViewLogs', self)
        self.getsinglelogs = Widget('getsinglelogs', self)
        self.Scan = Widget('Scan', self)
        self.Fullscan = Widget('Fullscan', self)
        self.SpecificScan = Widget('SpecificScan', self)
        self.ViewScanRES = Widget('ViewScanRES', self)
        self.Settings = Widget('Settings', self)

        

        

        self.initNavigation()
        self.initWindow()

    def initNavigation(self):
        self.addSubInterface(self.Dashboard, QIcon(r'C:\Users\BALLS2 (rip BALLS)\Desktop\REST GUI\RestIcons\dashboard'), 'Dashboard')
        self.addSubInterface(self.RemoteExecInt, QIcon(r'C:\Users\BALLS2 (rip BALLS)\Desktop\REST GUI\RestIcons\SSH'), 'Remote execution', NavigationItemPosition.SCROLL)
        self.addSubInterface(self.SingleSSH, QIcon(r'C:\Users\BALLS2 (rip BALLS)\Desktop\REST GUI\RestIcons\singlechannel'), 'Single Channel', parent=self.RemoteExecInt)
        self.addSubInterface(self.MultiSSH, QIcon(r'C:\Users\BALLS2 (rip BALLS)\Desktop\REST GUI\RestIcons\multichannel'), 'Multi-Channel', parent=self.RemoteExecInt)
        self.addSubInterface(self.Schedule, QIcon(r'C:\Users\BALLS2 (rip BALLS)\Desktop\REST GUI\RestIcons\schedule'), 'Schedule', parent=self.RemoteExecInt)
        self.addSubInterface(self.Txteditor, QIcon(r'C:\Users\BALLS2 (rip BALLS)\Desktop\REST GUI\RestIcons\writescript'), 'Write a script', parent=self.RemoteExecInt)
        self.addSubInterface(self.FileTransfer, QIcon(r'C:\Users\BALLS2 (rip BALLS)\Desktop\REST GUI\RestIcons\updownarr'), 'Upload/Download a file', NavigationItemPosition.SCROLL)
        self.navigationInterface.addSeparator()
        
        self.addSubInterface(self.Logs, QIcon(r'C:\Users\BALLS2 (rip BALLS)\Desktop\REST GUI\RestIcons\logs'), 'Logs', NavigationItemPosition.SCROLL)
        self.addSubInterface(self.ViewLogs, QIcon(r''), 'View current', parent=self.Logs)
        self.addSubInterface(self.getsinglelogs, QIcon(r''), 'Get a machine\'s logs', parent=self.Logs)
        self.addSubInterface(self.Scan, QIcon(r'C:\Users\BALLS2 (rip BALLS)\Desktop\REST GUI\RestIcons\scan'), 'Scan', NavigationItemPosition.SCROLL)
        self.addSubInterface(self.Fullscan, QIcon(r'C:\Users\BALLS2 (rip BALLS)\Desktop\REST GUI\RestIcons\fullscan'), 'Full Scan', parent=self.Scan)
        self.addSubInterface(self.SpecificScan, QIcon(r'C:\Users\BALLS2 (rip BALLS)\Desktop\REST GUI\RestIcons\scansingle'), 'Scan a machine', parent=self.Scan)
        self.addSubInterface(self.ViewScanRES, QIcon(r'C:\Users\BALLS2 (rip BALLS)\Desktop\REST GUI\RestIcons\scansingle'), 'View scan results', parent=self.Scan)

        
        self.addSubInterface(self.Settings, QIcon(r'C:\Users\BALLS2 (rip BALLS)\Desktop\REST GUI\qfluenticons\Setting_black'), 'Settings', NavigationItemPosition.BOTTOM)




    def initWindow(self):
        self.resize(900, 700)
        self.setWindowIcon(QIcon(r'C:\Users\BALLS2 (rip BALLS)\Desktop\REST GUI\rest logo\black'))
        self.setWindowTitle('REMT')

        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)

        # set the minimum window width that allows the navigation panel to be expanded
        # self.navigationInterface.setMinimumExpandWidth(900)
        # self.navigationInterface.expand(useAni=False)




if __name__ == '__main__':
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    #setTheme(Theme.DARK)

    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec_()
