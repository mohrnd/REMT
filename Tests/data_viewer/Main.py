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
        self.FillTables()
        

    def PlotData(self):
        StartDate = self.StartDate.text()
        EndDate = self.EndDate.text()
        start_time = self.TimePicker_4.time.toString()
        end_time = self.TimePicker_3.time.toString()
        Ticks = self.TicksForm.text() 
        print(StartDate, EndDate, start_time, end_time, Ticks)
        
    def FillTables(self):
        # this is just temporary, i will make it fetch the latest value from the json file later 
        timestamp_value = "2024-04-11 10:00:00"
        uptime_value = "2 days"
        cpu_usage_value = "40%"
        ram_usage_value = "60%"
        disk_usage_value = "80%"
        network_up_value = "100 KB/s"
        network_down_value = "200 KB/s"
        
        cpu_cores_value = "2"
        total_ram_value = "7 GB"
        total_disk_value = "30 GB"
        network_cards_values = "eth0, t0"
    
        timestamp_item = QTableWidgetItem(timestamp_value)
        uptime_item = QTableWidgetItem(uptime_value)
        cpu_usage_item = QTableWidgetItem(cpu_usage_value)
        ram_usage_item = QTableWidgetItem(ram_usage_value)
        disk_usage_item = QTableWidgetItem(disk_usage_value)
        network_up_item = QTableWidgetItem(network_up_value)
        network_down_item = QTableWidgetItem(network_down_value)
        
        cpu_cores_item = QTableWidgetItem(cpu_cores_value)
        total_ram_item = QTableWidgetItem(total_ram_value)
        total_disk_item = QTableWidgetItem(total_disk_value)
        network_cards_item = QTableWidgetItem(network_cards_values)
        
    
        self.TableWidget_2.setItem(0, 0, timestamp_item)
        self.TableWidget_2.setItem(1, 0, uptime_item)
        self.TableWidget_2.setItem(2, 0, cpu_usage_item)
        self.TableWidget_2.setItem(3, 0, ram_usage_item)
        self.TableWidget_2.setItem(4, 0, disk_usage_item)
        self.TableWidget_2.setItem(5, 0, network_up_item)
        self.TableWidget_2.setItem(6, 0, network_down_item)
        
        self.TableWidget.setItem(0, 0, cpu_cores_item)
        self.TableWidget.setItem(1, 0, total_ram_item)
        self.TableWidget.setItem(2, 0, total_disk_item)
        self.TableWidget.setItem(3, 0, network_cards_item)
        
def main():
    color = QColor('#351392')
    setThemeColor(color ,Qt.GlobalColor , '') 
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())



if __name__ == "__main__":
    main()