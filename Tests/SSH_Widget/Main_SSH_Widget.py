import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QHBoxLayout, QSpacerItem, QSizePolicy, QAbstractItemView
from Ui_main import Ui_Frame
from qfluentwidgets import setTheme, setThemeColor, FluentWindow, CheckBox, PushButton, ToggleButton

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
import csv
import os
class MainWindow(Ui_Frame, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show_active_machines()
        # self.MainTable.setShowGrid(True)
        self.MainTable.setStyleSheet("QTableWidget { border: 1px solid gray; selection-background-color: #AF9BE5;  }")
        self.MainTable.setEditTriggers(QAbstractItemView.NoEditTriggers) 
    def show_active_machines(self):
        CSV_File_Path = '../REMT/Tests/task_scheduling/snmp_users.csv'
        with open(CSV_File_Path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                MachineName = row['Machine_Name']
                hostname = row['ip_add']
                stat = Check_ip(hostname)
                if stat:
                    rowPositionMachines = self.MainTable.rowCount()
                    self.MainTable.insertRow(rowPositionMachines)
                    self.MainTable.setItem(rowPositionMachines, 0, QTableWidgetItem(MachineName))
                    self.MainTable.setItem(rowPositionMachines, 1, QTableWidgetItem(hostname))
                    # Create a widget to contain the buttons
                    buttons_widget = QWidget()
                    buttons_layout = QHBoxLayout(buttons_widget)
                    buttons_layout.setAlignment(Qt.AlignCenter)
                    
                    # PushButton
                    push_button = PushButton("Open terminal")
                    push_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                    buttons_layout.addWidget(push_button)
                    
                    # Spacer
                    spacer = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Fixed)
                    buttons_layout.addItem(spacer)
                    
                    # ToggleButton
                    toggle_button = ToggleButton("Select")
                    toggle_button.setCheckable(True)
                    toggle_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                    buttons_layout.addWidget(toggle_button)
                    
                    buttons_layout.setContentsMargins(0, 0, 0, 0)
                    buttons_widget.setLayout(buttons_layout)

                    self.MainTable.setCellWidget(rowPositionMachines, 2, buttons_widget)
                    
def Check_ip(hostname):
    param = '-n' if os.name.lower() == 'nt' else '-c'
    response = os.system(f"ping {param} 1 -w 100 {hostname} > NUL 2>&1")   # 100 ms wait time, might change it later
    if response == 0:
        return True
    else:
        return False


def main():
    app = QApplication(sys.argv)
    color = QColor('#351392')
    setThemeColor(color.name(), Qt.GlobalColor, '') 
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
