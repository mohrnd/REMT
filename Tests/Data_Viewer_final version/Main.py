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
    def __init__(self, Machine_Name, Machine_Ip):
        super().__init__()
        self.setupUi(self)
        self.Machine_Name = Machine_Name
        self.Machine_Ip = Machine_Ip
        self.FillData()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.FillData)
        self.timer.start(10000)  # 10000 milliseconds -> 10 seconds

    def FillData(self):
        # change the filepath !!!!
        filepath = f"..\REMT\Tests\data_viewer (DONT USE ME)\{self.Machine_Name}.json"
        
        
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
            
        self.TimestampLabel.setText(f" As of {timestamp}")
        self.MachineName.setText(self.Machine_Name)
        self.MachineIP.setText(self.Machine_Ip)
        self.Uptime.setText(uptime)
        self.TotalDisk.setText(disk_total)
        self.CpuCores.setText(cpu_cores)
        self.TotalRam.setText(ram_total)
        self.Nics.setText(nic_names)
        self.TotalCachedMemory.setText(total_cached_memory)
        self.TotalSwap.setText(total_swap)
        self.AvailableSwap.setText(available_swap)
        self.NetworkOut.setText(data_out)
        self.NetworkIn.setText(data_in)


        self.CPUusagering.setProperty("value", cpu_usage)
        self.RAMusagering.setProperty("value", ram_usage)
        self.Diskusagering.setProperty("value", disk_usage)
        load_1min = float(load_1min) * 100
        load_5min = float(load_5min) * 100
        load_15min = float(load_15min) * 100
        self.min1LoadRing.setProperty("value", load_1min)
        self.min5LoadRing.setProperty("value", load_5min)
        self.min15LoadRing.setProperty("value", load_15min)
        
    def plot_graphs(self):
        '''
        last hour
        last 24 hours
        
        '''
        pass
    def plot_custom_graphs(self):
        StartDate = self.StartDate.text()
        EndDate = self.EndDate.text()
        start_time = self.StartTime.time.toString()
        end_time = self.EndTime.time.toString()
        Ticks = self.TicksForm.text() 
        print(StartDate, EndDate, start_time, end_time, Ticks)
        '''
        
        '''
        pass
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
    window = MainWindow('SERVER1', '192.168.69.40') 
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
