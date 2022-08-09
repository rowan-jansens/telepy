import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from gsui_py import Ui_MainWindow
import numpy as np
import serial
import time
import serial.tools.list_ports



import pyqtgraph as pg


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        pg.setConfigOptions(antialias=True)

        plot_LUT = {"x_accel": ["Accel", "y"],
                 "y_accel": ["Accel", "r"],
                 "z_accel": ["Accel", "m"],
                 "x_gyr": ["Gyro", "y"],
                 "y_gyr": ["Gyro", "r"],
                 "z_gyr": ["Gyro", "m"]}

        ports = list(serial.tools.list_ports.comports())
        for p in ports:
            self.ui.serial_port.addItem((str(p)[0:4]))
        self.ui.serial_baud.setCurrentIndex(7)
        self.num_lines_read = 0

        
        self.ui.connect_button.clicked.connect(self.open_serial)
        self.ui.disconnect_button.clicked.connect(self.close_serial)
        self.ui.resize_button.clicked.connect(self.resize_plots)
        self.ui.save_button.clicked.connect(self.add_data_to_file)

        self.ui.Accel.addLegend()
        self.ui.Accel.setTitle("Acceleraion", color=[85, 170, 255], size="12pt")
        self.ui.Gyro.addLegend()
        self.ui.Gyro.setTitle("Angular Rate", color=[85, 170, 255], size="12pt")

        for i in range(6):
            data_series = list(plot_LUT.keys())[i]
            plot_widget = plot_LUT[data_series][0]
            series_color = plot_LUT[data_series][1]
            
            setattr(self.ui, data_series, getattr(self.ui, plot_widget).plot(name=data_series, pen=series_color, width=4))
        


    def update_plot(self, data_series, x, y):
        getattr(self.ui, data_series).setData(x,y)
        

    def open_serial(self):
        global file_name
        time_struct = time.gmtime()
        file_name = "log_files/" + str(time_struct.tm_mon) + "_" + str(time_struct.tm_mday) + "_" + str(time.time())[-5:-1] + ".txt"
        print(file_name)
        with open(file_name, 'w') as f:
            f.write("time,ax,ay,az,gx,gy,gz,\n")


        
        # print(self.ui.serial_baud.cu)
        self.init_data()
        self.ser = serial.Serial(self.ui.serial_port.currentText(), int(self.ui.serial_baud.currentText()))  # change COM# if necessary
        time.sleep(2)
        self.ser.flushInput
        # print(self.ser.readline())
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.fetch_serial_data)
        self.timer.start(50)
    
    def close_serial(self):
        self.ser.close()
        self.timer.timeout.disconnect()
        

    def resize_plots(self):
        self.ui.Accel.autoRange()
        self.ui.Gyro.autoRange()



    def init_data(self):
        self.data_entries = 7
        self.data_buffer  = 200
        self.data_array = np.zeros([self.data_buffer, self.data_entries], dtype = np.float64)
        self.x = np.arange(-1 * self.data_buffer, 0, 1)

    def fetch_serial_data(self):
        while (self.ser.in_waiting > 0):
            self.line = self.ser.readline()
            self.num_lines_read += 1
            self.line = np.asarray(self.line.decode().rstrip('\n').split(","), dtype=np.single)
            # print(line)
            self.data_array = np.append(self.data_array, [self.line], axis=0)
            self.data_array = self.data_array[1:, :]
            self.data_rate = (int(1 / ((np.mean(np.diff(self.data_array[180:, 0]))) / 1000)))
            if self.data_rate == 0:
                self.data_rate = 1
            if self.num_lines_read > self.data_buffer:
                self.add_data_to_file()
        print(self.num_lines_read)
        
        GC.update_plot("x_accel", self.x / self.data_rate, self.data_array[:,1])
        GC.update_plot("y_accel", self.x / self.data_rate, self.data_array[:,2])
        GC.update_plot("z_accel", self.x / self.data_rate, self.data_array[:,3])
        GC.update_plot("x_gyr", self.x / self.data_rate, self.data_array[:,4])
        GC.update_plot("y_gyr", self.x / self.data_rate, self.data_array[:,5])
        GC.update_plot("z_gyr", self.x / self.data_rate, self.data_array[:,6])


    def add_data_to_file(self):
        with open(file_name, 'a') as f:
            f.writelines(np.array2string(self.data_array[-self.num_lines_read:, :], separator=',', edgeitems=300, max_line_width=300).replace('[','').replace(']',''))
            f.write('\n')
        self.num_lines_read = 0




        

if __name__ == "__main__":

    
    app = QtWidgets.QApplication([])

    GC = MainWindow()

    GC.show()

    sys.exit(app.exec())
    ser.close()
    