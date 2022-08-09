import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from gsui_py import Ui_MainWindow
import numpy as np
import serial
import time


import pyqtgraph as pg



class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        plot_LUT = {"x_accel": ["Accel", "y"],
                 "y_accel": ["Accel", "r"],
                 "z_accel": ["Accel", "m"],
                 "x_gyr": ["Gyro", "y"],
                 "y_gyr": ["Gyro", "r"],
                 "z_gyr": ["Gyro", "m"]}


        for i in range(6):
            data_series = list(plot_LUT.keys())[i]
            plot_widget = plot_LUT[data_series][0]
            series_color = plot_LUT[data_series][1]
            
            setattr(self.ui, data_series, getattr(self.ui, plot_widget).plot(name=data_series, pen=series_color, width=4))


    def update_plot(self, data_series, x, y):
        getattr(self.ui, data_series).setData(x,y)




        

if __name__ == "__main__":

    ser = serial.Serial("COM4", 115200)  # change COM# if necessary
    time.sleep(2)
    ser.flushInput


    app = QtWidgets.QApplication([])

    GC = MainWindow()
    GC.resize(800, 600)


    data_entries = 7
    data_buffer  = 200
    data = np.zeros([data_buffer, data_entries], dtype = np.float64)
    x = np.arange(-1 * data_buffer, 0, 1)

    i = 0
    def update():
 
        global GC, data, x, data_rate
        while (ser.in_waiting > 0):
            line = ser.readline()
            line = np.asarray(line.decode().rstrip('\n').split(","), dtype=np.single)
            # print(line)
            data = np.append(data, [line], axis=0)
            data = data[1:, :]
            data_rate = (int(1 / ((np.mean(np.diff(data[180:, 0]))) / 1000)))
            if data_rate == 0:
                data_rate = 1

        GC.update_plot("x_accel", x / data_rate, data[:,1])
        GC.update_plot("y_accel", x / data_rate, data[:,2])
        GC.update_plot("z_accel", x / data_rate, data[:,3])
        GC.update_plot("x_gyr", x / data_rate, data[:,4])
        GC.update_plot("y_gyr", x / data_rate, data[:,5])
        GC.update_plot("z_gyr", x / data_rate, data[:,6])


    timer = QtCore.QTimer()
    timer.timeout.connect(update)
    timer.start(10)


    GC.show()

    sys.exit(app.exec())
    ser.close()
    