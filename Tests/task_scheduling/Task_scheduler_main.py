import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem
from Ui_CrontabGUI import Ui_Frame  
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from qfluentwidgets import (NavigationItemPosition, MessageBox, setTheme, setThemeColor, Theme, FluentWindow,
                            NavigationAvatarWidget, SubtitleLabel, setFont, InfoBadge,
                            InfoBadgePosition, CheckBox)
class MainWindow(QWidget, Ui_Frame):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.add_button.clicked.connect(self.test)
        
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
