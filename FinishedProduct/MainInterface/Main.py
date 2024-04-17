# coding:utf-8
import sys

from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QIcon, QDesktopServices
from PyQt5.QtWidgets import QApplication, QFrame, QHBoxLayout, QWidget
from qfluentwidgets import (NavigationItemPosition, MessageBox, setTheme, setThemeColor,Theme, MSFluentWindow,
                            NavigationAvatarWidget, qrouter, SubtitleLabel, setFont)
from qfluentwidgets import FluentIcon as FIF
from PyQt5.QtGui import *
from TaskScheduler.Task_scheduler_main import *
from TaskScheduler import *
class TaskScheduler():
# #Task Scheduler
    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.hBoxLayout = QHBoxLayout(self)
        self.Scheduler = MainWindow()  # Provide appropriate hostname, username, and password
        self.hBoxLayout.addWidget(self.Scheduler)  # Add SSHWidget to layout
        self.setObjectName(text.replace('-', '-'))



class Widget(QFrame):

    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.label = SubtitleLabel(text, self)
        self.hBoxLayout = QHBoxLayout(self)

        setFont(self.label, 24)
        self.label.setAlignment(Qt.AlignCenter)
        self.hBoxLayout.addWidget(self.label, 1, Qt.AlignCenter)
        self.setObjectName(text.replace(' ', '-'))



class Window(MSFluentWindow):

    def __init__(self):
        super().__init__()

        self.Dashboard = Widget('Home Interface', self)
        self.SSH_window = Widget('Application Interface', self)
        self.TaskScheduler = TaskScheduler(self)
        self.CodeEditor = Widget('Video Interface 2', self)
        self.LogFetcher = Widget('Video Interface 3', self)
        self.DeployFile = Widget('Video Interface 4', self)
        self.GetFile = Widget('Video Interface 5', self)
        self.AddMachine = Widget('Video Interface 6', self)

        self.initNavigation()
        self.initWindow()

    def initNavigation(self):
        self.addSubInterface(self.Dashboard, QIcon(r'..\REMT\FinishedProduct\MainInterface\RemtIcons\dashboard.svg'), 'Dashboard')
        self.addSubInterface(self.SSH_window, QIcon(r'..\REMT\FinishedProduct\MainInterface\RemtIcons\SSH.svg'), 'SSH')
        self.addSubInterface(self.TaskScheduler, QIcon(r'..\REMT\FinishedProduct\MainInterface\RemtIcons\schedule.svg'), 'Scheduler')
        self.addSubInterface(self.CodeEditor, QIcon(r'..\REMT\FinishedProduct\MainInterface\RemtIcons\codeEditor.svg'), 'Code Editor')
        self.addSubInterface(self.LogFetcher, QIcon(r'..\REMT\FinishedProduct\MainInterface\RemtIcons\logs.svg'), 'Log Fetcher')
        self.addSubInterface(self.DeployFile, QIcon(r'..\REMT\FinishedProduct\MainInterface\RemtIcons\upload.svg'), 'Deploy')
        self.addSubInterface(self.GetFile, QIcon(r'..\REMT\FinishedProduct\MainInterface\RemtIcons\download.svg'), 'Get')
        self.addSubInterface(self.AddMachine, QIcon(r'..\REMT\FinishedProduct\MainInterface\RemtIcons\add.svg'), 'Add server')

        
        self.navigationInterface.addItem(
            routeKey='Help',
            icon=FIF.HELP,
            text='Help',
            onClick=self.showMessageBox,
            selectable=False,
            position=NavigationItemPosition.BOTTOM,
        )

        self.navigationInterface.setCurrentItem(self.Dashboard.objectName())
        
    def initWindow(self):
        self.resize(1200, 900)
        self.setWindowTitle("REMT Main Window")
        self.setWindowIcon(QIcon(r"..\REMT\FinishedProduct\MainInterface\black.png"))

        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)

    def showMessageBox(self):
        w = MessageBox(
            'Encountering any issues or have suggestions? Your feedback is invaluable!',
            'Please assist us in enhancing this project by reporting any problems or offering suggestions ',
            self
        )
        w.yesButton.setText('Github')
        w.cancelButton.setText('Cancel')

        if w.exec():
            QDesktopServices.openUrl(QUrl("https://github.com/mohrnd/REMT"))


if __name__ == '__main__':
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    color = QColor('#351392')
    setThemeColor(color ,Qt.GlobalColor , '') 

    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec_()
