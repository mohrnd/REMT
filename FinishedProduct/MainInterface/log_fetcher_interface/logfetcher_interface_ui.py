# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'logfetcher_interface.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QSizePolicy, QTreeWidgetItem,
    QWidget)

from qfluentwidgets import TreeWidget

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(813, 768)
        self.TreeWidget = TreeWidget(Form)
        self.TreeWidget.setObjectName(u"TreeWidget")
        self.TreeWidget.setGeometry(QRect(20, 60, 771, 651))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        ___qtreewidgetitem = self.TreeWidget.headerItem()
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("Form", u"Actions", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("Form", u"Latest fetch", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("Form", u"Status", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("Form", u"IP", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Form", u"Machine name", None));
    # retranslateUi

