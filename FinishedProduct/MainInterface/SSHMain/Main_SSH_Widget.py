import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QHBoxLayout, QSpacerItem, QSizePolicy, QAbstractItemView, QMessageBox,QDialogButtonBox,QDialog,QVBoxLayout, QLabel,QLineEdit
from qfluentwidgets import setTheme, setThemeColor, FluentWindow, CheckBox, PushButton, ToggleButton,PasswordLineEdit
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QColor
import csv
import os
from .SingleSSH import SSHWidget
from .MultiSSH import MultiSSHWidget, MultiSSHWindow
from .Ui_main import Ui_Frame
from .cipher_decipher_logic.AES_cipher_decipher import get_password_no_form
# The dot (.) in the import statement indicates that you want to import the module relative to the current package or directory.


class MainWindow(Ui_Frame, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.MainTable.setStyleSheet("QTableWidget { border: 1px solid gray; selection-background-color: #AF9BE5;  }")
        self.MainTable.setEditTriggers(QAbstractItemView.NoEditTriggers) 
        self.OpenMultiSSH.clicked.connect(self.MultiSSH)
        self.single_ssh_window = [] 
        self.multi_ssh_window = None 
        
        # Add the Masterpassword_input field
        self.master_password_input = PasswordLineEdit(self)
        self.master_password_input.setPlaceholderText("Master password")
        self.password_entered = None 
        self.master_password_input.setGeometry(10, 770, 570, 80) 
        
        # Connect the signal to update the master password variable
        self.master_password_input.textChanged.connect(self.update_master_password) 
        
        self.MainTable.setColumnWidth(2, 200)  # Définir la largeur de la colonne "Actions" sur 200 pixels
        
        # Ajuster la largeur de toute la table
        self.MainTable.setMinimumWidth(780)
        
        # Ajuster la hauteur de toute la table
        self.MainTable.setMinimumHeight(500)
        
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
    
                    # PushButton
                    OpenTerminal = PushButton("Open terminal")  # Changed to QPushButton
                    OpenTerminal.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                    buttons_layout.addWidget(OpenTerminal)
                    # Connect the clicked signal with a lambda function passing the IP address
                    OpenTerminal.clicked.connect(lambda checked, ip=hostname: self.SingleSSH(ip))
                    
                    # Spacer
                    spacer = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Fixed)
                    buttons_layout.addItem(spacer)
                    
                    # Checkbox
                    Checkbox_select = CheckBox()  # Changed to QCheckBox
                    Checkbox_select.setCheckable(True)
                    buttons_layout.addWidget(Checkbox_select)
                    
                    buttons_layout.setContentsMargins(0, 0, 0, 0)
                    buttons_widget.setLayout(buttons_layout)

                    self.MainTable.setCellWidget(rowPositionMachines, 2, buttons_widget)
    
        
    def MultiSSH(self):
        
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
            hosts = []
            master_password_error = False
            print(selectedIPS)
            for ip in selectedIPS:
                CSV_File_Path = 'machines.csv'
                with open(CSV_File_Path, 'r') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        if row['ip_add'] == ip: 
                            username = row['linux_username']
                            ciphered_password = row['password']
                            Machine_Name = row['Machine_Name']
                            password1 = get_password_no_form(password_entered, ciphered_password)
                            if password1 == 'REMTM@$terP@$$w0rdErr0r':
                                master_password_error = True
                                break
                            else:
                                password = password1
                                temp = [ip, username, password, Machine_Name]
                                hosts.append(temp.copy())  
                            break
                if master_password_error:
                    break
            
            if master_password_error:
                return
            
            if len(hosts) < 2:
                multissh_error_dialog()
                print(len(hosts))
                print(hosts)
            else:
                self.multi_ssh_window = MultiSSHWindow(hosts)
                self.multi_ssh_window.show()
                
            
    def SingleSSH(self, ip_address):
        
        password_entered = self.password_entered
        if not password_entered:
            QMessageBox.warning(self, "Warning", "Please enter a password.")
            return
        
        hostname = ip_address
        CSV_File_Path = 'machines.csv'
        with open(CSV_File_Path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['ip_add'] == hostname: 
                    username = row['linux_username']
                    ciphered_password = row['password']      
                    password1 = get_password_no_form(password_entered, ciphered_password)
                    if password1 == 'REMTM@$terP@$$w0rdErr0r':
                        return
                    else:
                        password = password1
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


def main():
    app = QApplication(sys.argv)
    color = QColor('#351392')
    setThemeColor(color.name(), Qt.GlobalColor, '') 
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
