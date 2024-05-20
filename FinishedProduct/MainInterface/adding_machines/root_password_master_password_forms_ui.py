# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'root_password_master_password_forms.ui'
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
    ProgressBar, PushButton, StrongBodyLabel)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(413, 315)
        self.RootPassword_config = PasswordLineEdit(Form)
        self.RootPassword_config.setObjectName(u"RootPassword_config")
        self.RootPassword_config.setGeometry(QRect(10, 140, 391, 33))
        self.StartTheConf_config = PrimaryPushButton(Form)
        self.StartTheConf_config.setObjectName(u"StartTheConf_config")
        self.StartTheConf_config.setGeometry(QRect(250, 230, 153, 32))
        self.CancelTheConf_config = PushButton(Form)
        self.CancelTheConf_config.setObjectName(u"CancelTheConf_config")
        self.CancelTheConf_config.setGeometry(QRect(130, 230, 102, 32))
        self.StrongBodyLabel = StrongBodyLabel(Form)
        self.StrongBodyLabel.setObjectName(u"StrongBodyLabel")
        self.StrongBodyLabel.setGeometry(QRect(10, 10, 281, 19))
        self.BodyLabel = BodyLabel(Form)
        self.BodyLabel.setObjectName(u"BodyLabel")
        self.BodyLabel.setGeometry(QRect(10, 30, 971, 21))
        self.BodyLabel_2 = BodyLabel(Form)
        self.BodyLabel_2.setObjectName(u"BodyLabel_2")
        self.BodyLabel_2.setGeometry(QRect(10, 50, 691, 19))
        self.BodyLabel_3 = BodyLabel(Form)
        self.BodyLabel_3.setObjectName(u"BodyLabel_3")
        self.BodyLabel_3.setGeometry(QRect(10, 70, 191, 19))
        self.RootUser_config = LineEdit(Form)
        self.RootUser_config.setObjectName(u"RootUser_config")
        self.RootUser_config.setGeometry(QRect(10, 100, 391, 33))
        self.MasterPassword_config = PasswordLineEdit(Form)
        self.MasterPassword_config.setObjectName(u"MasterPassword_config")
        self.MasterPassword_config.setGeometry(QRect(10, 180, 391, 33))
        self.ProgressBar = ProgressBar(Form)
        self.ProgressBar.setObjectName(u"ProgressBar")
        self.ProgressBar.setGeometry(QRect(10, 290, 391, 4))
        self.StrongBodyLabel_2 = StrongBodyLabel(Form)
        self.StrongBodyLabel_2.setObjectName(u"StrongBodyLabel_2")
        self.StrongBodyLabel_2.setGeometry(QRect(10, 270, 111, 19))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.RootPassword_config.setPlaceholderText(QCoreApplication.translate("Form", u"Password", None))
        self.StartTheConf_config.setText(QCoreApplication.translate("Form", u"Start ", None))
        self.CancelTheConf_config.setText(QCoreApplication.translate("Form", u"Cancel", None))
        self.StrongBodyLabel.setText(QCoreApplication.translate("Form", u"Enter the machine's root user and password", None))
        self.BodyLabel.setText(QCoreApplication.translate("Form", u"Please be aware that the password you're entering in this form ", None))
        self.BodyLabel_2.setText(QCoreApplication.translate("Form", u"will be utilized solely for configuring the machine and will not be ", None))
        self.BodyLabel_3.setText(QCoreApplication.translate("Form", u"stored anywhere afterward.", None))
        self.RootUser_config.setPlaceholderText(QCoreApplication.translate("Form", u"Root user", None))
        self.MasterPassword_config.setPlaceholderText(QCoreApplication.translate("Form", u"Master Password", None))
        self.StrongBodyLabel_2.setText(QCoreApplication.translate("Form", u"Progress:", None))
    # retranslateUi

