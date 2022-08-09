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

        plot_LUT = {"x_accel": ["Pos", "y"],
                 "y_accel": ["Pos", "r"],
                 "z_accel": ["Vel", "m"]}


        pg.setConfigOptions(antialias=True)
        self.text = QtWidgets.QLabel("Ground Control",
                                     alignment=QtCore.Qt.AlignCenter)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)



        for i in range(3):
            current_widgets = list(vars(self).keys())
            data_series = list(plot_LUT.keys())[i]
            plot_widget = plot_LUT[data_series][0]
            series_color = plot_LUT[data_series][1]
            
            #if widget does not exist, make new widget and add to screen
            if plot_widget not in current_widgets:
                setattr(self, plot_widget, pg.PlotWidget(title=plot_widget))
                self.layout.addWidget(getattr(self, plot_widget))


            #add series to widget and set line style
            setattr(self, data_series, getattr(self, plot_widget).plot(pen=series_color))


    def update_plot(self, plot_name, x, y):
        getattr(self, plot_name).setData(x,y)


        

if __name__ == "__main__":

    ser = serial.Serial("COM4", 115200)  # change COM# if necessary
    time.sleep(2)
    ser.flushInput


    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)


    data_entries = 4
    data_buffer  = 6
    data = np.empty([data_buffer, data_entries])
    print(data.shape)

    i = 0
    def update():
        global widget, i, data
        while (ser.in_waiting > 0):
            line = ser.readline()
            line = np.asarray(line.decode().rstrip('\n').split(","), dtype=np.single)
            print(line)
            data = np.append(data, [line], axis=0)
            data = data[1:, :]
            
        t = np.arange(0,3.0,0.01)
        y1 = np.sin(4 * np.pi * t + i)
        y2 = np.cos(2 * np.pi * t + i)
        y3 = np.cos(1.5 * np.pi * t + i + 1.5)
        widget.update_plot("x_accel", t, y1)
        widget.update_plot("y_accel", t, y2)
        widget.update_plot("z_accel", t, y3)
        i += 0.1

    timer = QtCore.QTimer()
    timer.timeout.connect(update)
    timer.start(10)


    widget.show()

    sys.exit(app.exec())
    ser.close()
    