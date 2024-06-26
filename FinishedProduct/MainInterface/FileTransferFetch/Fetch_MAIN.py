import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog,QTableWidgetItem, QHBoxLayout, QSpacerItem, QSizePolicy, QAbstractItemView, QMessageBox
from qfluentwidgets import setTheme, setThemeColor, FluentWindow, CheckBox, PushButton, ToggleButton
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QColor
import csv
import os
from .Ui_Fetch import Ui_Frame
from .file_transfer import Transfer
from .Exec_cmds_remote import run_ssh_command
from .cipher_decipher_logic.AES_cipher_decipher import get_password_no_form


class MainWindow(Ui_Frame, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.MainTable.setStyleSheet("QTableWidget { border: 1px solid gray; selection-background-color: #AF9BE5;  }")
        self.MainTable.setEditTriggers(QAbstractItemView.NoEditTriggers) 
        self.Fetch_button.clicked.connect(self.Fetch)
        self.Browse.clicked.connect(self.browse_files)
        self.PushButton.clicked.connect(self.verify_remote_path)
        
        # Connect the signal to update the master password variable
        self.Master_password.textChanged.connect(self.update_master_password)
        
        self.password_entered = ""
        self.show_active_machines()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.show_active_machines)
        self.timer.start(10000)
    def update_master_password(self, text):
        self.password_entered = text
        
    def show_active_machines(self):
        self.MainTable.setRowCount(0)
        
        # Load online machines from machines_online.csv
        online_csv_file = 'machines_online.csv'
        online_machines = set()
        if os.path.exists(online_csv_file):
            with open(online_csv_file, 'r') as file:
                csv_reader = csv.reader(file)
                for row in csv_reader:
                    if row:
                        online_machines.add((row[0], row[1]))  # Add (Machine_Name, ip_add) to the set
        
        # Load all machines from machines.csv and check if they are online
        CSV_File_Path = 'machines.csv'
        with open(CSV_File_Path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                MachineName = row['Machine_Name']
                hostname = row['ip_add']
                
                # Check if the machine is in the online_machines set
                if (MachineName, hostname) in online_machines:
                    rowPositionMachines = self.MainTable.rowCount()
                    self.MainTable.insertRow(rowPositionMachines)
                    self.MainTable.setItem(rowPositionMachines, 0, QTableWidgetItem(MachineName))
                    self.MainTable.setItem(rowPositionMachines, 1, QTableWidgetItem(hostname))
                    
                    # Create a widget to contain the buttons
                    buttons_widget = QWidget()
                    buttons_layout = QHBoxLayout(buttons_widget)
                    buttons_layout.setAlignment(Qt.AlignCenter)
                    
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
    def Fetch(self):
        
        password_entered = self.password_entered
        if not password_entered:
            QMessageBox.warning(self, "Warning", "Please enter a password.")
            return
        
        localpath = self.Localpath.text()
        if localpath == '':
            no_localpath_error_dialog()
        else:
            # filename = os.path.basename(localpath) #gets the filename
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
                outputs = []
                for hostname in selectedIPS:
                    CSV_File_Path = 'machines.csv'
                    with open(CSV_File_Path, 'r') as file:
                        reader = csv.DictReader(file)
                        for row in reader:
                            if row['ip_add'] == hostname: 
                                remotepath = self.LineEdit.text()
                                username = row['linux_username']
                                ciphered_password = row['password']
                                password1 = get_password_no_form(password_entered,ciphered_password)
                                password=password1
                                if remotepath == '':
                                    General_info_dialog('Remote path empty')
                                else:
                                    temppath = self.Localpath.text()
                                    filename = os.path.basename(remotepath) #gets the filename
                                    localpath = f'{temppath}/{filename}'
                                    temp = Transfer()
                                    output = temp.GET(hostname, username, password, localpath, remotepath)
                                    outputs.append(f'{output} at {hostname}')
                                    break
                
                General_info_dialog('\n'.join(outputs))



    def browse_files(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        folder = QFileDialog.getExistingDirectory(self, "Select Folder", "", options=options)
        if folder:
            self.Localpath.setText(str(folder))

        
    def verify_remote_path(self):
        
        password_entered = self.password_entered
        if not password_entered:
            QMessageBox.warning(self, "Warning", "Please enter a password.")
            return
        
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
            path = self.LineEdit.text()
            not_found_ips = []  
            for hostname in selectedIPS:
                CSV_File_Path = 'machines.csv'
                with open(CSV_File_Path, 'r') as file:
                    reader = csv.DictReader(file)
                    path_found = False
                    for row in reader:
                        if row['ip_add'] == hostname:
                            username = row['linux_username']
                            ciphered_password = row['password']
                            password1 = get_password_no_form(password_entered,ciphered_password)
                            password=password1
                            command = f'[ -f "{path}" ] && echo "True" || echo "False"'
                            output = run_ssh_command(hostname, username, password, command)
                            if output.strip() == 'True':
                                path_found = True
                                break
                    if not path_found:
                        not_found_ips.append(hostname)
            if not_found_ips:
                General_info_dialog('Path not found on machines: ' + ', '.join(not_found_ips))
            else:
                General_info_dialog('Path found on all selected machines!')

def no_ip_error_dialog():
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Critical)
    msg_box.setText(f"No IP selected")
    msg_box.setWindowTitle("Error")
    msg_box.setStandardButtons(QMessageBox.Cancel)
    msg_box.setDefaultButton(QMessageBox.Cancel)
    result = msg_box.exec_()
    
def General_info_dialog(info):
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Information)
    msg_box.setText(info)
    msg_box.setWindowTitle("Info")
    msg_box.setStandardButtons(QMessageBox.Ok)
    msg_box.setDefaultButton(QMessageBox.Ok)
    result = msg_box.exec_()

def no_localpath_error_dialog():
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Critical)
    msg_box.setText(f"No file selected")
    msg_box.setWindowTitle("Error")
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