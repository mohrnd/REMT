# coding:utf-8
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QStackedWidget, QVBoxLayout, QLabel, QSizePolicy

from qfluentwidgets import Pivot, setTheme, Theme, SegmentedWidget, FluentIcon
from PyQt5.QtGui import *
from qfluentwidgets import *

class MainWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.setStyleSheet("""
            MainWidget{background: white}
            QLabel{
                font: 20px 'Segoe UI';
                background: rgb(242,242,242);
                border-radius: 8px;
            }
        """)
        self.resize(400, 400)

        self.pivot = SegmentedWidget(self)
        self.stackedWidget = QStackedWidget(self)
        self.vBoxLayout = QVBoxLayout(self)

        self.Upload = QLabel('Upload Interface', self)
        self.Download = QLabel('Download Interface', self)


        # add items to pivot
        self.addSubInterface(self.Upload, 'Upload', 'Upload')
        self.addSubInterface(self.Download, 'Download', 'Download')


        self.vBoxLayout.addWidget(self.pivot)
        self.vBoxLayout.addWidget(self.stackedWidget)
        self.vBoxLayout.setContentsMargins(30, 10, 30, 30)

        self.stackedWidget.currentChanged.connect(self.onCurrentIndexChanged)
        self.stackedWidget.setCurrentWidget(self.Upload)
        self.pivot.setCurrentItem(self.Upload.objectName())

    def addSubInterface(self, widget: QLabel, objectName, text):
        widget.setObjectName(objectName)
        widget.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(widget)
        self.pivot.addItem(
            routeKey=objectName,
            text=text,
            onClick=lambda: self.stackedWidget.setCurrentWidget(widget),
        )

    def onCurrentIndexChanged(self, index):
        widget = self.stackedWidget.widget(index)
        self.pivot.setCurrentItem(widget.objectName())


if __name__ == '__main__':
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    color = QColor('#351392')
    setThemeColor(color ,Qt.GlobalColor , '') 
    
    app = QApplication(sys.argv)
    w = MainWidget()
    w.show()
    app.exec_()