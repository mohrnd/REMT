import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem
from Ui_CrontabGUI import Ui_Frame  
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from qfluentwidgets import (NavigationItemPosition, MessageBox, setTheme, setThemeColor, Theme, FluentWindow,
                            NavigationAvatarWidget, SubtitleLabel, setFont, InfoBadge,
                            InfoBadgePosition, CheckBox)
from TaskScheduler import *
import os

class MainWindow(QWidget, Ui_Frame):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.add_button.clicked.connect(self.test)
        self.Apply.clicked.connect(self.Apply)
        
    def show_active_crons(self):
        pass
    
    def show_active_machines(self):
        pass
    
    def Check_ip(hostname):
        param = '-n' if os.name.lower() == 'nt' else '-c'
        response = os.system(f"ping {param} 1 -w 100 {hostname} > NUL 2>&1")   # 100 ms wait time, might change it later
        if response == 0:
            return True
        else:
            return False
    
    
    
    
    def Apply(self):
        selectedIPS = []
        for row in range(self.Machines.rowCount()):
            checkbox_item = self.Machines.cellWidget(row, 2)
            if isinstance(checkbox_item, CheckBox) and checkbox_item.isChecked():
                ip_address_item = self.Machines.item(row, 0)
                if ip_address_item is not None:
                    selectedIPS.append(ip_address_item.text())
        print(selectedIPS)
        
        ### add the add_cron method
    

    def test(self):
        text = self.minute_input.text()
        if text == '':
            print('*')
        else: 
            print(text)
            
        # insert data in the machines table (get data from the csv file)
        rowPositionMachines = self.Machines.rowCount()
        self.Machines.insertRow(rowPositionMachines)
        # Set data for the new row in Machines table
        self.Machines.setItem(rowPositionMachines, 0, QTableWidgetItem(text))
        self.Machines.setItem(rowPositionMachines, 1, QTableWidgetItem('Machine 1'))
        
        checkbox = CheckBox()  
        checkbox.setChecked(False)
        self.Machines.setCellWidget(rowPositionMachines, 2, checkbox)  # Set the CheckBox widget in the table cell


def main():
    
    color = QColor('#351392')
    setThemeColor(color ,Qt.GlobalColor , '') 
    
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()

