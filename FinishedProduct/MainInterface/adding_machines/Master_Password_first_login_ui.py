# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Master_Password_first_login.ui'
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

from qfluentwidgets import (BodyLabel, LineEdit, PasswordLineEdit, PrimaryPushButton,
    PushButton, StrongBodyLabel)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(404, 245)
        self.PasswordLineEdit = PasswordLineEdit(Form)
        self.PasswordLineEdit.setObjectName(u"PasswordLineEdit")
        self.PasswordLineEdit.setGeometry(QRect(10, 110, 381, 33))
        self.MasterPWDContinue = PrimaryPushButton(Form)
        self.MasterPWDContinue.setObjectName(u"MasterPWDContinue")
        self.MasterPWDContinue.setGeometry(QRect(240, 200, 153, 32))
        self.CloseMasterPWDWindow = PushButton(Form)
        self.CloseMasterPWDWindow.setObjectName(u"CloseMasterPWDWindow")
        self.CloseMasterPWDWindow.setGeometry(QRect(120, 200, 102, 32))
        self.StrongBodyLabel = StrongBodyLabel(Form)
        self.StrongBodyLabel.setObjectName(u"StrongBodyLabel")
        self.StrongBodyLabel.setGeometry(QRect(10, 10, 171, 19))
        self.PasswordLineEdit_2 = PasswordLineEdit(Form)
        self.PasswordLineEdit_2.setObjectName(u"PasswordLineEdit_2")
        self.PasswordLineEdit_2.setGeometry(QRect(10, 150, 381, 33))
        self.BodyLabel = BodyLabel(Form)
        self.BodyLabel.setObjectName(u"BodyLabel")
        self.BodyLabel.setGeometry(QRect(10, 40, 1061, 19))
        self.BodyLabel_2 = BodyLabel(Form)
        self.BodyLabel_2.setObjectName(u"BodyLabel_2")
        self.BodyLabel_2.setGeometry(QRect(10, 60, 671, 19))
        self.BodyLabel_3 = BodyLabel(Form)
        self.BodyLabel_3.setObjectName(u"BodyLabel_3")
        self.BodyLabel_3.setGeometry(QRect(10, 80, 161, 19))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.PasswordLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Master Password", None))
        self.MasterPWDContinue.setText(QCoreApplication.translate("Form", u"Save", None))
        self.CloseMasterPWDWindow.setText(QCoreApplication.translate("Form", u"Cancel", None))
        self.StrongBodyLabel.setText(QCoreApplication.translate("Form", u"Enter a master Password", None))
        self.PasswordLineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"Re-enter the Master Password", None))
        self.BodyLabel.setText(QCoreApplication.translate("Form", u"Please note that the password you're about to select will serve", None))
        self.BodyLabel_2.setText(QCoreApplication.translate("Form", u"as both your login credentials and the key for encrypting and ", None))
        self.BodyLabel_3.setText(QCoreApplication.translate("Form", u"decrypting passwords.", None))
    # retranslateUi

