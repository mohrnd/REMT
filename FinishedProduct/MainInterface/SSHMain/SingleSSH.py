import sys
import paramiko
import threading
import socket
import logging
import os
import re
from PyQt5.QtWidgets import QWidget, QTextEdit, QMessageBox, QVBoxLayout, QPushButton, QApplication
from PyQt5.QtGui import QTextCursor, QFont
from PyQt5.QtCore import Qt
from qfluentwidgets import PrimaryPushButton

logging.basicConfig(filename='ssh2.log', level=logging.INFO, format='%(asctime)s - %(message)s')

PASSWORD_PROMPT_PATTERN = re.compile(r'[Pp]assword:?\s*$')

class SSHWidget(QWidget):
    def __init__(self, hostname, username, password):
        super().__init__()
        self.hostname = hostname
        self.username = username
        self.password = password
        self.letter_count = 0

        font = QFont("Cairo Bold", 14)
        self.text_edit = QTextEdit(self)
        self.text_edit.setFont(font)
        self.text_edit.setGeometry(0, 0, 1200, 700)
        self.buffer = ""
        
        self.ssh_client = None
        self.transport = None
        self.channel = None

        self.init_ui()
        self.connect()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)

        self.password_button = PrimaryPushButton("Insert Password", self)
        self.password_button.clicked.connect(self.insert_password)
        self.password_button.setEnabled(False)
        self.password_button.setFixedWidth(191)
        layout.addWidget(self.password_button)

        self.setLayout(layout)

    def connect(self):
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            self.ssh_client.connect(self.hostname, username=self.username, password=self.password)
            current_user = os.getenv("USERNAME")
            logging.info(f"SSH connection established to {self.hostname} by user {current_user}")
            self.text_edit.append("SSH connection established to " + self.hostname +  " By " + current_user + "\r")
            
            self.transport = self.ssh_client.get_transport()
            self.channel = self.transport.open_session()
            self.channel.get_pty()
            self.channel.invoke_shell()

            output_thread = threading.Thread(target=self.read_ssh_output)
            output_thread.daemon = True
            output_thread.start()

            self.text_edit.keyPressEvent = self.keyPressEvent

        except paramiko.AuthenticationException:
            self.text_edit.append("Authentication failed for " + self.username + "@" + self.hostname)
            logging.error(f"Authentication failed for {self.username}@{self.hostname} established by {current_user}")
            self.show_connection_error_dialog()
        except paramiko.SSHException as e:
            self.text_edit.append("SSH connection failed to " + self.hostname + ": " + str(e))
            logging.error(f"SSH connection established by {current_user} failed {self.hostname}: {e}")
            self.show_connection_error_dialog()
        except socket.timeout:
            self.text_edit.append("Connection timed out while trying to connect to " + self.hostname)
            logging.error(f"Connection timed out while trying to connect to {self.hostname}")
            self.show_connection_error_dialog()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Backspace:
            if self.letter_count > 0:
                self.letter_count -= 1  
                self.buffer = self.buffer[:-1]  
                cursor = self.text_edit.textCursor()
                cursor.deletePreviousChar()  
        elif event.modifiers() == Qt.ControlModifier:
            if event.key() == Qt.Key_C:  
                self.channel.send('\x03')
            elif event.key() == Qt.Key_D:  
                self.channel.send('\x04')
            elif event.key() == Qt.Key_L:  
                self.text_edit.clear()
        else:
            self.text_edit.insertPlainText(event.text())
            if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
                if PASSWORD_PROMPT_PATTERN.search(self.buffer):
                    self.enable_password_button()  
                else:
                    self.channel.send(self.buffer + "\n")
                self.buffer = ""
            else:
                self.buffer += event.text()
                self.letter_count += 1  

    def read_ssh_output(self):
        while True:
            try:
                x = self.channel.recv(1024)
                if not x:
                    break
                decoded_text = x.decode('utf-8', errors='ignore')
                filtered_text = self.filter_special_chars(decoded_text)
                logging.info(f"Command output: {filtered_text}")
                self.update_text_edit(filtered_text)
                
                if ("[sudo] Mot de passe" in filtered_text or
                    "[sudo] password" in filtered_text or 
                    "Mot de passe" in filtered_text or
                    "password" in filtered_text):
                    self.enable_password_button()  
                else:
                    self.disable_password_button()  
                    
                self.letter_count = 0
                
            except socket.timeout:
                pass

    def filter_special_chars(self, text):
        filtered_text = re.sub(r'\x1b\[[^a-zA-Z]*[a-zA-Z]', '', text)
        return filtered_text

    def update_text_edit(self, text):
        self.text_edit.moveCursor(QTextCursor.End)
        self.text_edit.insertPlainText(text)
        self.text_edit.moveCursor(QTextCursor.End)

    def show_connection_error_dialog(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setText(f"Failed to connect to {self.hostname}")
        msg_box.setWindowTitle("Connection Error")
        msg_box.setStandardButtons(QMessageBox.Retry | QMessageBox.Cancel)
        msg_box.setDefaultButton(QMessageBox.Retry)

        result = msg_box.exec_()
        if result == QMessageBox.Retry:
            self.connect()
        else:
            sys.exit()

    def insert_password(self):
        self.buffer = self.password
        
        QMessageBox.information(self, "Password inserted", "The password was inserted successfully.")

        self.text_edit.moveCursor(QTextCursor.End)
        
        print("Contenu du buffer:", self.buffer)

        self.disable_password_button()

    def enable_password_button(self):
        self.password_button.setEnabled(True)

    def disable_password_button(self):
        self.password_button.setEnabled(False)



