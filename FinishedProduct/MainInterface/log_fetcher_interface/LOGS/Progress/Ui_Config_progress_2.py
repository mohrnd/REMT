# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\dell-5320\Desktop\REMT\Tests\LOGS\Progress\Config_progress_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(474, 459)
        self.configprogress_TextEdit = TextEdit(Form)
        self.configprogress_TextEdit.setGeometry(QtCore.QRect(10, 10, 451, 331))
        self.configprogress_TextEdit.setObjectName("configprogress_TextEdit")
        self.StartButton = PrimaryPushButton(Form)
        self.StartButton.setGeometry(QtCore.QRect(310, 400, 151, 51))
        self.StartButton.setObjectName("StartButton")
        self.Progress_wheel = StateToolTip(title='Please Wait', content='fetching logs', parent=Form)
        self.Progress_wheel.setEnabled(True)
        self.Progress_wheel.setGeometry(QtCore.QRect(10, 400, 256, 51))
        self.Progress_wheel.setObjectName("Progress_wheel")
        self.Masterpassword_input = PasswordLineEdit(Form)
        self.Masterpassword_input.setGeometry(QtCore.QRect(10, 350, 451, 33))
        self.Masterpassword_input.setObjectName("Masterpassword_input")
        self.ExitButton = PrimaryPushButton(Form)
        self.ExitButton.setGeometry(QtCore.QRect(310, 400, 151, 51))
        self.ExitButton.setObjectName("ExitButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.StartButton.setText(_translate("Form", "Start Fetching Logs"))
        self.Masterpassword_input.setPlaceholderText(_translate("Form", "Master password"))
        self.ExitButton.setText(_translate("Form", "Exit"))
from qfluentwidgets import PasswordLineEdit, PrimaryPushButton, StateToolTip, TextEdit
