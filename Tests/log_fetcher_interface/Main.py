import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QHBoxLayout, QSpacerItem, QSizePolicy, QAbstractItemView, QMessageBox
from Ui_logfetcher_interface import Ui_Form
from qfluentwidgets import setTheme, setThemeColor, FluentWindow, CheckBox, PushButton, ToggleButton, TreeWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QTimer
from LOGS.fetch_logs import fetch
# self.fetch('localhost','192.168.1.21','../REMT/Tests/LOGS/var/')

class MainWindow(Ui_Form, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.hBoxLayout = QHBoxLayout(self)
        self.hBoxLayout.addWidget(self.TreeWidget)
        self.hBoxLayout.setContentsMargins(15, 15, 15, 15)
        self.TreeWidget.setBorderVisible(True)
        self.TreeWidget.setBorderRadius(8)
        

def main():
    app = QApplication(sys.argv)
    color = QColor('#351392')
    setThemeColor(color.name(), Qt.GlobalColor, '') 
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
