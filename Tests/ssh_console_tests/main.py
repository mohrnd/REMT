import sys
from PySide6.QtCore import QCoreApplication, QThread
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QGridLayout,
    QVBoxLayout,
    QTextEdit,
    QLineEdit,
    QPushButton,
)
import paramiko
import socket
import select
import tty
import termios
import os
import re

PASSWORD_PROMPT_PATTERN = re.compile(r'[Pp]assword:?\s*')

class SSHThread(QThread):
    def __init__(self, hostname, username, password, window):
        super().__init__()
        self.hostname = hostname
        self.username = username
        self.password = password
        self.window = window
        self.ssh_client = None

    def run(self):
        try:
            self.ssh_client = paramiko.SSHClient()
            self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh_client.connect(self.hostname, username=self.username, password=self.password)
            self.window.append_text(f"SSH connection established to {self.hostname}")
            self.window.append_text("")
            self.window.setFocus()
            transport = self.ssh_client.get_transport()
            self.channel = transport.open_session()
            self.channel.get_pty()
            self.channel.invoke_shell()
            self.shell()
        except paramiko.AuthenticationException:
            self.window.append_text(f"Authentication failed for {self.username}@{self.hostname}")
        except paramiko.SSHException as e:
            self.window.append_text(f"SSH connection failed to {self.hostname}: {e}")
        finally:
            if self.ssh_client:
                self.ssh_client.close()

    def shell(self):
        oldtty = termios.tcgetattr(sys.stdin)
        try:
            tty.setraw(sys.stdin.fileno())
            tty.setcbreak(sys.stdin.fileno())
            self.channel.settimeout(0.0)
            command_buffer = ""
            password_input = False
            while True:
                r, w, e = select.select([self.channel, sys.stdin], [], [])
                if self.channel in r:
                    try:
                        x = self.channel.recv(1024)
                        if len(x) == 0:
                            self.window.append_text("\r\n*** EOF\r\n")
                            break
                        if not password_input:
                            self.window.append_text(x.decode())
                        else:
                            pass
                        # self.window.repaint()
                        if not password_input and PASSWORD_PROMPT_PATTERN.search(x.decode()):
                            password_input = True
                    except socket.timeout:
                        pass
                if sys.stdin in r and not password_input:
                    x = sys.stdin.read(1)
                    if len(x) == 0:
                        break
                    elif x != '\r':
                        if 'sudo' not in command_buffer:
                            self.window.append_text(x)
                        self.channel.send(x.encode())
                        if x == '\r':
                            self.channel.send('\n'.encode())
                    else:
                        if 'sudo' not in command_buffer:
                            self.window.append_text(f"$ {command_buffer}")
                            self.window.repaint()
                        self.channel.send(command_buffer.encode() + b'\n')
                        command_buffer = ""
                if sys.stdin in r and password_input:
                    x = sys.stdin.read(1)
                    self.channel.send(b'\r\n')
                    password_input = False
                    continue
        finally:
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, oldtty)

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        print("Setting up UI...")
        self.setWindowTitle("SSH Terminal")
        self.resize(800, 600)

        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)

        self.gridLayout = QGridLayout(self.centralwidget)

        self.textEdit = QTextEdit()
        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 2)

        self.lineEdit = QLineEdit()
        self.gridLayout.addWidget(self.lineEdit, 1, 0)

        self.pushButton = QPushButton("Send")
        self.gridLayout.addWidget(self.pushButton, 1, 1)

        self.pushButton.clicked.connect(self.sendCommand)

        print("UI setup completed.")

    def sendCommand(self):
        command = self.lineEdit.text()
        self.textEdit.append(f"$ {command}")
        self.lineEdit.clear()

        if hasattr(self, 'ssh_thread') and self.ssh_thread.isRunning():
            self.ssh_thread.channel.send(command + '\n')

    def connectSSH(self, hostname, username, password):
        self.ssh_thread = SSHThread(hostname, username, password, self)
        self.ssh_thread.start()

    def append_text(self, text):
        self.textEdit.append(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.connectSSH("192.168.69.44", "server1", "Pa$$w0rd")
    print("Window setup completed.")
    window.show()
    print("Window shown.")
    sys.exit(app.exec_())
