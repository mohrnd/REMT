# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Traps_Viewer_interface.ui'
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

from qfluentwidgets import (LineEdit, PrimaryPushButton, PushButton, SearchLineEdit,
    TextEdit)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(813, 768)
        self.All_Traps_received = TextEdit(Form)
        self.All_Traps_received.setObjectName(u"All_Traps_received")
        self.All_Traps_received.setGeometry(QRect(10, 50, 791, 711))
        self.All_Traps_received.setReadOnly(True)
        self.Filter = SearchLineEdit(Form)
        self.Filter.setObjectName(u"Filter")
        self.Filter.setGeometry(QRect(10, 10, 691, 33))
        self.Filter_Button = PrimaryPushButton(Form)
        self.Filter_Button.setObjectName(u"Filter_Button")
        self.Filter_Button.setGeometry(QRect(710, 10, 91, 32))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.Filter.setText("")
        self.Filter.setPlaceholderText("")
        self.Filter_Button.setText(QCoreApplication.translate("Form", u"Filter", None))
    # retranslateUi

