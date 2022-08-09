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
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        plot_LUT = {"x_accel": ["Accel", "y"],
                 "y_accel": ["Accel", "r"],
                 "z_accel": ["Accel", "m"],
                 "x_gyr": ["Gyro", "y"],
                 "y_gyr": ["Gyro", "r"],
                 "z_gyr": ["Gyro", "m"]}

        
        self.ui.connect_button.clicked.connect(self.open_serial)
        self.ui.disconnect_button.clicked.connect(self.close_serial)

        for i in range(6):
            data_series = list(plot_LUT.keys())[i]
            plot_widget = plot_LUT[data_series][0]
            series_color = plot_LUT[data_series][1]
            
            setattr(self.ui, data_series, getattr(self.ui, plot_widget).plot(name=data_series, pen=series_color, width=4))


    def update_plot(self, data_series, x, y):
        getattr(self.ui, data_series).setData(x,y)

    def open_serial(self):
        self.init_data()
        self.ser = serial.Serial("COM4", 115200)  # change COM# if necessary
        time.sleep(2)
        self.ser.flushInput
        # print(self.ser.readline())
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.fetch_serial_data)
        self.timer.start(10)
    
    def close_serial(self):
        self.ser.close()
        self.timer.timeout.disconnect()


    def init_data(self):
        self.data_entries = 7
        self.data_buffer  = 200
        self.data_array = np.zeros([self.data_buffer, self.data_entries], dtype = np.float64)
        self.x = np.arange(-1 * self.data_buffer, 0, 1)

    def fetch_serial_data(self):
        while (self.ser.in_waiting > 0):
            self.line = self.ser.readline()
            self.line = np.asarray(self.line.decode().rstrip('\n').split(","), dtype=np.single)
            # print(line)
            self.data_array = np.append(self.data_array, [self.line], axis=0)
            self.data_array = self.data_array[1:, :]
            self.data_rate = (int(1 / ((np.mean(np.diff(self.data_array[180:, 0]))) / 1000)))
            if self.data_rate == 0:
                self.data_rate = 1
        GC.update_plot("x_accel", self.x / self.data_rate, self.data_array[:,1])
        GC.update_plot("y_accel", self.x / self.data_rate, self.data_array[:,2])
        GC.update_plot("z_accel", self.x / self.data_rate, self.data_array[:,3])
        GC.update_plot("x_gyr", self.x / self.data_rate, self.data_array[:,4])
        GC.update_plot("y_gyr", self.x / self.data_rate, self.data_array[:,5])
        GC.update_plot("z_gyr", self.x / self.data_rate, self.data_array[:,6])





        

if __name__ == "__main__":

    
    app = QtWidgets.QApplication([])

    GC = MainWindow()

    GC.show()

    sys.exit(app.exec())
    ser.close()
    