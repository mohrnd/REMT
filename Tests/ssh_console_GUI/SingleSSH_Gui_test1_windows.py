import sys
import paramiko
import threading
import socket
import logging
import os
import re
import msvcrt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit
from PyQt5.QtGui import QTextCursor
from PyQt5.QtCore import Qt

logging.basicConfig(filename='ssh2.log', level=logging.INFO, format='%(asctime)s - %(message)s')

PASSWORD_PROMPT_PATTERN = re.compile(r'[Pp]assword:?\s*$')

class SSHWindow(QMainWindow):
    def __init__(self, hostname, username, password):
        super().__init__()

        self.hostname = hostname
        self.username = username
        self.password = password

        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)
        self.buffer = ""

        self.ssh_client = None
        self.transport = None
        self.channel = None

        self.connect()

    def connect(self):
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            self.ssh_client.connect(self.hostname, username=self.username, password=self.password)
            current_user = os.getenv("USERNAME")
            logging.info(f"SSH connection established to {self.hostname} by user {current_user}")
            self.text_edit.append("SSH connection established to " + self.hostname)
            
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
            sys.exit(1)
        except paramiko.SSHException as e:
            self.text_edit.append("SSH connection failed to " + self.hostname + ": " + str(e))
            logging.error(f"SSH connection established by {current_user} failed {self.hostname}: {e}")
            sys.exit(1)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Backspace:
            self.buffer = self.buffer[:-1]  #remove the last character from the buffer
            cursor = self.text_edit.textCursor()
            cursor.deletePreviousChar()  #delete the last character from the text edit
        elif event.modifiers() == Qt.ControlModifier:
            if event.key() == Qt.Key_C:  #Ctrl C
                self.channel.send('\x03')
            elif event.key() == Qt.Key_D:  #Ctrl D
                self.channel.send('\x04')
        else:
            self.text_edit.insertPlainText(event.text())
            if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
                self.channel.send(self.buffer + "\n")
                self.buffer = ""
            else:
                self.buffer += event.text()

    def read_ssh_output(self):
        while True:
            try:
                x = self.channel.recv(1024)
                if not x:
                    break
                decoded_text = x.decode('utf-8', errors='ignore')
                filtered_text = self.filter_special_chars(decoded_text)
                self.update_text_edit(filtered_text)
            except socket.timeout:
                pass

    def filter_special_chars(self, text):
        filtered_text = re.sub(r'\x1b\[[^a-zA-Z]*[a-zA-Z]', '', text)
        
        return filtered_text

    def update_text_edit(self, text):
        self.text_edit.moveCursor(QTextCursor.End)
        self.text_edit.insertPlainText(text)
        self.text_edit.moveCursor(QTextCursor.End)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SSHWindow("192.168.69.44", "server1", "Pa$$w0rd")
    window.show()
    sys.exit(app.exec_())
import sys
import paramiko
import threading
import socket
import logging
import os
import re
import msvcrt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit
from PyQt5.QtGui import QTextCursor
from PyQt5.QtCore import Qt

logging.basicConfig(filename='ssh2.log', level=logging.INFO, format='%(asctime)s - %(message)s')

PASSWORD_PROMPT_PATTERN = re.compile(r'[Pp]assword:?\s*$')

class SSHWindow(QMainWindow):
    def __init__(self, hostname, username, password):
        super().__init__()

        self.hostname = hostname
        self.username = username
        self.password = password

        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)
        self.buffer = ""

        self.ssh_client = None
        self.transport = None
        self.channel = None

        self.connect()

    def connect(self):
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            self.ssh_client.connect(self.hostname, username=self.username, password=self.password)
            current_user = os.getenv("USERNAME")
            logging.info(f"SSH connection established to {self.hostname} by user {current_user}")
            self.text_edit.append("SSH connection established to " + self.hostname)
            
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
            sys.exit(1)
        except paramiko.SSHException as e:
            self.text_edit.append("SSH connection failed to " + self.hostname + ": " + str(e))
            logging.error(f"SSH connection established by {current_user} failed {self.hostname}: {e}")
            sys.exit(1)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Backspace:
            self.buffer = self.buffer[:-1]  # Remove the last character from the buffer
            cursor = self.text_edit.textCursor()
            cursor.deletePreviousChar()  # Delete the last character from the text edit
        elif event.modifiers() == Qt.ControlModifier:
            if event.key() == Qt.Key_C:  # Ctrl+C
                self.channel.send('\x03')
            elif event.key() == Qt.Key_D:  # Ctrl+D
                self.channel.send('\x04')
        else:
            self.text_edit.insertPlainText(event.text())
            if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
                self.channel.send(self.buffer + "\n")
                self.buffer = ""
            else:
                self.buffer += event.text()

    def read_ssh_output(self):
        while True:
            try:
                x = self.channel.recv(1024)
                if not x:
                    break
                decoded_text = x.decode('utf-8', errors='ignore')
                filtered_text = self.filter_special_chars(decoded_text)
                self.update_text_edit(filtered_text)
            except socket.timeout:
                pass

    def filter_special_chars(self, text):
        filtered_text = re.sub(r'\x1b\[[^a-zA-Z]*[a-zA-Z]', '', text)
        
        return filtered_text

    def update_text_edit(self, text):
        self.text_edit.moveCursor(QTextCursor.End)
        self.text_edit.insertPlainText(text)
        self.text_edit.moveCursor(QTextCursor.End)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SSHWindow("192.168.69.44", "server1", "Pa$$w0rd")
    window.show()
    sys.exit(app.exec_())


# TODO: FIX LOGGING, Detect nano/vim/ect.. input and print a message, make it more secure (use ssh keys), remove the "self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())"
