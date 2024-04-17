# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Config_progress.ui'
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

from qfluentwidgets import (PrimaryPushButton, PushButton, StateToolTip, TextEdit)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(474, 459)
        self.configprogress_TextEdit = TextEdit(Form)
        self.configprogress_TextEdit.setObjectName(u"configprogress_TextEdit")
        self.configprogress_TextEdit.setGeometry(QRect(10, 10, 451, 381))
        self.configprogress_finish = PrimaryPushButton(Form)
        self.configprogress_finish.setObjectName(u"configprogress_finish")
        self.configprogress_finish.setGeometry(QRect(330, 400, 131, 51))
        self.StateToolTip = StateToolTip(Form)
        self.StateToolTip.setObjectName(u"StateToolTip")
        self.StateToolTip.setEnabled(True)
        self.StateToolTip.setGeometry(QRect(10, 400, 256, 51))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.configprogress_finish.setText(QCoreApplication.translate("Form", u"Finish", None))
    # retranslateUi

