import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox, QAbstractItemView
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import *
from qfluentwidgets import (TimePicker, NavigationItemPosition, MessageBox, setTheme, setThemeColor, Theme, FluentWindow,
                            NavigationAvatarWidget, SubtitleLabel, setFont, InfoBadge,
                            InfoBadgePosition, CheckBox, PushButton, PrimaryPushButton)
from Ui_Main_Window_data_viewer import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow
import json

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, Machine_Name):
        super().__init__()
        self.setupUi(self)
        self.Machine_Name = Machine_Name  # Storing machine name
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
        self.SubtitleLabel.setText(f'Machine Name: {Machine_Name}')

        self.FillTables()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.FillTables)
        self.timer.start(5000)  # 5000 milliseconds -> 5 seconds
        

    def PlotData(self):
        StartDate = self.StartDate.text()
        EndDate = self.EndDate.text()
        start_time = self.TimePicker_4.time.toString()
        end_time = self.TimePicker_3.time.toString()
        Ticks = self.TicksForm.text() 
        print(StartDate, EndDate, start_time, end_time, Ticks)







    def FillTables(self):
        filepath = f"../REMT/tests/dashboard/{self.Machine_Name}.json"
        with open(filepath, 'r') as f:
            data = json.load(f)
            Latest_line = data[-1]
            
        timestamp = Latest_line['timestamp']
        load_1min = Latest_line['LOAD1min']
        load_5min = Latest_line['LOAD5min']
        load_15min = Latest_line['LOAD15min']
        cpu_cores = Latest_line['CPUcores']
        cpu_usage = Latest_line['CPUusage']
        ram_total = convert_to_gb_or_mb(Latest_line['RAMtotal'])
        ram_usage = Latest_line['RAMusage']
        disk_total = convert_to_gb_or_mb(Latest_line['DISKtotal'])
        disk_usage = Latest_line['DISKusage']
        uptime_hundredths = Latest_line['UPTIME']
        uptime = convert_uptime(uptime_hundredths)
                
        total_swap = convert_to_gb_or_mb(Latest_line['TotalSWAP'])
        available_swap = convert_to_gb_or_mb(Latest_line['AvailableSWAP'])
        total_cached_memory = convert_to_gb_or_mb(Latest_line['TotalCachedMemory'])
        nic_names = ', '.join(Latest_line['NICnames'])
        # data_out = ', '.join(Latest_line['dataOUT'])
        table = []
        for item in Latest_line['dataOUT']:
            converted = convert_to_gb_or_mb(item)
            table.append(converted)
            data_out = ', '.join(table)
        table2 = []
        for item in Latest_line['dataIN']:
            converted = convert_to_gb_or_mb(item)
            table2.append(converted)
            data_in = ', '.join(table2)

        loads = f'{load_1min}, {load_5min}, {load_15min}'
        timestamp_item = QTableWidgetItem(timestamp)
        loads_item = QTableWidgetItem(loads)
        cpu_cores_item = QTableWidgetItem(cpu_cores)
        cpu_usage_item = QTableWidgetItem(cpu_usage)
        ram_total_item = QTableWidgetItem(ram_total)
        ram_usage_item = QTableWidgetItem(ram_usage)
        disk_total_item = QTableWidgetItem(disk_total)
        disk_usage_item = QTableWidgetItem(disk_usage)
        uptime_item = QTableWidgetItem(uptime)
        total_swap_item = QTableWidgetItem(total_swap)
        available_swap_item = QTableWidgetItem(available_swap)
        total_cached_memory_item = QTableWidgetItem(total_cached_memory)
        nic_names_item = QTableWidgetItem(nic_names)
        data_in_item = QTableWidgetItem(data_in)
        data_out_item = QTableWidgetItem(data_out)
        
        self.TableWidget.setItem(0, 0, cpu_cores_item)
        self.TableWidget.setItem(1, 0, ram_total_item)
        self.TableWidget.setItem(2, 0, disk_total_item)
        self.TableWidget.setItem(3, 0, total_swap_item)
        self.TableWidget.setItem(4, 0, available_swap_item)
        self.TableWidget.setItem(5, 0, total_cached_memory_item)
        self.TableWidget.setItem(6, 0, nic_names_item)
        
        
        self.TableWidget_2.setItem(0, 0, timestamp_item)
        self.TableWidget_2.setItem(1, 0, uptime_item)
        self.TableWidget_2.setItem(2, 0, cpu_usage_item)
        self.TableWidget_2.setItem(3, 0, loads_item)
        self.TableWidget_2.setItem(4, 0, ram_usage_item)
        self.TableWidget_2.setItem(5, 0, disk_usage_item)
        self.TableWidget_2.setItem(6, 0, data_in_item)
        self.TableWidget_2.setItem(7, 0, data_out_item)

        

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
