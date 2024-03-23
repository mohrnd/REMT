# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\BALLS2 (rip BALLS)\Desktop\REMT\Tests\adding_machines\Add_machine.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QButtonGroup

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(581, 768)
        self.SubtitleLabel = SubtitleLabel(Form)
        self.SubtitleLabel.setGeometry(QtCore.QRect(10, 20, 141, 21))
        self.SubtitleLabel.setObjectName("SubtitleLabel")
        self.MachineName = LineEdit(Form)
        self.MachineName.setGeometry(QtCore.QRect(10, 60, 561, 33))
        self.MachineName.setObjectName("MachineName")
        self.IPAddress = LineEdit(Form)
        self.IPAddress.setGeometry(QtCore.QRect(10, 110, 461, 33))
        self.IPAddress.setObjectName("IPAddress")
        self.ipstatusONLINE = CaptionLabel(Form)
        self.ipstatusONLINE.setGeometry(QtCore.QRect(10, 150, 70, 15))
        self.ipstatusONLINE.setStyleSheet("FluentLabelBase {\n"
"    color: black;\n"
"}\n"
"\n"
"HyperlinkLabel {\n"
"    color: #009faa;\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    text-align: left;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"}\n"
"\n"
"HyperlinkLabel[underline=true] {\n"
"    text-decoration: underline;\n"
"}\n"
"\n"
"HyperlinkLabel[underline=false] {\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"HyperlinkLabel:hover {\n"
"    color: #007780;\n"
"}\n"
"\n"
"HyperlinkLabel:pressed {\n"
"    color: #00a7b3;\n"
"}\n"
"FluentLabelBase{color:green}")
        self.ipstatusONLINE.setObjectName("ipstatusONLINE")
        self.ipstatusOFFLINE = CaptionLabel(Form)
        self.ipstatusOFFLINE.setGeometry(QtCore.QRect(10, 150, 70, 15))
        self.ipstatusOFFLINE.setStyleSheet("FluentLabelBase {\n"
"    color: black;\n"
"}\n"
"\n"
"HyperlinkLabel {\n"
"    color: #009faa;\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    text-align: left;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"}\n"
"\n"
"HyperlinkLabel[underline=true] {\n"
"    text-decoration: underline;\n"
"}\n"
"\n"
"HyperlinkLabel[underline=false] {\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"HyperlinkLabel:hover {\n"
"    color: #007780;\n"
"}\n"
"\n"
"HyperlinkLabel:pressed {\n"
"    color: #00a7b3;\n"
"}\n"
"FluentLabelBase{color:red}")
        self.ipstatusOFFLINE.setObjectName("ipstatusOFFLINE")
        self.MachineUsername = LineEdit(Form)
        self.MachineUsername.setGeometry(QtCore.QRect(10, 180, 441, 33))
        self.MachineUsername.setObjectName("MachineUsername")
        self.MachinePassword = PasswordLineEdit(Form)
        self.MachinePassword.setGeometry(QtCore.QRect(10, 230, 441, 33))
        self.MachinePassword.setObjectName("MachinePassword")
        self.VerifyMachineInfo = PushButton(Form)
        self.VerifyMachineInfo.setGeometry(QtCore.QRect(470, 230, 102, 32))
        self.VerifyMachineInfo.setObjectName("VerifyMachineInfo")
        self.SubtitleLabel_2 = SubtitleLabel(Form)
        self.SubtitleLabel_2.setGeometry(QtCore.QRect(10, 290, 221, 28))
        self.SubtitleLabel_2.setObjectName("SubtitleLabel_2")
        self.HorizontalSeparator = HorizontalSeparator(Form)
        self.HorizontalSeparator.setGeometry(QtCore.QRect(10, 280, 561, 3))
        self.HorizontalSeparator.setObjectName("HorizontalSeparator")
        self.SNMPv3USERNAME = LineEdit(Form)
        self.SNMPv3USERNAME.setGeometry(QtCore.QRect(10, 340, 561, 33))
        self.SNMPv3USERNAME.setObjectName("SNMPv3USERNAME")
        self.AUTHTYPELabel = BodyLabel(Form)
        self.AUTHTYPELabel.setGeometry(QtCore.QRect(10, 480, 131, 19))
        self.AUTHTYPELabel.setObjectName("AUTHTYPELabel")
        self.SNMPv3PASSWORD = PasswordLineEdit(Form)
        self.SNMPv3PASSWORD.setGeometry(QtCore.QRect(10, 390, 561, 33))
        self.SNMPv3PASSWORD.setObjectName("SNMPv3PASSWORD")
        self.MD5CheckBox = CheckBox(Form)
        self.MD5CheckBox.setGeometry(QtCore.QRect(160, 480, 92, 22))
        self.MD5CheckBox.setObjectName("MD5CheckBox")
        self.SHACheckBox = CheckBox(Form)
        self.SHACheckBox.setGeometry(QtCore.QRect(240, 480, 92, 22))
        self.SHACheckBox.setObjectName("SHACheckBox")
        self.PRIVTYPELABEL = BodyLabel(Form)
        self.PRIVTYPELABEL.setGeometry(QtCore.QRect(10, 520, 111, 19))
        self.PRIVTYPELABEL.setObjectName("PRIVTYPELABEL")
        self.DESCheckBoX = CheckBox(Form)
        self.DESCheckBoX.setGeometry(QtCore.QRect(130, 520, 92, 22))
        self.DESCheckBoX.setObjectName("DESCheckBoX")
        self.AESCheckBox = CheckBox(Form)
        self.AESCheckBox.setGeometry(QtCore.QRect(210, 520, 92, 22))
        self.AESCheckBox.setObjectName("AESCheckBox")
        self.SNMPTIMEOUT = LineEdit(Form)
        self.SNMPTIMEOUT.setGeometry(QtCore.QRect(10, 620, 561, 33))
        self.SNMPTIMEOUT.setObjectName("SNMPTIMEOUT")
        self.ADD_BUTTON = PrimaryPushButton(Form)
        self.ADD_BUTTON.setGeometry(QtCore.QRect(420, 690, 153, 32))
        self.ADD_BUTTON.setObjectName("ADD_BUTTON")
        self.Port = LineEdit(Form)
        self.Port.setGeometry(QtCore.QRect(490, 110, 81, 33))
        self.Port.setText("")
        self.Port.setObjectName("Port")
        self.ReadOnly = CheckBox(Form)
        self.ReadOnly.setGeometry(QtCore.QRect(90, 440, 101, 22))
        self.ReadOnly.setObjectName("ReadOnly")
        self.ReadWrite = CheckBox(Form)
        self.ReadWrite.setGeometry(QtCore.QRect(200, 440, 121, 22))
        self.ReadWrite.setObjectName("ReadWrite")
        self.UserTypeLabel = BodyLabel(Form)
        self.UserTypeLabel.setGeometry(QtCore.QRect(10, 440, 71, 19))
        self.UserTypeLabel.setObjectName("UserTypeLabel")
        self.EncryptionKey = PasswordLineEdit(Form)
        self.EncryptionKey.setGeometry(QtCore.QRect(10, 570, 561, 33))
        self.EncryptionKey.setObjectName("EncryptionKey")
        self.authTypeButtonGroup = QButtonGroup(Form)
        self.authTypeButtonGroup.addButton(self.MD5CheckBox)
        self.authTypeButtonGroup.addButton(self.SHACheckBox)
        
        self.privTypeButtonGroup = QButtonGroup(Form)
        self.privTypeButtonGroup.addButton(self.DESCheckBoX)
        self.privTypeButtonGroup.addButton(self.AESCheckBox)
        
        self.UserTypeButtonGroup = QButtonGroup(Form)
        self.UserTypeButtonGroup.addButton(self.ReadOnly)
        self.UserTypeButtonGroup.addButton(self.ReadWrite)
        

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.SubtitleLabel.setText(_translate("Form", "Machine info:"))
        self.MachineName.setPlaceholderText(_translate("Form", "Machine name"))
        self.IPAddress.setPlaceholderText(_translate("Form", "IP Address"))
        self.ipstatusONLINE.setText(_translate("Form", "IP Online !"))
        self.ipstatusOFFLINE.setText(_translate("Form", "IP Offine !"))
        self.MachineUsername.setPlaceholderText(_translate("Form", "Username"))
        self.MachinePassword.setPlaceholderText(_translate("Form", "Password"))
        self.VerifyMachineInfo.setText(_translate("Form", "Verify info"))
        self.SubtitleLabel_2.setText(_translate("Form", "SNMPv3 configuration:"))
        self.SNMPv3USERNAME.setPlaceholderText(_translate("Form", "SNMPv3 Username"))
        self.AUTHTYPELabel.setText(_translate("Form", "Authentication Type:"))
        self.SNMPv3PASSWORD.setPlaceholderText(_translate("Form", "Password"))
        self.MD5CheckBox.setText(_translate("Form", "MD5"))
        self.SHACheckBox.setText(_translate("Form", "SHA512"))
        self.PRIVTYPELABEL.setText(_translate("Form", "Encryption Type:"))
        self.DESCheckBoX.setText(_translate("Form", "DES"))
        self.AESCheckBox.setText(_translate("Form", "AES256"))
        self.SNMPTIMEOUT.setPlaceholderText(_translate("Form", "SNMP Timeout (Default 5 Sec)"))
        self.ADD_BUTTON.setText(_translate("Form", "Add"))
        self.Port.setPlaceholderText(_translate("Form", "Port"))
        self.ReadOnly.setText(_translate("Form", "Read Only"))
        self.ReadWrite.setText(_translate("Form", "Read-Write"))
        self.UserTypeLabel.setText(_translate("Form", "User Type:"))
        self.EncryptionKey.setPlaceholderText(_translate("Form", "Encryption Key"))
from qfluentwidgets import BodyLabel, CaptionLabel, CheckBox, HorizontalSeparator, LineEdit, PasswordLineEdit, PrimaryPushButton, PushButton, SubtitleLabel
