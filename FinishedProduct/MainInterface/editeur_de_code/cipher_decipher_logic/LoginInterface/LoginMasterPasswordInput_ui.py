# Form implementation generated from reading ui file 'c:\Users\dell-5320\Desktop\REMT\FinishedProduct\MainInterface\editeur_de_code\cipher_decipher_logic\LoginInterface\LoginMasterPasswordInput.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(404, 139)
        self.MasterPassword_login = PasswordLineEdit(parent=Form)
        self.MasterPassword_login.setGeometry(QtCore.QRect(10, 50, 381, 33))
        self.MasterPassword_login.setObjectName("MasterPassword_login")
        self.MasterPWDContinue_login = PrimaryPushButton(parent=Form)
        self.MasterPWDContinue_login.setGeometry(QtCore.QRect(240, 90, 153, 32))
        self.MasterPWDContinue_login.setObjectName("MasterPWDContinue_login")
        self.CloseMasterPWDWindow_login = PushButton(parent=Form)
        self.CloseMasterPWDWindow_login.setGeometry(QtCore.QRect(120, 90, 102, 32))
        self.CloseMasterPWDWindow_login.setObjectName("CloseMasterPWDWindow_login")
        self.StrongBodyLabel = StrongBodyLabel(parent=Form)
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