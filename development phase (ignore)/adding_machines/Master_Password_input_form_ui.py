# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Master_Password_input_form.ui'
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

from qfluentwidgets import (LineEdit, PasswordLineEdit, PrimaryPushButton, PushButton,
    StrongBodyLabel)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(404, 139)
        self.MasterPassword_login = PasswordLineEdit(Form)
        self.MasterPassword_login.setObjectName(u"MasterPassword_login")
        self.MasterPassword_login.setGeometry(QRect(10, 50, 381, 33))
        self.MasterPWDContinue_login = PrimaryPushButton(Form)
        self.MasterPWDContinue_login.setObjectName(u"MasterPWDContinue_login")
        self.MasterPWDContinue_login.setGeometry(QRect(240, 90, 153, 32))
        self.CloseMasterPWDWindow_login = PushButton(Form)
        self.CloseMasterPWDWindow_login.setObjectName(u"CloseMasterPWDWindow_login")
        self.CloseMasterPWDWindow_login.setGeometry(QRect(120, 90, 102, 32))
        self.StrongBodyLabel = StrongBodyLabel(Form)
        self.StrongBodyLabel.setObjectName(u"StrongBodyLabel")
        self.StrongBodyLabel.setGeometry(QRect(10, 10, 261, 19))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.MasterPassword_login.setPlaceholderText(QCoreApplication.translate("Form", u"Master Password", None))
        self.MasterPWDContinue_login.setText(QCoreApplication.translate("Form", u"Continue", None))
        self.CloseMasterPWDWindow_login.setText(QCoreApplication.translate("Form", u"Cancel", None))
        self.StrongBodyLabel.setText(QCoreApplication.translate("Form", u"Enter your master Password to continue", None))
    # retranslateUi

