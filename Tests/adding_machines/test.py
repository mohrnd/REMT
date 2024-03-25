

import sys
from PyQt5.QtWidgets import QApplication, QTextEdit, QVBoxLayout, QPushButton, QDialog
from PyQt5.QtCore import QTimer

class SecondWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Second Window")
        layout = QVBoxLayout(self)
        self.edit = QTextEdit()
        layout.addWidget(self.edit)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.append_line)
        self.timer.start(1000)  # 3000 milliseconds = 3 seconds

    def append_line(self):
        self.edit.append('spam: spam spam spam spam')

class FirstWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First Window")
        layout = QVBoxLayout(self)
        self.button = QPushButton('Start')
        layout.addWidget(self.button)
        self.button.clicked.connect(self.open_second_window)

    def open_second_window(self):
        self.second_window = SecondWindow()
        self.second_window.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = FirstWindow()
    win.show()
    sys.exit(app.exec_())
