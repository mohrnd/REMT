import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt, QSize

class LoadingGif(object):

    def mainUI(self, FrontWindow):
        FrontWindow.setObjectName("FTwindow")
        FrontWindow.resize(320, 300)
        self.centralwidget = QtWidgets.QWidget(FrontWindow)
        self.centralwidget.setObjectName("main-widget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(25, 25, 200, 200))
        self.label.setMinimumSize(QtCore.QSize(250, 250))
        self.label.setMaximumSize(QtCore.QSize(250, 250))
        self.label.setObjectName("lb1")
        FrontWindow.setCentralWidget(self.centralwidget)
        self.LoadingSetup(45, 45)
        
    def LoadingSetup(self, x, y):
        self.movie = QMovie("../REMT/Tests/loading_anim/loading.gif")
        self.movie.setScaledSize(QSize(x, y))
        self.label.setMovie(self.movie)
        self.label.setStyleSheet('QLabel { background: transparent; }')
        self.label.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)
        self.startAnimation()

    # Start Animation
    def startAnimation(self):
        self.movie.start()
        self.timer = QtCore.QTimer()
        self.timer.singleShot(2000, self.stopAnimation)


    def stopAnimation(self):
        self.movie.stop()
        self.label.hide()

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()
demo = LoadingGif()
demo.mainUI(window)
window.show()
sys.exit(app.exec_())
