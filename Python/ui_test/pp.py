from PySide6 import QtWidgets, QtCore
from PySide6.QtUiTools import loadUiType
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
import serial
import time
import numpy as np
from ui_mainwindow import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        #Load the UI Page
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.plot([1,2,3,4,5,6,7,8,9,10], [30,32,34,32,33,31,29,32,35,45])

    def plot(self, hour, temperature):
        self.ui.p1_data = self.ui.p1.plot(hour, temperature)
        

        


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    GC = MainWindow()

    GC.ui.p1_data.setData([1, 2, 3, 4, 5], [0, 1, 0, 2, 0])


    # x = [1, 2, 3, 4, 5]
    # y = [1, 3, 2, 4, 5]
    # GC.graphWidget.setData(x, y)

    # def update():
    #     global GC, data, x
    #     y = np.random.normal(10,1,size=[100]).tolist
    #     GC.update_plot(x, y)


    # timer = QtCore.QTimer()
    # timer.timeout.connect(update)
    # timer.start(10)



    GC.show()
    sys.exit(app.exec())