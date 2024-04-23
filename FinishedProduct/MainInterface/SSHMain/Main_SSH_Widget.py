import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QHBoxLayout, QSpacerItem, QSizePolicy, QAbstractItemView, QMessageBox,QDialogButtonBox,QDialog,QVBoxLayout, QLabel,QLineEdit
from .Ui_main import Ui_Frame
from qfluentwidgets import setTheme, setThemeColor, FluentWindow, CheckBox, PushButton, ToggleButton

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
import csv
import os
from .SingleSSH import SSHWidget
from .MultiSSH import MultiSSHWidget, MultiSSHWindow
# The dot (.) in the import statement indicates that you want to import the module relative to the current package or directory.


class MainWindow(Ui_Frame, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show_active_machines()
        self.MainTable.setStyleSheet("QTableWidget { border: 1px solid gray; selection-background-color: #AF9BE5;  }")
        self.MainTable.setEditTriggers(QAbstractItemView.NoEditTriggers) 
        self.OpenMultiSSH.clicked.connect(self.MultiSSH)
        self.single_ssh_window = [] 
        self.multi_ssh_window = None  
        
        self.MainTable.setColumnWidth(2, 915)  # Définir la largeur de la colonne "Actions" sur 200 pixels
        
        # Ajuster la largeur de toute la table
        self.MainTable.setMinimumWidth(1280)
        
        # Ajuster la hauteur de toute la table
        self.MainTable.setMinimumHeight(350)
        
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
                    OpenTerminal = PushButton("Open terminal")
                    OpenTerminal.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                    buttons_layout.addWidget(OpenTerminal)
                    # Connect the clicked signal with a lambda function passing the IP address
                    OpenTerminal.clicked.connect(lambda checked, ip=hostname: self.SingleSSH(ip))
                    
                    # Spacer
                    spacer = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Fixed)
                    buttons_layout.addItem(spacer)
                    
        
                    
                    # Checkbox
                    Checkbox_select = CheckBox()
                    Checkbox_select.setCheckable(True)
                    buttons_layout.addWidget(Checkbox_select)
                    
                    buttons_layout.setContentsMargins(0, 0, 0, 0)
                    buttons_widget.setLayout(buttons_layout)

                    self.MainTable.setCellWidget(rowPositionMachines, 2, buttons_widget)
    
    
    def MultiSSH(self):
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
            hosts = []
            for ip in selectedIPS:
                CSV_File_Path = '../REMT/Tests/task_scheduling/snmp_users.csv'
                with open(CSV_File_Path, 'r') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        if row['ip_add'] == ip: 
                            username = row['linux_username']
                            password = row['password']
                            temp = [ip, username, password]
                            hosts.append(temp.copy())  
                            break
            if len(hosts) < 2:
                multissh_error_dialog()
            else:
                self.multi_ssh_window = MultiSSHWindow(hosts)
                self.multi_ssh_window.show()
            
            
    def SingleSSH(self, ip_address):
        hostname = ip_address
        CSV_File_Path = '../REMT/Tests/task_scheduling/snmp_users.csv'
        with open(CSV_File_Path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['ip_add'] == hostname: 
                    username = row['linux_username']
                    password = row['password']
                    single_ssh_window = SSHWidget(hostname, username, password)
                    single_ssh_window.setGeometry(200, 200, 1200, 900) 
                    single_ssh_window.show()
                    return


def no_ip_error_dialog():
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Critical)
    msg_box.setText(f"No IP selected")
    msg_box.setWindowTitle("Error")
    msg_box.setStandardButtons(QMessageBox.Cancel)
    msg_box.setDefaultButton(QMessageBox.Cancel)
    result = msg_box.exec_()
    
def multissh_error_dialog():
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Warning)
    msg_box.setText(f"Please select 2 or more machines for multi-SSH")
    msg_box.setWindowTitle("Info")
    msg_box.setStandardButtons(QMessageBox.Cancel)
    msg_box.setDefaultButton(QMessageBox.Cancel)
    result = msg_box.exec_()
                    
def Check_ip(hostname):
    param = '-n' if os.name.lower() == 'nt' else '-c'
    response = os.system(f"ping {param} 1 -w 100 {hostname} > NUL 2>&1")   # 100 ms wait time, might change it later
    if response == 0:
        return True
    else:
        return False


# def main():
#     app = QApplication(sys.argv)
#     color = QColor('#351392')
#     setThemeColor(color.name(), Qt.GlobalColor, '') 
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())

# if __name__ == "__main__":
#     main()
