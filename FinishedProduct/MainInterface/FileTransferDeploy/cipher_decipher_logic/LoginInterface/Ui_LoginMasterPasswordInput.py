# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\BALLS2 (rip BALLS)\Desktop\REMT\FinishedProduct\MasterPasswordInput\LoginInterface\LoginMasterPasswordInput.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(404, 139)
        self.MasterPassword_login = PasswordLineEdit(Form)
        self.MasterPassword_login.setGeometry(QtCore.QRect(10, 50, 381, 33))
        self.MasterPassword_login.setObjectName("MasterPassword_login")
        self.MasterPWDContinue_login = PrimaryPushButton(Form)
        self.MasterPWDContinue_login.setGeometry(QtCore.QRect(240, 90, 153, 32))
        self.MasterPWDContinue_login.setObjectName("MasterPWDContinue_login")
        self.CloseMasterPWDWindow_login = PushButton(Form)
        self.CloseMasterPWDWindow_login.setGeometry(QtCore.QRect(120, 90, 102, 32))
        self.CloseMasterPWDWindow_login.setObjectName("CloseMasterPWDWindow_login")
        self.StrongBodyLabel = StrongBodyLabel(Form)
        self.StrongBodyLabel.setGeometry(QtCore.QRect(10, 10, 261, 19))
        self.StrongBodyLabel.setObjectName("StrongBodyLabel")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.MasterPassword_login.setPlaceholderText(_translate("Form", "Master Password"))
        self.MasterPWDContinue_login.setText(_translate("Form", "Continue"))
        self.CloseMasterPWDWindow_login.setText(_translate("Form", "Cancel"))
        self.StrongBodyLabel.setText(_translate("Form", "Enter your master Password to continue"))
from qfluentwidgets import PasswordLineEdit, PrimaryPushButton, PushButton, StrongBodyLabel
