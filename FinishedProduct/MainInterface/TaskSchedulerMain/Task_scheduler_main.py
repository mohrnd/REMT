import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox, QAbstractItemView, QDialog, QInputDialog
from .Ui_CrontabGUI import Ui_Frame  
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from qfluentwidgets import (NavigationItemPosition, MessageBox, setTheme, setThemeColor, Theme, FluentWindow,
                            NavigationAvatarWidget, SubtitleLabel, setFont, InfoBadge,
                            InfoBadgePosition, CheckBox, PushButton, PasswordLineEdit)
from .TaskScheduler import *
import os
import csv
from .cron_interpreter import interpret_schedule
import datetime
from .cipher_decipher_logic.CipherDecipher import *
import threading

class MainWindow(QWidget, Ui_Frame):
    def __init__(self, Masterpassword):
        super().__init__()
        self.setupUi(self)
        self.Masterpassword = Masterpassword
        self.TableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Machines.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Machines.setStyleSheet("QTableWidget { border: 1px solid gray; selection-background-color: #AF9BE5;}")
        self.TableWidget.setStyleSheet("QTableWidget { border: 1px solid gray; selection-background-color: #AF9BE5;}")

        self.show_active_crons()
        self.add_button.clicked.connect(self.Add_to_preview)
        self.Apply.clicked.connect(self.Apply_cron)

        self.Onstartup.clicked.connect(self.on_startup_clicked)
        self.hourly.clicked.connect(self.hourly_clicked)
        self.Daily_2.clicked.connect(self.daily_clicked)
        self.weekly_2.clicked.connect(self.weekly_clicked)
        self.monthly_2.clicked.connect(self.monthly_clicked)
        self.PushButton_5.clicked.connect(self.yearly_clicked)
                
                
        self.show_active_machines()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.show_active_machines)
        self.timer.start(10000)

    def prompt_master_password(self):
        master_password, ok = QInputDialog.getText(self, 'Master Password', 'Enter Master Password:', QLineEdit.Password)
        if ok:
            return master_password
        else:
            return None

    def show_active_crons(self):
        CSV_File_Path = 'machines.csv'
        with open(CSV_File_Path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Check = row['ip_add']
                if Check_ip(Check):
                    hostname = row['ip_add']
                    port = 22
                    username = row['linux_username']
                    ciphered_password = row['password']
                    password = get_password_no_form(self.Masterpassword, ciphered_password)
                    if password:
                        ssh_client = ssh_client_creation(hostname, port, username, password)
                        lines = print_active_jobs(ssh_client)
                        if lines:
                            cron_list = lines.split('\n')
                            for cron_job in cron_list:
                                rowPositionMachines = self.TableWidget.rowCount()
                                self.TableWidget.insertRow(rowPositionMachines)
                                self.TableWidget.setItem(rowPositionMachines, 0, QTableWidgetItem(hostname))
                                self.TableWidget.setItem(rowPositionMachines, 1, QTableWidgetItem(cron_job))
                                schedule_expression, command = splitter(cron_job)
                                inter, Next_exec = interpret_schedule(schedule_expression)
                                self.TableWidget.setItem(rowPositionMachines, 2, QTableWidgetItem(str(Next_exec)))
                                self.TableWidget.setItem(rowPositionMachines, 3, QTableWidgetItem(inter))
                                DeleteButton = PushButton('Delete')
                                self.TableWidget.setCellWidget(rowPositionMachines, 4, DeleteButton)
                                self.connect_delete_button(DeleteButton)
                        ssh_client.close()
                else:
                    pass

    def show_active_machines(self):
        self.Machines.setRowCount(0)
        
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
                    rowPositionMachines = self.Machines.rowCount()
                    self.Machines.insertRow(rowPositionMachines)
                    self.Machines.setItem(rowPositionMachines, 0, QTableWidgetItem(hostname))
                    self.Machines.setItem(rowPositionMachines, 1, QTableWidgetItem(MachineName))
                    
                    # Create checkbox
                    checkbox = CheckBox()  # Changed to QCheckBox
                    checkbox.setChecked(False)
                    self.Machines.setCellWidget(rowPositionMachines, 2, checkbox)

    def Apply_cron(self):
        master_password = self.prompt_master_password()
        if not master_password:
            return

        selectedIPS = []
        for row in range(self.Machines.rowCount()):
            checkbox_item = self.Machines.cellWidget(row, 2)
            if isinstance(checkbox_item, CheckBox) and checkbox_item.isChecked():
                ip_address_item = self.Machines.item(row, 0)
                if ip_address_item is not None:
                    selectedIPS.append(ip_address_item.text())
        if selectedIPS == []:
            no_ip_error_dialog()
        else:
            preview_text = self.Preview.toPlainText()
            preview_lines = preview_text.split('\n')
            job = preview_lines[0]
            for IP in selectedIPS:
                CSV_File_Path = 'machines.csv'
                with open(CSV_File_Path, 'r') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        if row['ip_add'] == IP:
                            hostname = IP
                            port = 22
                            username = row['linux_username']
                            ciphered_password = row['password']
                            password = get_password_no_form(master_password, ciphered_password)
                            if password:
                                ssh_client = ssh_client_creation(hostname, port, username, password)
                                add_cron(ssh_client, job)
                                ssh_client.close()
                                rowPositionMachines = self.TableWidget.rowCount()
                                self.TableWidget.insertRow(rowPositionMachines)
                                self.TableWidget.setItem(rowPositionMachines, 0, QTableWidgetItem(hostname))
                                self.TableWidget.setItem(rowPositionMachines, 1, QTableWidgetItem(job))
                                schedule_expression, command = splitter(job)
                                inter, Next_exec = interpret_schedule(schedule_expression)
                                self.TableWidget.setItem(rowPositionMachines, 2, QTableWidgetItem(str(Next_exec)))
                                self.TableWidget.setItem(rowPositionMachines, 3, QTableWidgetItem(inter))
                                DeleteButton = PushButton('Delete')
                                self.TableWidget.setCellWidget(rowPositionMachines, 4, DeleteButton)
                                self.connect_delete_button(DeleteButton)
                            break

    def delete_cron(self):
        master_password = self.prompt_master_password()
        if not master_password:
            return

        sender_button = self.sender()
        for table_row in range(self.TableWidget.rowCount()):
            delete_button = self.TableWidget.cellWidget(table_row, 4)
            if sender_button == delete_button:
                ip_address_item = self.TableWidget.item(table_row, 0)
                job_item = self.TableWidget.item(table_row, 1)
                if ip_address_item and job_item:
                    ip_address = ip_address_item.text()
                    job = job_item.text()
                    CSV_File_Path = 'machines.csv'
                    with open(CSV_File_Path, 'r') as file:
                        reader = csv.DictReader(file)
                        for row in reader:
                            if row['ip_add'] == ip_address:
                                username = row['linux_username']
                                ciphered_password = row['password']
                                password = get_password_no_form(master_password, ciphered_password)
                                if password:
                                    ssh_client = ssh_client_creation(ip_address, 22, username, password)
                                    remove_cron(ssh_client, job)
                                    ssh_client.close()
                                    self.TableWidget.removeRow(int(table_row))
                                break

    def connect_delete_button(self, button):
        button.clicked.connect(self.delete_cron)

    def Add_to_preview(self):
        # add value checking
        Months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
        Weekdays = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
        if self.Command_input.text() == '':
            no_cmd_error_dialog()
        else:
            Minutes = '*' if not self.minute_input.text() else self.minute_input.text()
            Hours = '*' if not self.hour_input.text() else self.hour_input.text()
            Days = '*' if not self.day_input.text() else self.day_input.text()
            months = '*' if not self.month_input.text() else self.month_input.text()
            weekdays = '*' if not self.LineEdit.text() else self.LineEdit.text()
            cmd = self.Command_input.text()
            inter, Next_exec = interpret_schedule(f'{Minutes} {Hours} {Days} {months} {weekdays}')
            self.Preview.setText(f"{Minutes} {Hours} {Days} {months} {weekdays} {cmd} \n Next execution: {Next_exec.strftime('%Y-%m-%d %H:%M:%S')} \n Interpretation: {inter}")

    def on_startup_clicked(self):
        cmd = self.Command_input.text()
        if cmd == '':
            no_cmd_error_dialog()
        else:
            inter, Next_exec = interpret_schedule(f'@reboot')
            self.Preview.setText(f"@reboot {cmd}\n Next execution: {Next_exec} \n Interpretation: {inter}")

    def hourly_clicked(self):
        cmd = self.Command_input.text()
        if cmd == '':
            no_cmd_error_dialog()
        else:
            inter, Next_exec = interpret_schedule(f'@hourly')
            self.Preview.setText(f"@hourly {cmd} \n Next execution: {Next_exec.strftime('%Y-%m-%d %H:%M:%S')} \n Interpretation: {inter}")

    def daily_clicked(self):
        cmd = self.Command_input.text()
        if cmd == '':
            no_cmd_error_dialog()
        else:
            inter, Next_exec = interpret_schedule(f'@daily')
            self.Preview.setText(f"@daily {cmd} \n Next execution: {Next_exec.strftime('%Y-%m-%d %H:%M:%S')} \n Interpretation: {inter}")

    def weekly_clicked(self):
        cmd = self.Command_input.text()
        if cmd == '':
            no_cmd_error_dialog()
        else:
            inter, Next_exec = interpret_schedule(f'@weekly')
            self.Preview.setText(f"@weekly {cmd} \n Next execution: {Next_exec.strftime('%Y-%m-%d %H:%M:%S')} \n Interpretation: {inter}")

    def monthly_clicked(self):
        cmd = self.Command_input.text()
        if cmd == '':
            no_cmd_error_dialog()
        else:
            inter, Next_exec = interpret_schedule(f'@monthly')
            self.Preview.setText(f"@monthly {cmd} \n Next execution: {Next_exec.strftime('%Y-%m-%d %H:%M:%S')} \n Interpretation: {inter}")

    def yearly_clicked(self):
        cmd = self.Command_input.text()
        if cmd == '':
            no_cmd_error_dialog()
        else:
            inter, Next_exec = interpret_schedule(f'@yearly')
            self.Preview.setText(f"@yearly {cmd} \n Next execution: {Next_exec.strftime('%Y-%m-%d %H:%M:%S')} \n Interpretation: {inter}")

def no_ip_error_dialog():
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Critical)
    msg_box.setText(f"No IP selected")
    msg_box.setWindowTitle("Error")
    msg_box.setStandardButtons(QMessageBox.Cancel)
    msg_box.setDefaultButton(QMessageBox.Cancel)
    result = msg_box.exec_()

def no_cmd_error_dialog():
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Critical)
    msg_box.setText(f"No Command/path entered")
    msg_box.setWindowTitle("Error")
    msg_box.setStandardButtons(QMessageBox.Cancel)
    msg_box.setDefaultButton(QMessageBox.Cancel)
    result = msg_box.exec_()

def value_error_dialog():
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Critical)
    msg_box.setText(f"Value error")
    msg_box.setWindowTitle("Error")
    msg_box.setStandardButtons(QMessageBox.Cancel)
    msg_box.setDefaultButton(QMessageBox.Cancel)
    result = msg_box.exec_()

def Check_ip(hostname):
    param = '-n' if os.name.lower() == 'nt' else '-c'
    response = os.system(f"ping {param} 1 -w 100 {hostname} > NUL 2>&1")  # 100 ms wait time, might change it later
    if response == 0:
        return True
    else:
        return False

def main():
    color = QColor('#351392')
    setThemeColor(color, Qt.GlobalColor, '')
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


# if __name__ == "__main__":
#     main()
    
    
