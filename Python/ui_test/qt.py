from re import A
import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
import numpy as np
import serial
import time

import pyqtgraph as pg






class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        plot_LUT = {"x_accel": ["Acceleration", "y"],
                 "y_accel": ["Acceleration", "r"],
                 "z_accel": ["Acceleration", "m"],
                 "x_gyr": ["Gyro", "y"],
                 "y_gyr": ["Gyro", "r"],
                 "z_gyr": ["Gyro", "m"]}


        pg.setConfigOptions(antialias=True)
        self.text = QtWidgets.QLabel("Ground Control",
                                     alignment=QtCore.Qt.AlignCenter)

        self.frequency = QtWidgets.QLabel("0Hz",
                                     alignment=QtCore.Qt.AlignCenter)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.frequency)


        for i in range(6):
            current_widgets = list(vars(self).keys())
            data_series = list(plot_LUT.keys())[i]
            plot_widget = plot_LUT[data_series][0]
            series_color = plot_LUT[data_series][1]
            
            #if widget does not exist, make new widget and add to screen
            if plot_widget not in current_widgets:
                setattr(self, plot_widget, pg.PlotWidget(title=plot_widget))
                self.layout.addWidget(getattr(self, plot_widget))
                getattr(self, plot_widget).addLegend()


            #add series to widget and set line style
            setattr(self, data_series, getattr(self, plot_widget).plot(name=data_series, pen=series_color, width=4))


    def update_plot(self, plot_name, x, y):
        getattr(self, plot_name).setData(x,y)


    def update_text(self, hz):
        self.frequency.setText(str(hz) + " Hz")


        

if __name__ == "__main__":

    ser = serial.Serial("COM4", 115200)  # change COM# if necessary
    time.sleep(2)
    ser.flushInput


    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)


    data_entries = 7
    data_buffer  = 200
    data = np.zeros([data_buffer, data_entries], dtype = np.float64)
    x = np.arange(-1 * data_buffer, 0, 1)

    i = 0
    def update():
        global widget, i, data, x, data_rate
        while (ser.in_waiting > 0):
            line = ser.readline()
            line = np.asarray(line.decode().rstrip('\n').split(","), dtype=np.single)
            # print(line)
            data = np.append(data, [line], axis=0)
            data = data[1:, :]
            data_rate = (int(1 / ((np.mean(np.diff(data[180:, 0]))) / 1000)))

        widget.update_plot("x_accel", x / data_rate, data[:,1])
        widget.update_plot("y_accel", x / data_rate, data[:,2])
        widget.update_plot("z_accel", x / data_rate, data[:,3])
        widget.update_plot("x_gyr", x / data_rate, data[:,4])
        widget.update_plot("y_gyr", x / data_rate, data[:,5])
        widget.update_plot("z_gyr", x / data_rate, data[:,6])
        widget.update_text(data_rate)


    timer = QtCore.QTimer()
    timer.timeout.connect(update)
    timer.start(10)

    


    widget.show()

    sys.exit(app.exec())
    ser.close()
    