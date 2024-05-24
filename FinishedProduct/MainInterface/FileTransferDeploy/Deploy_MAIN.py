import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog,QTableWidgetItem, QHBoxLayout, QSpacerItem, QSizePolicy, QAbstractItemView, QMessageBox
from qfluentwidgets import setTheme, setThemeColor, FluentWindow, CheckBox, PushButton, ToggleButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
import csv
import os
from .Ui_Deploy import Ui_Frame
from .file_transfer import Transfer
from .Exec_cmds_remote import run_ssh_command
from .cipher_decipher_logic.AES_cipher_decipher import get_password_no_form

class MainWindow(Ui_Frame, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.MainTable.setStyleSheet("QTableWidget { border: 1px solid gray; selection-background-color: #AF9BE5;  }")
        self.MainTable.setEditTriggers(QAbstractItemView.NoEditTriggers) 
        self.show_active_machines()
        self.Deploy_button.clicked.connect(self.Deploy)
        self.Broswse.clicked.connect(self.browse_files)
        self.PushButton.clicked.connect(self.verify_remote_path)
        
        # Connect the signal to update the master password variable
        self.Master_password.textChanged.connect(self.update_master_password)
        
        self.password_entered = ""
        
    def update_master_password(self, text):
        self.password_entered = text
        
    def show_active_machines(self):
        CSV_File_Path = '../REMT/FinishedProduct/MainInterface/FileTransferFetch/user.csv'
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
    def Deploy(self):
        
        password_entered = self.password_entered
        if not password_entered:
            QMessageBox.warning(self, "Warning", "Please enter a password.")
            return
        
        localpath = self.Localpath.text()
        if localpath == '':
            no_localpath_error_dialog()
        else:
            filename = os.path.basename(localpath) #gets the filename
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
                    CSV_File_Path = '../REMT/FinishedProduct/MainInterface/FileTransferFetch/user.csv'
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
                                    remotepath = f'/home/{username}/remt/{filename}'
                                else:
                                    temppath = self.LineEdit.text()
                                    remotepath = f'{temppath}/{filename}'
                                temp = Transfer()
                                output = temp.PUT(hostname, username, password, localpath, remotepath)
                                outputs.append(f'{output} at {hostname}')
                                break
                
                General_info_dialog('\n'.join(outputs))



    def browse_files(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self, "Select File(s)", "", "All Files (*);;Python Files (*.py);;Shell Files (*.sh)", options=options)
        if files:
            self.Localpath.setText(str(files[0]))
        
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
                CSV_File_Path = '../REMT/FinishedProduct/MainInterface/FileTransferFetch/user.csv'
                with open(CSV_File_Path, 'r') as file:
                    reader = csv.DictReader(file)
                    path_found = False
                    for row in reader:
                        if row['ip_add'] == hostname:
                            username = row['linux_username']
                            ciphered_password = row['password']
                            password1 = get_password_no_form(password_entered,ciphered_password)
                            password=password1
                            command = f'[ -d "{path}" ] && echo "True" || echo "False"'
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
    

def main():
    app = QApplication(sys.argv)
    color = QColor('#351392')
    setThemeColor(color.name(), Qt.GlobalColor, '') 
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()