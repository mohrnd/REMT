import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QHBoxLayout, QSpacerItem, QSizePolicy, QAbstractItemView, QMessageBox
from Ui_logfetcher_interface import Ui_Form
from qfluentwidgets import setTheme, setThemeColor, FluentWindow, CheckBox, PushButton, ToggleButton, TreeWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
import csv
import os
from PyQt5.QtCore import QTimer
from pyqt_translucent_full_loading_screen_thread import LoadingThread, LoadingTranslucentScreen
from PyQt5.QtCore import QTimer

class MainWindow(Ui_Form, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.EndCycle = False
        
        self.hBoxLayout = QHBoxLayout(self)
        self.hBoxLayout.addWidget(self.TreeWidget)
        self.hBoxLayout.setContentsMargins(50, 30, 50, 30)

        self.TreeWidget.setBorderVisible(True)
        self.TreeWidget.setBorderRadius(8)
        self.StartLoading('Loading')
    def StartLoading(self, message):
        self.__loadingTranslucentScreen = LoadingTranslucentScreen(parent=self, description_text=message)
        self.__loadingTranslucentScreen.setDescriptionLabelDirection('Right')
        self.__thread = LoadingThread(loading_screen=self.__loadingTranslucentScreen)
        self.__thread.start()



def main():
    app = QApplication(sys.argv)
    color = QColor('#351392')
    setThemeColor(color.name(), Qt.GlobalColor, '') 
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
