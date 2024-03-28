from PyQt5 import QtWidgets
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        months = [1,2,3,4,5,6,7,8,9,10]
        temperature = [30,32,34,32,33,31,29,32,35,45]

        self.graphWidget.setBackground('w')

        pen = pg.mkPen(color=(255, 0, 0))

        month_labels = ['10/10/21','10/10/22','10/10/23','10/10/24','10/10/25','10/10/26','10/10/27','10/10/28','10/10/29','10/10/30']
        self.graphWidget.plot(months, temperature, pen=pen)

        ax = self.graphWidget.getAxis('bottom')
        ax.setTicks([[(i, label) for i, label in enumerate(month_labels)]])

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
