from PyQt5.QtWidgets import QApplication, QHBoxLayout, QTextEdit, QWidget
from pyqt_line_number_widget import LineNumberWidget


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.__te = QTextEdit()
        self.__te.textChanged.connect(self.__line_widget_line_count_changed)
        self.__lineWidget = LineNumberWidget(self.__te)

        lay = QHBoxLayout()
        lay.addWidget(self.__lineWidget)
        lay.addWidget(self.__te)

        self.setLayout(lay)

    def __line_widget_line_count_changed(self):
        if self.__lineWidget:
            n = int(self.__te.document().lineCount())
            self.__lineWidget.changeLineCount(n)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()