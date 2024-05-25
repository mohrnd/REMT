import sys
import paramiko
import threading
import socket
import logging
import os
import re
from PyQt5.QtWidgets import QWidget, QTextEdit, QMessageBox, QApplication, QVBoxLayout, QPushButton, QCheckBox, QScrollArea,QLabel
from PyQt5.QtGui import QTextCursor, QFont, QIcon
from PyQt5.QtCore import Qt
from qfluentwidgets import PrimaryPushButton
from PyQt5.QtGui import QKeySequence,QKeyEvent

logging.basicConfig(filename='ssh2.log', level=logging.INFO, format='%(asctime)s - %(message)s')

PASSWORD_PROMPT_PATTERN = re.compile(r'[Pp]assword:?\s*$')

class MultiSSHWidget(QWidget):
    def __init__(self, hostname, username, password, Machine_Name, shared_text_edit):
        super().__init__()
        self.hostname = hostname
        self.username = username
        self.password = password
        self.Machine_Name = Machine_Name
        self.shared_text_edit = shared_text_edit
        self.layout = QVBoxLayout(self)

        font = QFont("Cairo Bold", 14)
        self.text_edit = QTextEdit(self)
        self.text_edit.setFont(font)
        self.text_edit.setFixedHeight(200)  # Taille fixe pour le widget
        self.buffer = ""
        self.letter_count = 0  # Variable pour compter les lettres entrées
        
        

        # Création des étiquettes pour l'adresse IP et le nom d'utilisateur
        self.ip_label = QLabel(f"IP: {self.hostname} Name: {self.Machine_Name}")

        # Définir une taille de police plus grande pour les étiquettes
        font = QFont()
        font.setPointSize(11)  # Changer la taille de police selon vos préférences
        self.ip_label.setFont(font)

        # Ajouter les étiquettes et le widget QTextEdit au layout
        self.layout.addWidget(self.ip_label)
        self.layout.addWidget(self.text_edit)

        self.setLayout(self.layout)

        self.ssh_client = None
        self.transport = None
        self.channel = None

        self.connect()

        # Checkbox
        self.checkbox = QCheckBox("Enable Text Input", checked=True) 
        self.layout.addWidget(self.checkbox)

        # Connect checkbox state change to toggle_input method
        self.checkbox.stateChanged.connect(self.toggle_input)

        # Ajout du bouton "Insert Password"
        self.password_button = PrimaryPushButton("Insert Password")
        self.password_button.setEnabled(False)  # Désactiver le bouton au démarrage
        self.password_button.setFixedWidth(191)
        self.password_button.clicked.connect(self.insert_password)
        self.layout.addWidget(self.password_button)

    def toggle_input(self, state):
        if state == Qt.Checked:
            self.shared_text_edit.addTerminal(self)
        else:
            self.shared_text_edit.removeTerminal(self)

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
            logging.error(f"SSH connection established by failed")
            self.show_connection_error_dialog()
        except socket.timeout:
            self.text_edit.append("Connection timed out while trying to connect to " + self.hostname)
            logging.error(f"Connection timed out while trying to connect to {self.hostname}")
            self.show_connection_error_dialog()

    def keyPressEvent(self, event):
        if self.shared_text_edit.isChecked():  
            for widget in self.shared_text_edit.terminals:
                if event.key() == Qt.Key_Backspace:
                    if widget.letter_count > 0:
                        widget.letter_count -= 1  # Décrémente la variable pour la touche de suppression
                        widget.buffer = widget.buffer[:-1]
                        cursor = widget.text_edit.textCursor()
                        cursor.deletePreviousChar()
                elif event.modifiers() == Qt.ControlModifier:
                    if event.key() == Qt.Key_C:  
                        clipboard = QApplication.clipboard()
                        selected_text = self.text_edit.textCursor().selectedText()
                        clipboard.setText(selected_text)
                    elif event.key() == Qt.Key_D:  
                        self.channel.send('\x04')
                    elif event.key() == Qt.Key_L:  
                        self.text_edit.clear()
                    elif event.key() == Qt.Key_V:  # Handle Ctrl+V (paste)
                        clipboard_text = QApplication.clipboard().text()
                        self.text_edit.insertPlainText(clipboard_text)
                        self.buffer += clipboard_text
                else:
                    widget.text_edit.insertPlainText(event.text())
                    if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
                        widget.channel.send(widget.buffer + "\n")
                        logging.info(f"Command executed in {widget.hostname}: {widget.buffer}")
                        widget.buffer = ""
                    else:
                        widget.buffer += event.text()
                        widget.letter_count += 1  # Incrémente la variable pour chaque lettre entrée
        else:  
            if event.key() == Qt.Key_Backspace:
                if self.letter_count > 0:
                    self.letter_count -= 1  # Décrémente la variable pour la touche de suppression
                    self.buffer = self.buffer[:-1]
                    cursor = self.text_edit.textCursor()
                    cursor.deletePreviousChar()
            elif event.modifiers() == Qt.ControlModifier:
                if event.key() == Qt.Key_C:  
                    clipboard = QApplication.clipboard()
                    selected_text = self.text_edit.textCursor().selectedText()
                    clipboard.setText(selected_text)
                elif event.key() == Qt.Key_D:  
                    self.channel.send('\x04')
                elif event.key() == Qt.Key_L:  
                    self.text_edit.clear()
                elif event.key() == Qt.Key_V:  # Handle Ctrl+V (paste)
                    clipboard_text = QApplication.clipboard().text()
                    self.text_edit.insertPlainText(clipboard_text)
                    self.buffer += clipboard_text
            else:
                self.text_edit.insertPlainText(event.text())
                if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
                    self.channel.send(self.buffer + "\n")
                    logging.info(f"Command executed in {self.hostname}: {self.buffer}")
                    self.buffer = ""
                else:
                    self.buffer += event.text()
                    self.letter_count += 1  # Incrémente la variable pour chaque lettre entrée

    def read_ssh_output(self):
        while True:
            try:
                x = self.channel.recv(1024)
                if not x:
                    break
                decoded_text = x.decode('utf-8', errors='ignore')
                filtered_text = self.filter_special_chars(decoded_text)
                self.update_text_edit(filtered_text)
                
                # Réinitialiser le compteur de lettres
                self.letter_count = 0
                
                # Si une invite de mot de passe est détectée, activer le bouton
                if ("[sudo] Mot de passe" in filtered_text or
                    "[sudo] password" in filtered_text or 
                    "Mot de passe" in filtered_text or
                    "password" in filtered_text):
                    self.enable_password_button()
                    
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
        msg_box.setText(f"Your password was incorrect \nFailed to connect to {self.hostname}")
        msg_box.setWindowTitle("Connection Error")
        msg_box.setStandardButtons(QMessageBox.Cancel)

        result = msg_box.exec_()
        # if result == QMessageBox.Retry:
        #     self.connect()
        # else:
        #     self.hide()
            #         # Retirer le terminal de l'affichage s'il est dans la liste des terminaux
            # if self in self.shared_text_edit.terminals:
            #     self.shared_text_edit.removeTerminal(self)

    def insert_password(self):
        # Stocker le mot de passe dans le buffer
        self.buffer = self.password

        # Afficher un message sans afficher le mot de passe
        self.text_edit.moveCursor(QTextCursor.End)  # Déplacer le curseur à la fin
        # self.text_edit.insertPlainText("Mot de passe inséré\n")
        
        # Afficher une boîte de dialogue pour confirmer l'insertion du mot de passe
        QMessageBox.information(self, "Password inserted", "The password was inserted successfully.")
        # Désactiver le bouton après l'insertion du mot de passe
        self.disable_password_button()

    def enable_password_button(self):
        self.password_button.setEnabled(True)

    def disable_password_button(self):
        self.password_button.setEnabled(False)


class MultiSSHWindow(QWidget):
    def __init__(self, hosts):
        super().__init__()
        self.hosts = hosts
        self.setWindowTitle("Multiple SSH Terminals")
        self.layout = QVBoxLayout(self)

        self.shared_text_edit = SharedTextEdit()

        for host in self.hosts:
            ssh_widget = MultiSSHWidget(host[0], host[1], host[2],host[3],self.shared_text_edit)
            self.layout.addWidget(ssh_widget)
            self.shared_text_edit.terminals.append(ssh_widget)
        self.toggle_button = QCheckBox("Toggle Input for All Terminals")
        self.toggle_button.stateChanged.connect(self.toggle_input)

        self.layout.addWidget(self.toggle_button)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidget(QWidget())
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.widget().setLayout(self.layout)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.scroll_area)
        self.setLayout(main_layout)
        self.setWindowIcon(QIcon(r'..\FinishedProduct\MasterPasswordInput\FirstLoginInterface\black.png'))

    def toggle_input(self, state):
        if state == Qt.Checked:
            self.shared_text_edit.setChecked(True)
        else:
            self.shared_text_edit.setChecked(False)

class SharedTextEdit:
    def __init__(self):
        self.terminals = []
        self.checked = False

    def isChecked(self):
        return self.checked

    def setChecked(self, value):
        self.checked = value

    def addTerminal(self, terminal):
        if terminal not in self.terminals:
            self.terminals.append(terminal)

    def removeTerminal(self, terminal):
        if terminal in self.terminals:
            self.terminals.remove(terminal)



