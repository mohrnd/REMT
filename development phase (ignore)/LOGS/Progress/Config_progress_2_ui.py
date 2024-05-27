# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Config_progress_2.ui'
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
    StateToolTip, TextEdit)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(474, 459)
        self.configprogress_TextEdit = TextEdit(Form)
        self.configprogress_TextEdit.setObjectName(u"configprogress_TextEdit")
        self.configprogress_TextEdit.setGeometry(QRect(10, 10, 451, 331))
        self.StartButton = PrimaryPushButton(Form)
        self.StartButton.setObjectName(u"StartButton")
        self.StartButton.setGeometry(QRect(310, 400, 151, 51))
        self.Progress_wheel = StateToolTip(Form)
        self.Progress_wheel.setObjectName(u"Progress_wheel")
        self.Progress_wheel.setEnabled(True)
        self.Progress_wheel.setGeometry(QRect(10, 400, 256, 51))
        self.Masterpassword_input = PasswordLineEdit(Form)
        self.Masterpassword_input.setObjectName(u"Masterpassword_input")
        self.Masterpassword_input.setGeometry(QRect(10, 350, 451, 33))
        self.ExitButton = PrimaryPushButton(Form)
        self.ExitButton.setObjectName(u"ExitButton")
        self.ExitButton.setGeometry(QRect(310, 400, 151, 51))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.StartButton.setText(QCoreApplication.translate("Form", u"Start Fetching Logs", None))
        self.Masterpassword_input.setPlaceholderText(QCoreApplication.translate("Form", u"Master password", None))
        self.ExitButton.setText(QCoreApplication.translate("Form", u"Exit", None))
    # retranslateUi

