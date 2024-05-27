import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QHBoxLayout, QSpacerItem, QSizePolicy, QAbstractItemView, QMessageBox
from .Ui_Vault_interface import Ui_Form
from qfluentwidgets import setTheme, setThemeColor, FluentWindow, CheckBox, PushButton, ToggleButton

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QColor
import csv
import os
from .cipher_decipher_logic.CipherDecipher import get_password_no_form 

class MainWindow(Ui_Form, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.MainTable.setStyleSheet("QTableWidget { border: 1px solid gray; selection-background-color: #AF9BE5;  }")
        self.MainTable.setEditTriggers(QAbstractItemView.NoEditTriggers) 
        self.FetchPasswords_Button.clicked.connect(self.fetch_passwords)
        self.Flush_TextEdit.clicked.connect(self.flush)
        self.Fill_Table()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.Fill_Table)
        self.timer.start(10000)
        
        
    def flush(self):
        self.output_TextEdit.setText('')
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
                
    def fetch_passwords(self):
        selectedIPS = []
        for row in range(self.MainTable.rowCount()):
            items = self.MainTable.cellWidget(row, 2)
            checkbox_select = items.findChild(CheckBox)
            if checkbox_select is not None and checkbox_select.isChecked():
                ip_address_item = self.MainTable.item(row, 1)
                if ip_address_item is not None:
                    selectedIPS.append(ip_address_item.text())
        if not selectedIPS:
            no_ip_error_dialog()
        else:
            for ip in selectedIPS:
                CSV_File_Path = 'machines.csv'
                with open(CSV_File_Path, 'r') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        if row['ip_add'] == ip: 
                            username = row['linux_username']
                            password = row['password']
                            Ip = row['ip_add']
                            masterpassword = self.MasterPassword_input.text()
                            deciphered_pass = get_password_no_form(masterpassword, password)
                            Final_output = f"{Ip} {username} {deciphered_pass}"
                            self.output_TextEdit.append(Final_output)

def no_ip_error_dialog():
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Critical)
    msg_box.setText(f"No IP selected")
    msg_box.setWindowTitle("Error")
    msg_box.setStandardButtons(QMessageBox.Cancel)
    msg_box.setDefaultButton(QMessageBox.Cancel)
    result = msg_box.exec_()
# def main():
#     app = QApplication(sys.argv)
#     color = QColor('#351392')
#     setThemeColor(color.name(), Qt.GlobalColor, '') 
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())

# if __name__ == "__main__":
#     main()