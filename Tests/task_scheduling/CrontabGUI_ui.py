# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CrontabGUI.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLayout, QSizePolicy, QTableWidgetItem, QWidget)

from qfluentwidgets import (LineEdit, PrimaryPushButton, PushButton, StrongBodyLabel,
    TableWidget, TextEdit)

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.setEnabled(True)
        Frame.resize(813, 768)
        Frame.setMaximumSize(QSize(1000, 1000))
        self.frame = QFrame(Frame)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 270, 811, 491))
        self.frame.setStyleSheet(u"#Frame{border:\"5px solid black\"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayoutWidget = QWidget(self.frame)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 50, 791, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.minute_input = LineEdit(self.horizontalLayoutWidget)
        self.minute_input.setObjectName(u"minute_input")

        self.horizontalLayout.addWidget(self.minute_input)

        self.hour_input = LineEdit(self.horizontalLayoutWidget)
        self.hour_input.setObjectName(u"hour_input")

        self.horizontalLayout.addWidget(self.hour_input)

        self.day_input = LineEdit(self.horizontalLayoutWidget)
        self.day_input.setObjectName(u"day_input")

        self.horizontalLayout.addWidget(self.day_input)

        self.month_input = LineEdit(self.horizontalLayoutWidget)
        self.month_input.setObjectName(u"month_input")

        self.horizontalLayout.addWidget(self.month_input)

        self.LineEdit = LineEdit(self.horizontalLayoutWidget)
        self.LineEdit.setObjectName(u"LineEdit")

        self.horizontalLayout.addWidget(self.LineEdit)

        self.add_button = PrimaryPushButton(self.horizontalLayoutWidget)
        self.add_button.setObjectName(u"add_button")

        self.horizontalLayout.addWidget(self.add_button)

        self.horizontalLayoutWidget_3 = QWidget(self.frame)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(7, 0, 791, 41))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Onstartup = PushButton(self.horizontalLayoutWidget_3)
        self.Onstartup.setObjectName(u"Onstartup")

        self.horizontalLayout_3.addWidget(self.Onstartup)

        self.hourly = PushButton(self.horizontalLayoutWidget_3)
        self.hourly.setObjectName(u"hourly")

        self.horizontalLayout_3.addWidget(self.hourly)

        self.Daily_2 = PushButton(self.horizontalLayoutWidget_3)
        self.Daily_2.setObjectName(u"Daily_2")
        self.Daily_2.setEnabled(True)

        self.horizontalLayout_3.addWidget(self.Daily_2)

        self.weekly_2 = PushButton(self.horizontalLayoutWidget_3)
        self.weekly_2.setObjectName(u"weekly_2")

        self.horizontalLayout_3.addWidget(self.weekly_2)

        self.monthly_2 = PushButton(self.horizontalLayoutWidget_3)
        self.monthly_2.setObjectName(u"monthly_2")

        self.horizontalLayout_3.addWidget(self.monthly_2)

        self.PushButton_5 = PushButton(self.horizontalLayoutWidget_3)
        self.PushButton_5.setObjectName(u"PushButton_5")

        self.horizontalLayout_3.addWidget(self.PushButton_5)

        self.Command_input = LineEdit(self.frame)
        self.Command_input.setObjectName(u"Command_input")
        self.Command_input.setGeometry(QRect(10, 340, 791, 33))
        self.Apply = PrimaryPushButton(self.frame)
        self.Apply.setObjectName(u"Apply")
        self.Apply.setGeometry(QRect(720, 440, 81, 32))
        self.StrongBodyLabel = StrongBodyLabel(self.frame)
        self.StrongBodyLabel.setObjectName(u"StrongBodyLabel")
        self.StrongBodyLabel.setGeometry(QRect(10, 100, 121, 21))
        self.Machines = TableWidget(self.frame)
        if (self.Machines.columnCount() < 3):
            self.Machines.setColumnCount(3)
        font = QFont()
        font.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.Machines.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.Machines.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.Machines.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.Machines.setObjectName(u"Machines")
        self.Machines.setGeometry(QRect(10, 120, 791, 211))
        self.Preview = TextEdit(self.frame)
        self.Preview.setObjectName(u"Preview")
        self.Preview.setGeometry(QRect(10, 380, 701, 91))
        self.Preview.setReadOnly(True)
        self.Active_jobs = QFrame(Frame)
        self.Active_jobs.setObjectName(u"Active_jobs")
        self.Active_jobs.setGeometry(QRect(0, 0, 811, 271))
        self.Active_jobs.setFrameShape(QFrame.StyledPanel)
        self.Active_jobs.setFrameShadow(QFrame.Raised)
        self.TableWidget = TableWidget(self.Active_jobs)
        if (self.TableWidget.columnCount() < 5):
            self.TableWidget.setColumnCount(5)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.TableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.TableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.TableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.TableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.TableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem7)
        self.TableWidget.setObjectName(u"TableWidget")
        self.TableWidget.setGeometry(QRect(0, 40, 811, 231))

        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Crontab GUI", None))
        self.minute_input.setText("")
        self.minute_input.setPlaceholderText(QCoreApplication.translate("Frame", u"Minute", None))
        self.hour_input.setText("")
        self.hour_input.setPlaceholderText(QCoreApplication.translate("Frame", u"Hour", None))
        self.day_input.setText("")
        self.day_input.setPlaceholderText(QCoreApplication.translate("Frame", u"Day", None))
        self.month_input.setText("")
        self.month_input.setPlaceholderText(QCoreApplication.translate("Frame", u"Month", None))
        self.LineEdit.setText("")
        self.LineEdit.setPlaceholderText(QCoreApplication.translate("Frame", u"Week", None))
        self.add_button.setText(QCoreApplication.translate("Frame", u"Add", None))
        self.Onstartup.setText(QCoreApplication.translate("Frame", u"On Startup", None))
        self.hourly.setText(QCoreApplication.translate("Frame", u"Hourly", None))
        self.Daily_2.setText(QCoreApplication.translate("Frame", u"Daily", None))
        self.weekly_2.setText(QCoreApplication.translate("Frame", u"Weekly", None))
        self.monthly_2.setText(QCoreApplication.translate("Frame", u"Monthly", None))
        self.PushButton_5.setText(QCoreApplication.translate("Frame", u"Yearly", None))
        self.Command_input.setPlaceholderText(QCoreApplication.translate("Frame", u"Command/Path to script", None))
        self.Apply.setText(QCoreApplication.translate("Frame", u"Apply", None))
        self.StrongBodyLabel.setText(QCoreApplication.translate("Frame", u"Select a machine:", None))
        ___qtablewidgetitem = self.Machines.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Frame", u"Machine IP address", None));
        ___qtablewidgetitem1 = self.Machines.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Frame", u"Machine Name", None));
        ___qtablewidgetitem2 = self.Machines.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Frame", u"Select", None));
        self.Preview.setPlaceholderText(QCoreApplication.translate("Frame", u"Preview", None))
        ___qtablewidgetitem3 = self.TableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Frame", u"Machine IP address", None));
        ___qtablewidgetitem4 = self.TableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Frame", u"Job", None));
        ___qtablewidgetitem5 = self.TableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Frame", u"Next execution", None));
        ___qtablewidgetitem6 = self.TableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Frame", u"Interpretation", None));
        ___qtablewidgetitem7 = self.TableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Frame", u"Delete", None));
    # retranslateUi

