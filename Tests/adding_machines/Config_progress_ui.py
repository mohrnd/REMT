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

from qfluentwidgets import (PrimaryPushButton, ProgressBar, PushButton, StrongBodyLabel,
    SubtitleLabel, TextEdit)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(474, 488)
        self.configprogress_TextEdit = TextEdit(Form)
        self.configprogress_TextEdit.setObjectName(u"configprogress_TextEdit")
        self.configprogress_TextEdit.setGeometry(QRect(10, 10, 451, 351))
        self.configprogress_ProgressBar = ProgressBar(Form)
        self.configprogress_ProgressBar.setObjectName(u"configprogress_ProgressBar")
        self.configprogress_ProgressBar.setGeometry(QRect(10, 410, 451, 4))
        self.configprogress_StrongBodyLabel = StrongBodyLabel(Form)
        self.configprogress_StrongBodyLabel.setObjectName(u"configprogress_StrongBodyLabel")
        self.configprogress_StrongBodyLabel.setGeometry(QRect(10, 380, 111, 19))
        self.configprogress_finish = PrimaryPushButton(Form)
        self.configprogress_finish.setObjectName(u"configprogress_finish")
        self.configprogress_finish.setGeometry(QRect(332, 440, 131, 32))
        self.machine_added = SubtitleLabel(Form)
        self.machine_added.setObjectName(u"machine_added")
        self.machine_added.setStyleSheet(u"FluentLabelBase {\n"
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
        self.failure = SubtitleLabel(Form)
        self.failure.setObjectName(u"failure")
        self.failure.setGeometry(QRect(10, 440, 261, 28))
        self.failure.setStyleSheet(u"FluentLabelBase {\n"
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
"FluentLabelBase{color:red\n"
"}")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.configprogress_StrongBodyLabel.setText(QCoreApplication.translate("Form", u"Progress:", None))
        self.configprogress_finish.setText(QCoreApplication.translate("Form", u"Finish", None))
        self.machine_added.setText(QCoreApplication.translate("Form", u"machine added successfully !", None))
        self.failure.setText(QCoreApplication.translate("Form", u"machine addition failed!", None))
    # retranslateUi

