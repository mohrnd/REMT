# coding:utf-8
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QStackedWidget, QVBoxLayout, QLabel
from qfluentwidgets import SegmentedWidget
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWidgets import QApplication, QFrame, QHBoxLayout, QSizePolicy
from SSH_Widget import SSHWidget 


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

        self.addSubInterface1('PUT', 'PUT')
        self.addSubInterface2('GET', 'GET')

        self.vBoxLayout.addWidget(self.pivot)
        self.vBoxLayout.addWidget(self.stackedWidget)
        self.vBoxLayout.setContentsMargins(30, 10, 30, 30)

        self.stackedWidget.currentChanged.connect(self.onCurrentIndexChanged)

    def addSubInterface1(self, objectName, text):
        widget = PUT(text + ' interface', self)  # Instantiate Widget1 with different names
        widget.setObjectName(objectName)
        self.stackedWidget.addWidget(widget)
        self.pivot.addItem(
            routeKey=objectName,
            text=text,
            onClick=lambda: self.stackedWidget.setCurrentWidget(widget),
        )
    def addSubInterface2(self, objectName, text):
        widget = GET(text + ' interface', self)
        widget.setObjectName(objectName)
        self.stackedWidget.addWidget(widget)
        self.pivot.addItem(
            routeKey=objectName,
            text=text,
            onClick=lambda: self.stackedWidget.setCurrentWidget(widget),
        )
        
    def onCurrentIndexChanged(self, index):
        widget = self.stackedWidget.widget(index)
        self.pivot.setCurrentItem(widget.objectName())

class PUT(QFrame):
    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.ssh_widget = SSHWidget("192.168.69.38", "manager1", "Pa$$w0rd")  # Provide appropriate hostname, username, and password
        layout = QVBoxLayout(self)
        layout.addWidget(self.ssh_widget)  # Add SSHWidget to layout
        self.setObjectName(text.replace('-', '-'))

class GET(QFrame):
    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.ssh_widget = SSHWidget("192.168.69.38", "manager1", "Pa$$w0rd")  # Provide appropriate hostname, username, and password
        layout = QVBoxLayout(self)
        layout.addWidget(self.ssh_widget)  # Add SSHWidget to layout
        self.setObjectName(text.replace('-', '-'))

if __name__ == '__main__':
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    w = MainWidget()
    w.show()
    sys.exit(app.exec_())

