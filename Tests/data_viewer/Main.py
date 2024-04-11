import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox, QAbstractItemView
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from qfluentwidgets import (TimePicker, NavigationItemPosition, MessageBox, setTheme, setThemeColor, Theme, FluentWindow,
                            NavigationAvatarWidget, SubtitleLabel, setFont, InfoBadge,
                            InfoBadgePosition, CheckBox, PushButton)
from Ui_Main_Window_data_viewer import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.TableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers) 
        self.TableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers) 
        self.TableWidget.setStyleSheet("QTableWidget { border: 1px solid gray; selection-background-color: #AF9BE5;}")
        self.TableWidget_2.setStyleSheet("QTableWidget { border: 1px solid gray; selection-background-color: #AF9BE5;}")
        self.PlotButton.clicked.connect(self.PlotData)
        self.TimePicker_4 = TimePicker(self.centralwidget)
        self.TimePicker_4.setGeometry(QtCore.QRect(140, 230, 240, 30))
        self.TimePicker_4.setObjectName("TimePicker_4")
        self.TimePicker_3 = TimePicker(self.centralwidget)
        self.TimePicker_3.setGeometry(QtCore.QRect(140, 270, 240, 30))
        self.TimePicker_3.setObjectName("TimePicker_3")
        
        

    def PlotData(self):
        StartDate = self.StartDate.text()
        EndDate = self.EndDate.text()
        start_time = self.TimePicker_4.time.toString()
        end_time = self.TimePicker_3.time.toString()
        Ticks = self.TicksForm.text() 
        print(StartDate, EndDate, start_time, end_time, Ticks)
    
def main():
    color = QColor('#351392')
    setThemeColor(color ,Qt.GlobalColor , '') 
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())



if __name__ == "__main__":
    main()