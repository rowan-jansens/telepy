# edit UI $.\Scripts\pyside6-designer.exe .\gsui.ui
# convert UI to PY = $.\Scripts\pyside6-uic.exe gsui.ui -o gsui_py.py

# start virtual evironment Scripts\Activate
# .\.venv\Scripts\pyside6-designer.exe .\Python\gsui.ui 

import re
import sys
import random
from tkinter.ttk import Separator
from PySide6 import QtCore, QtWidgets, QtGui
from gsui_py import Ui_MainWindow
import numpy as np
import serial
import time
import serial.tools.list_ports
import math


import pyqtgraph as pg


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('telepy.png'))





        self.setWindowTitle("TelePy - Ground Station")
        pg.setConfigOptions(antialias=True)

        plot_LUT = {"bar_alt": ["Plot1", "m"],
                    "kf_alt": ["Plot1", "g"],
                    "trigger_alt": ["Plot1", "b"],

                    "kf_vel": ["Plot2", "b"],
                    "Int_vel": ["Plot2", "r"],
                    "trigger_vel": ["Plot2", "g"],
                    
                 "x_accel": ["Plot4", "y"],
                 "y_accel": ["Plot4", "r"],
                 "z_accel": ["Plot4", "m"],

                 "x_gyr": ["Plot5", "y"],
                 "y_gyr": ["Plot5", "r"],
                 "z_gyr": ["Plot5", "m"],

                 "x_ang": ["Plot6", "y"],
                 "y_ang": ["Plot6", "r"],
                 "z_ang": ["Plot6", "m"],
                 
                 "temp": ["Plot3", "y"]}

        ports = list(serial.tools.list_ports.comports())
        for p in ports:
            self.ui.serial_port.addItem((str(p)[0:5]))
        self.ui.serial_baud.setCurrentIndex(7)
        self.num_lines_read = 0
        self.status_que = []
        

        # connect buttons and sliders
        self.ui.connect_button.clicked.connect(self.open_serial)
        self.ui.disconnect_button.clicked.connect(self.close_serial)
        self.ui.resize_button.clicked.connect(self.resize_plots)
        self.ui.save_button.clicked.connect(self.save_now)


        self.ui.Plot1.addLegend()
        self.ui.Plot1.setTitle("Altitude", color=[85, 170, 255], size="12pt")
        self.ui.Plot2.addLegend()
        self.ui.Plot2.setTitle("Velocity", color=[85, 170, 255], size="12pt")
        self.ui.Plot3.addLegend()
        self.ui.Plot3.setTitle("Temperature", color=[85, 170, 255], size="12pt")
        self.ui.Plot4.addLegend()
        self.ui.Plot4.setTitle("Linear Accel", color=[85, 170, 255], size="12pt")
        self.ui.Plot5.addLegend()
        self.ui.Plot5.setTitle("Angular Accel", color=[85, 170, 255], size="12pt")
        self.ui.Plot6.addLegend()
        self.ui.Plot6.setTitle("Orientation", color=[85, 170, 255], size="12pt")


        self.status_timer = QtCore.QTimer()
        self.status_timer.timeout.connect(self.clear_status)
        



        for i in range(len(plot_LUT)):
            data_series = list(plot_LUT.keys())[i]
            plot_widget = plot_LUT[data_series][0]
            series_color = pg.mkPen(color=plot_LUT[data_series][1], width=5)

            setattr(self.ui, data_series, getattr(self.ui, plot_widget).plot(name=data_series, pen=series_color))
        


    def update_plot(self, data_series, x, y):
        getattr(self.ui, data_series).setData(x,y)
        

    def open_serial(self):
        try:
            self.init_data()
            self.ser = serial.Serial(self.ui.serial_port.currentText(), int(self.ui.serial_baud.currentText()))  # change COM# if necessary
            time.sleep(1)
            test_byte = ord(self.ser.read(1))
            if test_byte == 64:
                self.print_status("Connection sucessfull")
                time.sleep(2)
                self.ser.flushInput
                self.timer = QtCore.QTimer()
                self.timer.timeout.connect(self.fetch_serial_data)
                self.timer.start(50)
            else:
                self.print_status("Connection failed!")
                self.ser.close()
        except:
            self.print_status("Connection failed!")



    
    def close_serial(self):
        self.ser.close()
        self.print_status("Serial Closed")
        self.timer.timeout.disconnect()
        self.add_data_to_file()
        

    def resize_plots(self):
        self.ui.Plot1.enableAutoRange()
        self.ui.Plot2.enableAutoRange()
        self.ui.Plot3.enableAutoRange()
        self.ui.Plot4.enableAutoRange()
        self.ui.Plot5.enableAutoRange()
        self.ui.Plot6.enableAutoRange()


    def init_data(self):
        self.data_entries = 28
        self.data_buffer  = 300
        self.data_array = np.zeros([self.data_buffer, self.data_entries], dtype = np.float64)
        self.x = np.arange(-1 * self.data_buffer, 0, 1)

        




    def fetch_serial_data(self):

        # read lines
        while (self.ser.in_waiting > 0):
            self.line = self.ser.readline()
            self.num_lines_read += 1

            # decode line and append to buffer
            self.line = np.asarray(self.line.decode().rstrip('\n').split(","), dtype=np.single)
            self.data_array = np.append(self.data_array, [self.line], axis=0)

            #update data array using current buffer size set by slider
            self.data_array = self.data_array[1:, :]
            self.data_rate = (int(1 / ((np.mean(np.diff(self.data_array[180:, 0]))) / 1000)))

            # check for zero data rate
            if self.data_rate == 0:
                self.data_rate = 1

            # check for save state condition
            if self.num_lines_read > self.data_buffer:
                self.add_data_to_file()

            
        # print(self.num_lines_read)
        self.update_window()

    def print_status(self, text):
        if text != "#return#":
            self.status_que.append(text)
        if not self.status_timer.isActive():
            self.ui.print_debug.setText(self.status_que[0])
            self.status_que.pop(0)
            self.status_timer.start(2000)

    def clear_status(self):
        self.ui.print_debug.setText("     ")
        self.status_timer.stop()
        if len(self.status_que) > 0:
            self.print_status("#return#")
    



    def update_window(self):
        speed_scale = self.ui.plot_speed.value()

        if (self.num_lines_read%1) == 0:
            phase_color = np.random.normal(120, 30, 3)

            phase_labels = ["IDLE", "ARMED", "ASCENT", "APOGEE", "DECENT"]
            phase_colors = ["85, 156, 242", "232, 21, 21", "224, 104, 29", "214, 61, 217", "61, 217, 82"]



            self.ui.phase_indicator.setText(phase_labels[int(self.line[15])-1])
            
            self.ui.phase_indicator.setStyleSheet(u"font: 20pt \"Calibri\";\n"
"background-color: rgb(" + phase_colors[int(self.line[15])-1]  + ");\n"
"color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(188, 214, 255);\n"
"border-radius: 10px;")

        self.update_plot("x_accel", self.x[-speed_scale:] / self.data_rate, self.data_array[-speed_scale:,1])
        self.update_plot("y_accel", self.x[-speed_scale:] / self.data_rate, self.data_array[-speed_scale:,2])
        self.update_plot("z_accel", self.x[-speed_scale:] / self.data_rate, self.data_array[-speed_scale:,3])
        self.update_plot("x_gyr", self.x[-speed_scale:] / self.data_rate, self.data_array[-speed_scale:,4])
        self.update_plot("y_gyr", self.x[-speed_scale:] / self.data_rate, self.data_array[-speed_scale:,5])
        self.update_plot("z_gyr", self.x[-speed_scale:] / self.data_rate, self.data_array[-speed_scale:,6])
        self.update_plot("x_ang", self.x[-speed_scale:] / self.data_rate, self.data_array[-speed_scale:,8])
        self.update_plot("y_ang", self.x[-speed_scale:] / self.data_rate, self.data_array[-speed_scale:,9])
        self.update_plot("z_ang", self.x[-speed_scale:] / self.data_rate, self.data_array[-speed_scale:,10])
        self.update_plot("temp", self.x[-speed_scale:] / self.data_rate, self.data_array[-speed_scale:,7])

        self.update_plot("trigger_alt", self.x[-speed_scale:] / self.data_rate, self.data_array[-speed_scale:,20])
        self.update_plot("trigger_vel", self.x[-speed_scale:] / self.data_rate, self.data_array[-speed_scale:,19])


        self.update_plot("bar_alt", self.x[-speed_scale:] / self.data_rate, self.data_array[-speed_scale:,11])
        # self.update_plot("Int_vel", self.x[-speed_scale:] / self.data_rate, self.data_array[-speed_scale:,23])
        # self.update_plot("Dir_vel", self.x[-speed_scale:] / self.data_rate, self.data_array[-speed_scale:,22])
        self.update_plot("kf_alt", self.x[-speed_scale:] / self.data_rate, self.data_array[-speed_scale:,21])
        self.update_plot("kf_vel", self.x[-speed_scale:] / self.data_rate, self.data_array[-speed_scale:,24])

        on_time_seconds = round((self.line[0] / 1000) % 60, 3)
        on_time_minutes = math.floor((self.line[0] / (1000*60))) % 60
       
        
        #plot other textual telemetry elements
        self.ui.on_time.setText("  " + str(on_time_minutes) + ":" + format(on_time_seconds, '.2f') + "  ")
        self.ui.stats_1.setText(str(round(self.data_rate)) +"Hz\n" + str(round((self.data_array[-1,0] - self.data_array[-2,0]) / 10 )*10) + "ms\n" + str(round(self.line[17], 2)) + "v\n" + str(self.line[27]) + "%")

        pyro_code = str(int(self.line[16]))
    
        pyro_one_state = pyro_code[2]
        pyro_two_state = pyro_code[1]
        arm_state = pyro_code[3]

        self.ui.stats_2.setText("[" + pyro_one_state + ", " + pyro_two_state + "]\n"+ str(round(self.line[13], 7)) + "\n" + str(round(self.line[12], 7)) + "\n" + str(round(self.line[14], 3)))
    


    def save_now(self):
        self.ui.save_data_option.setChecked(True)
        if hasattr(self, "data_array"):
            self.add_data_to_file()


    def add_data_to_file(self):

        if self.ui.save_data_option.isChecked():
            if "file_name" not in globals():
                global file_name
                self.data_in_file = 0
                time_struct = time.gmtime()
                file_name = "log_files/" + str(time_struct.tm_mon) + "_" + str(time_struct.tm_mday) + "_" + str(round(time.time()))[-5:-1] + ".txt"
                with open(file_name, 'w') as f:
                    f.write("time,ax,ay,az,gx,gy,gz,\n")
                self.print_status("File Created: " + file_name[10:])

            if self.num_lines_read < self.data_buffer:
                self.data_in_file += self.num_lines_read
            else:
                self.data_in_file += self.data_buffer
            with open(file_name, 'a') as f:
                f.writelines(np.array2string(self.data_array[-self.num_lines_read:, :], separator=',', edgeitems=300, max_line_width=300).replace('[','').replace(']','').replace(' ',''))
                f.write('\n')
            self.ui.data_points_in_file.setText("  " + str(self.data_in_file) + "  ")
            self.num_lines_read = 0
            self.print_status("Data Saved")
        





        

if __name__ == "__main__":


    app = QtWidgets.QApplication([])
    GC = MainWindow()


    GC.show()
    sys.exit(app.exec())
    ser.close()
    