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
        __qtreewidgetitem = QTreeWidgetItem(self.TreeWidget)
        QTreeWidgetItem(__qtreewidgetitem)
        self.TreeWidget.setObjectName(u"TreeWidget")
        self.TreeWidget.setGeometry(QRect(20, 80, 751, 461))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        ___qtreewidgetitem = self.TreeWidget.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("Form", u"2", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Form", u"1", None));

        __sortingEnabled = self.TreeWidget.isSortingEnabled()
        self.TreeWidget.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.TreeWidget.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("Form", u"item2", None));
        ___qtreewidgetitem2 = ___qtreewidgetitem1.child(0)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("Form", u"item1", None));
        self.TreeWidget.setSortingEnabled(__sortingEnabled)

    # retranslateUi

