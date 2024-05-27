import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QHBoxLayout, QSpacerItem, QSizePolicy, QAbstractItemView, QMessageBox, QLineEdit
from .Ui_RemoveMachinesInterface import Ui_Form
from qfluentwidgets import setTheme, setThemeColor, FluentWindow, CheckBox, PushButton, ToggleButton, TreeWidget, PrimaryPushButton
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox, QAbstractItemView, QDialog, QInputDialog
from .cipher_decipher_logic.CipherDecipher import check_password
from configparser import ConfigParser
import os
from pathlib import Path
import subprocess
import csv
import threading
import shutil

class MainWindow(Ui_Form, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.RemoveMachinesButton.clicked.connect(self.Delete_machines)
        self.MainTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.MainTable.setStyleSheet("QTableWidget { border: 1px solid gray; selection-background-color: #AF9BE5;}")
        self.Fill_Table()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.Fill_Table)
        self.timer.start(10000)

    def Fill_Table(self):
        self.MainTable.setRowCount(0)
        CSV_File_Path = 'machines.csv'
        with open(CSV_File_Path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                MachineName = row['Machine_Name']
                hostname = row['ip_add']
                rowPositionMachines = self.MainTable.rowCount()
                self.MainTable.insertRow(rowPositionMachines)
                self.MainTable.setItem(rowPositionMachines, 0, QTableWidgetItem(MachineName))
                self.MainTable.setItem(rowPositionMachines, 1, QTableWidgetItem(hostname))
                # Create a widget to contain the buttons
                buttons_widget = QWidget()
                buttons_layout = QHBoxLayout(buttons_widget)
                buttons_layout.setAlignment(Qt.AlignCenter)
                spacer = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Fixed)
                buttons_layout.addItem(spacer)
                Checkbox_select = CheckBox()
                Checkbox_select.setCheckable(True)
                buttons_layout.addWidget(Checkbox_select)
                buttons_layout.setContentsMargins(0, 0, 0, 0)
                buttons_widget.setLayout(buttons_layout)
                self.MainTable.setCellWidget(rowPositionMachines, 2, buttons_widget)
                
    def prompt_master_password(self):
        master_password, ok = QInputDialog.getText(self, 'Master Password', 'Enter Master Password:', QLineEdit.Password)
        if ok:
            return master_password
        else:
            return None          
    def Delete_machines(self):
        masterpassword = self.prompt_master_password()
        if check_password(masterpassword):
            selectedIPS = []
            selected_machine_names = []
            for row in range(self.MainTable.rowCount()):
                items = self.MainTable.cellWidget(row, 2)
                checkbox_select = items.findChild(CheckBox)
                if checkbox_select is not None and checkbox_select.isChecked():
                    ip_address_item = self.MainTable.item(row, 1)
                    machine_name_item = self.MainTable.item(row, 0)
                    if ip_address_item is not None:
                        selectedIPS.append(ip_address_item.text())
                        selected_machine_names.append(machine_name_item.text())
            print(selected_machine_names)
            if not selectedIPS:
                no_ip_error_dialog()
                return
            CSV_File_Path = 'machines.csv'
            temp_csv_file_path = 'temp_machines.csv'
            with open(CSV_File_Path, 'r') as file:
                reader = csv.DictReader(file)
                fieldnames = reader.fieldnames
                rows_to_keep = [row for row in reader if row['ip_add'] not in selectedIPS]
                
            with open(temp_csv_file_path, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(rows_to_keep)
            
            os.remove(CSV_File_Path)
            os.rename(temp_csv_file_path, CSV_File_Path)
            
            for machine_name in selected_machine_names:
                directory_path = fr'C:\ProgramData\REMT\{machine_name}'
                print(directory_path)
                if os.path.exists(directory_path):
                    shutil.rmtree(directory_path)
                        
        self.Fill_Table()
                    
def no_ip_error_dialog():
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Critical)
    msg_box.setText(f"No IP selected")
    msg_box.setWindowTitle("Error")
    msg_box.setStandardButtons(QMessageBox.Cancel)
    msg_box.setDefaultButton(QMessageBox.Cancel)
    result = msg_box.exec_()
def main():
    app = QApplication(sys.argv)
    color = QColor('#351392')
    setThemeColor(color.name(), Qt.GlobalColor, '') 
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

# if __name__ == "__main__":
#     main()