# coding:utf-8
import sys

from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QIcon, QDesktopServices
from PyQt5.QtWidgets import QApplication, QFrame, QHBoxLayout, QWidget
from qfluentwidgets import (NavigationItemPosition, MessageBox, setTheme, setThemeColor,Theme, MSFluentWindow,
                            NavigationAvatarWidget, qrouter, SubtitleLabel, setFont)
from qfluentwidgets import FluentIcon as FIF
from PyQt5.QtGui import *
from MainInterface.TaskSchedulerMain.Task_scheduler_main import MainWindow as SchedulerWindow
# dont forget to add a dot to the files you want to import
from MainInterface.SSHMain.Main_SSH_Widget import MainWindow as SSHWindow
from MainInterface.editeur_de_code.editeur import MainWindowWidget as editeurwindow
from MainInterface.MainDashboard.Main import MainWindow as Dashboard
from MainInterface.log_fetcher_interface.Main import MainWindow as LogFetcher
from MainInterface.Passwordvault.Main import MainWindow as Passvault
from MainInterface.adding_machines.adding_machines_forms_main import MainWindow as MachineAdder
from MainInterface.FileTransferDeploy.Deploy_MAIN import MainWindow as Deploy
from MainInterface.FileTransferFetch.Fetch_MAIN import MainWindow as Fetch
from MainInterface.Trapsviewer.Main_Trap_Viewer import MainWindow as TrapsViewer
class TaskScheduler(QWidget):
#Task Scheduler
    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.hBoxLayout = QHBoxLayout(self)
        self.Scheduler = SchedulerWindow()  
        self.hBoxLayout.addWidget(self.Scheduler)  
        self.setObjectName(text.replace('-', '-'))
        
class SSH(QWidget):
    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.hBoxLayout = QHBoxLayout(self)
        self.SSH = SSHWindow()
        self.hBoxLayout.addWidget(self.SSH)
        self.setObjectName(text.replace('-', '-'))

class code_editeur(QWidget):
    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.hBoxLayout = QHBoxLayout(self)
        self.code_editeur = editeurwindow()  
        self.hBoxLayout.addWidget(self.code_editeur)  
        self.setObjectName(text.replace('-', '-'))


class New_Dashboard(QWidget):
    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.hBoxLayout = QHBoxLayout(self)
        self.dashboard = Dashboard()  
        self.hBoxLayout.addWidget(self.dashboard)  
        self.setObjectName(text.replace('-', '-'))

class New_LogFetcher(QWidget):
    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.hBoxLayout = QHBoxLayout(self)
        self.logfetcher = LogFetcher()  
        self.hBoxLayout.addWidget(self.logfetcher)  
        self.setObjectName(text.replace('-', '-'))


class New_PassVault(QWidget):
    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.hBoxLayout = QHBoxLayout(self)
        self.passvault = Passvault()  
        self.hBoxLayout.addWidget(self.passvault)  
        self.setObjectName(text.replace('-', '-'))
        
class New_MachineAdder(QWidget):
    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.hBoxLayout = QHBoxLayout(self)
        self.widget = MachineAdder()  
        self.hBoxLayout.addWidget(self.widget)  
        self.setObjectName(text.replace('-', '-'))
        
class New_Deploy(QWidget):
    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.hBoxLayout = QHBoxLayout(self)
        self.widget = Deploy()  
        self.hBoxLayout.addWidget(self.widget)  
        self.setObjectName(text.replace('-', '-'))

class New_Fetch(QWidget):
    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.hBoxLayout = QHBoxLayout(self)
        self.widget = Fetch()  
        self.hBoxLayout.addWidget(self.widget)  
        self.setObjectName(text.replace('-', '-'))
        
class New_TrapsViewer(QWidget):
    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.hBoxLayout = QHBoxLayout(self)
        self.widget = TrapsViewer()  
        self.hBoxLayout.addWidget(self.widget)  
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

        self.Dashboard = New_Dashboard(text='Dashboard', parent=self)
        self.SSH_window = SSH(text='Single', parent=self)
        self.TaskScheduler = TaskScheduler(text='Scheduler', parent=self)
        self.CodeEditor = code_editeur(text='code_editeur', parent=self)
        self.LogFetcher = New_LogFetcher(text='Log', parent=self)
        self.DeployFile = New_Deploy(text='Deploy', parent=self)
        self.GetFile = New_Fetch(text='Fetch', parent=self)
        self.ViewTraps = New_TrapsViewer(text='Traps', parent=self)
        self.AddMachine = New_MachineAdder(text='machineadder', parent=self)
        self.PasswordVault = New_PassVault(text='Pass', parent=self)
        self.initNavigation()
        self.initWindow()

    def initNavigation(self):
        self.addSubInterface(self.Dashboard, QIcon(r'..\REMT\FinishedProduct\MainInterface\RemtIcons\dashboard.svg'), 'Dashboard')
        self.addSubInterface(self.SSH_window, QIcon(r'..\REMT\FinishedProduct\MainInterface\RemtIcons\SSH.svg'), 'SSH')
        self.addSubInterface(self.TaskScheduler, QIcon(r'..\REMT\FinishedProduct\MainInterface\RemtIcons\schedule.svg'), 'Scheduler')
        self.addSubInterface(self.CodeEditor, QIcon(r'..\REMT\FinishedProduct\MainInterface\RemtIcons\codeEditor.svg'), 'Code Editor')
        self.addSubInterface(self.LogFetcher, QIcon(r'..\REMT\FinishedProduct\MainInterface\RemtIcons\logs.svg'), 'Log Fetcher')
        self.addSubInterface(self.DeployFile, QIcon(r'..\REMT\FinishedProduct\MainInterface\RemtIcons\upload.svg'), 'Deploy')
        self.addSubInterface(self.GetFile, QIcon(r'..\REMT\FinishedProduct\MainInterface\RemtIcons\download.svg'), 'Fetch')
        self.addSubInterface(self.ViewTraps, QIcon(r'..\REMT\FinishedProduct\MainInterface\RemtIcons\view.svg'), 'View Traps')
        self.addSubInterface(self.PasswordVault, QIcon(r'..\REMT\FinishedProduct\MainInterface\RemtIcons\password.svg'), 'Vault')
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
