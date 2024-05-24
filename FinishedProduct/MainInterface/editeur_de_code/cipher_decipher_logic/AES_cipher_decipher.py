from Cryptodome.Cipher import AES
from Cryptodome.Protocol.KDF import PBKDF2
import binascii
import os
from .LoginInterface.Ui_LoginMasterPasswordInput import Ui_Form
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox, QAbstractItemView
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import *
from qfluentwidgets import (TimePicker, NavigationItemPosition, MessageBox, setTheme, setThemeColor, Theme, FluentWindow,
                            NavigationAvatarWidget, SubtitleLabel, setFont, InfoBadge,
                            InfoBadgePosition, CheckBox, PushButton, PrimaryPushButton)
from PyQt5.QtWidgets import QWidget, QDialog
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
import hashlib


class MasterPasswordDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.MasterPWDContinue_login.clicked.connect(self.accept)
        self.ui.CloseMasterPWDWindow_login.clicked.connect(self.reject)

    def get_master_password(self):
        return self.ui.MasterPassword_login.text()

def get_master_password():
    app = QApplication([])
    color = QColor('#351392')
    setThemeColor(color.name(), Qt.GlobalColor, '') 
    dialog = MasterPasswordDialog()
    result = dialog.exec_()
    if result == QDialog.Accepted:
        master_password = dialog.get_master_password()
        return master_password
    else:
        return None

def derive_key_from_MasterPassword(MasterPassword, key_length=32):
    return PBKDF2(MasterPassword, b'', dkLen=key_length)

def encrypt_AES_GCM(Password, MasterPassword):
    secretKey = derive_key_from_MasterPassword(MasterPassword)
    aesCipher = AES.new(secretKey, AES.MODE_GCM)
    ciphertext, authTag = aesCipher.encrypt_and_digest(Password.encode('utf-8'))
    return (ciphertext, aesCipher.nonce, authTag)

def decrypt_AES_GCM(encryptedMsg, MasterPassword):
    (ciphertext, nonce, authTag) = encryptedMsg
    secretKey = derive_key_from_MasterPassword(MasterPassword)
    aesCipher = AES.new(secretKey, AES.MODE_GCM, nonce)
    plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
    return plaintext.decode('utf-8')

def create_vault_file(ciphertext, aesIV, authTag):
    file_path = 'C:\\ProgramData\\.Vault1851320.txt' 

    with open(file_path, 'a') as file:
        file.write(binascii.hexlify(ciphertext).decode('utf-8') + ',' + binascii.hexlify(aesIV).decode('utf-8') + ',' + binascii.hexlify(authTag).decode('utf-8') + '\n')
    try:
        os.system('attrib +H "{}"'.format(file_path))
        Multi_Purpose_info_dialog("Password file created successfully.")
    except Exception as e:
        Multi_Purpose_error_dialog(f"Error occurred while setting file attributes: {e}")


def add_new_entry(Password):
    MasterPassword = get_master_password()
    status = check_password(MasterPassword)
    if status == True:
        encryptedMsg = encrypt_AES_GCM(Password, MasterPassword)
        create_vault_file(*encryptedMsg) # Pass ciphertext, aesIV, and authTag separately
    else:
        Multi_Purpose_error_dialog('Your password was incorrect')
        pass


def get_password(CipheredPassword):
    MasterPassword = get_master_password()
    status = check_password(MasterPassword)
    if status == True:
        try:
            file_path = 'C:\\ProgramData\\.Vault1851320.txt'
            with open(file_path, 'r') as file:
                lines = file.readlines()
            for line in lines:
                components = line.strip().split(',')
                if CipheredPassword == components[0]:
                    encrypted_password = binascii.unhexlify(components[0])
                    aesIV = binascii.unhexlify(components[1])
                    authTag = binascii.unhexlify(components[2])
                    decrypted_password = decrypt_AES_GCM((encrypted_password, aesIV, authTag), MasterPassword)
                    return decrypted_password

            Multi_Purpose_error_dialog("CipheredPassword not found in the file.")
            return None
        except Exception as e:
            Multi_Purpose_error_dialog(f"Error occurred while getting password: {e}")
            return None
    else:
        Multi_Purpose_error_dialog('Your password was incorrect')
        pass
    
def get_password_no_form(MasterPassword,CipheredPassword):
    status = check_password(MasterPassword)
    if status == True:
        try:
            file_path = 'C:\\ProgramData\\.Vault1851320.txt'
            with open(file_path, 'r') as file:
                lines = file.readlines()
            for line in lines:
                components = line.strip().split(',')
                if CipheredPassword == components[0]:
                    encrypted_password = binascii.unhexlify(components[0])
                    aesIV = binascii.unhexlify(components[1])
                    authTag = binascii.unhexlify(components[2])
                    decrypted_password = decrypt_AES_GCM((encrypted_password, aesIV, authTag), MasterPassword)
                    Multi_Purpose_info_dialog("The file was successfully sent")
                    return decrypted_password

            Multi_Purpose_error_dialog("CipheredPassword not found in the file.")
            return None
        except Exception as e:
            Multi_Purpose_error_dialog(f"Error occurred while getting password: {e}")
            return None
    else:
        Multi_Purpose_error_dialog('Your password was incorrect')
        pass
        
def hash_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def create_password_file(hashed_password):
    file_path = 'C:\\ProgramData\\.Hash1851320.txt' 

    with open(file_path, 'w') as file:
        file.write(hashed_password)
    try:
        os.system('attrib +R +H +S "{}"'.format(file_path))
        Multi_Purpose_info_dialog("Password file created successfully.")

    except Exception as e:
        Multi_Purpose_error_dialog(f"Error occurred while setting file attributes: {e}")
        
def check_password(password):
    hashed_input = hash_password(password)
    file_path = 'C:\\ProgramData\\.Hash1851320.txt'

    with open(file_path, 'r') as file:
        stored_password = file.read().strip()

    if hashed_input == stored_password:
        return True
    else:
        return False

def Multi_Purpose_error_dialog(Message):
    app = QApplication.instance()  # Get the existing application instance
    if app is None:
        app = QApplication([])  # Create a new application instance if none exists
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Critical)
    msg_box.setText(Message)
    msg_box.setWindowTitle("Error")
    msg_box.setStandardButtons(QMessageBox.Ok)
    msg_box.setDefaultButton(QMessageBox.Ok)
    result = msg_box.exec_()
    
def Multi_Purpose_info_dialog(Message):
    app = QApplication.instance()  # Get the existing application instance
    if app is None:
        app = QApplication([])  # Create a new application instance if none exists
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Information)
    msg_box.setText(Message)
    msg_box.setWindowTitle("Information")
    msg_box.setStandardButtons(QMessageBox.Ok)
    msg_box.setDefaultButton(QMessageBox.Ok)
    result = msg_box.exec_()

# Usage 
# print(add_new_entry('Pa$$w0rd13')) 
#print(get_password('bd475a48a62ecc596ec7')) 


# hasher usage: 
# password = input("Enter the password to be hashed: ")
# hashed_password = hash_password(password)
# create_password_file(hashed_password)
# print(check_password(password))
# MASTERPASSWORD