# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Add_machine.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QSizePolicy, QWidget)

from qfluentwidgets import (BodyLabel, CaptionLabel, CheckBox, HorizontalSeparator,
    LineEdit, PasswordLineEdit, PrimaryPushButton, PushButton,
    SubtitleLabel)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(581, 768)
        self.SubtitleLabel = SubtitleLabel(Form)
        self.SubtitleLabel.setObjectName(u"SubtitleLabel")
        self.SubtitleLabel.setGeometry(QRect(10, 20, 141, 21))
        self.MachineName = LineEdit(Form)
        self.MachineName.setObjectName(u"MachineName")
        self.MachineName.setGeometry(QRect(10, 60, 561, 33))
        self.IPAddress = LineEdit(Form)
        self.IPAddress.setObjectName(u"IPAddress")
        self.IPAddress.setGeometry(QRect(10, 110, 461, 33))
        self.ipstatusONLINE = CaptionLabel(Form)
        self.ipstatusONLINE.setObjectName(u"ipstatusONLINE")
        self.ipstatusONLINE.setGeometry(QRect(10, 150, 70, 15))
        self.ipstatusONLINE.setStyleSheet(u"FluentLabelBase {\n"
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
        self.ipstatusOFFLINE = CaptionLabel(Form)
        self.ipstatusOFFLINE.setObjectName(u"ipstatusOFFLINE")
        self.ipstatusOFFLINE.setGeometry(QRect(10, 150, 70, 15))
        self.ipstatusOFFLINE.setStyleSheet(u"FluentLabelBase {\n"
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
        self.MachineUsername = LineEdit(Form)
        self.MachineUsername.setObjectName(u"MachineUsername")
        self.MachineUsername.setGeometry(QRect(10, 180, 441, 33))
        self.MachinePassword = PasswordLineEdit(Form)
        self.MachinePassword.setObjectName(u"MachinePassword")
        self.MachinePassword.setGeometry(QRect(10, 230, 441, 33))
        self.VerifyMachineInfo = PushButton(Form)
        self.VerifyMachineInfo.setObjectName(u"VerifyMachineInfo")
        self.VerifyMachineInfo.setGeometry(QRect(470, 230, 102, 32))
        self.SubtitleLabel_2 = SubtitleLabel(Form)
        self.SubtitleLabel_2.setObjectName(u"SubtitleLabel_2")
        self.SubtitleLabel_2.setGeometry(QRect(10, 290, 221, 28))
        self.HorizontalSeparator = HorizontalSeparator(Form)
        self.HorizontalSeparator.setObjectName(u"HorizontalSeparator")
        self.HorizontalSeparator.setGeometry(QRect(10, 280, 561, 3))
        self.SNMPv3USERNAME = LineEdit(Form)
        self.SNMPv3USERNAME.setObjectName(u"SNMPv3USERNAME")
        self.SNMPv3USERNAME.setGeometry(QRect(10, 340, 561, 33))
        self.AUTHTYPELabel = BodyLabel(Form)
        self.AUTHTYPELabel.setObjectName(u"AUTHTYPELabel")
        self.AUTHTYPELabel.setGeometry(QRect(10, 480, 131, 19))
        self.SNMPv3PASSWORD = PasswordLineEdit(Form)
        self.SNMPv3PASSWORD.setObjectName(u"SNMPv3PASSWORD")
        self.SNMPv3PASSWORD.setGeometry(QRect(10, 390, 561, 33))
        self.MD5CheckBox = CheckBox(Form)
        self.MD5CheckBox.setObjectName(u"MD5CheckBox")
        self.MD5CheckBox.setGeometry(QRect(160, 480, 92, 22))
        self.SHACheckBox = CheckBox(Form)
        self.SHACheckBox.setObjectName(u"SHACheckBox")
        self.SHACheckBox.setGeometry(QRect(240, 480, 92, 22))
        self.PRIVTYPELABEL = BodyLabel(Form)
        self.PRIVTYPELABEL.setObjectName(u"PRIVTYPELABEL")
        self.PRIVTYPELABEL.setGeometry(QRect(10, 520, 111, 19))
        self.DESCheckBoX = CheckBox(Form)
        self.DESCheckBoX.setObjectName(u"DESCheckBoX")
        self.DESCheckBoX.setGeometry(QRect(130, 520, 92, 22))
        self.AESCheckBox = CheckBox(Form)
        self.AESCheckBox.setObjectName(u"AESCheckBox")
        self.AESCheckBox.setGeometry(QRect(210, 520, 92, 22))
        self.SNMPTIMEOUT = LineEdit(Form)
        self.SNMPTIMEOUT.setObjectName(u"SNMPTIMEOUT")
        self.SNMPTIMEOUT.setGeometry(QRect(10, 620, 561, 33))
        self.ADD_BUTTON = PrimaryPushButton(Form)
        self.ADD_BUTTON.setObjectName(u"ADD_BUTTON")
        self.ADD_BUTTON.setGeometry(QRect(420, 690, 153, 32))
        self.Port = LineEdit(Form)
        self.Port.setObjectName(u"Port")
        self.Port.setGeometry(QRect(490, 110, 81, 33))
        self.ReadOnly = CheckBox(Form)
        self.ReadOnly.setObjectName(u"ReadOnly")
        self.ReadOnly.setGeometry(QRect(90, 440, 101, 22))
        self.ReadWrite = CheckBox(Form)
        self.ReadWrite.setObjectName(u"ReadWrite")
        self.ReadWrite.setGeometry(QRect(200, 440, 121, 22))
        self.UserTypeLabel = BodyLabel(Form)
        self.UserTypeLabel.setObjectName(u"UserTypeLabel")
        self.UserTypeLabel.setGeometry(QRect(10, 440, 71, 19))
        self.EncryptionKey = PasswordLineEdit(Form)
        self.EncryptionKey.setObjectName(u"EncryptionKey")
        self.EncryptionKey.setGeometry(QRect(10, 570, 561, 33))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.SubtitleLabel.setText(QCoreApplication.translate("Form", u"Machine info:", None))
        self.MachineName.setPlaceholderText(QCoreApplication.translate("Form", u"Machine name", None))
        self.IPAddress.setPlaceholderText(QCoreApplication.translate("Form", u"IP Address", None))
        self.ipstatusONLINE.setText(QCoreApplication.translate("Form", u"IP Online !", None))
        self.ipstatusOFFLINE.setText(QCoreApplication.translate("Form", u"IP Offine !", None))
        self.MachineUsername.setPlaceholderText(QCoreApplication.translate("Form", u"Username", None))
        self.MachinePassword.setPlaceholderText(QCoreApplication.translate("Form", u"Password", None))
        self.VerifyMachineInfo.setText(QCoreApplication.translate("Form", u"Verify info", None))
        self.SubtitleLabel_2.setText(QCoreApplication.translate("Form", u"SNMPv3 configuration:", None))
        self.SNMPv3USERNAME.setPlaceholderText(QCoreApplication.translate("Form", u"SNMPv3 Username", None))
        self.AUTHTYPELabel.setText(QCoreApplication.translate("Form", u"Authentication Type:", None))
        self.SNMPv3PASSWORD.setPlaceholderText(QCoreApplication.translate("Form", u"Password", None))
        self.MD5CheckBox.setText(QCoreApplication.translate("Form", u"MD5", None))
        self.SHACheckBox.setText(QCoreApplication.translate("Form", u"SHA512", None))
        self.PRIVTYPELABEL.setText(QCoreApplication.translate("Form", u"Encryption Type:", None))
        self.DESCheckBoX.setText(QCoreApplication.translate("Form", u"DES", None))
        self.AESCheckBox.setText(QCoreApplication.translate("Form", u"AES256", None))
        self.SNMPTIMEOUT.setPlaceholderText(QCoreApplication.translate("Form", u"SNMP Timeout (Default 5 Sec)", None))
        self.ADD_BUTTON.setText(QCoreApplication.translate("Form", u"Add", None))
        self.Port.setText("")
        self.Port.setPlaceholderText(QCoreApplication.translate("Form", u"Port", None))
        self.ReadOnly.setText(QCoreApplication.translate("Form", u"Read Only", None))
        self.ReadWrite.setText(QCoreApplication.translate("Form", u"Read-Write", None))
        self.UserTypeLabel.setText(QCoreApplication.translate("Form", u"User Type:", None))
        self.EncryptionKey.setPlaceholderText(QCoreApplication.translate("Form", u"Encryption Key", None))
    # retranslateUi

