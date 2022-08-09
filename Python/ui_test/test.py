# live_plot_sensor.py

import time
from turtle import end_fill
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation


    # whole_line = ser.readline()
    # line_array = split(whole_line, ",")
    # print(line_array)

# set up the serial line
ser = serial.Serial("COM4", 115200)  # change COM# if necessary
time.sleep(2)


while True:
    if(ser.in_waiting > 100):
        while (ser.in_waiting > 0):
            line = ser.readline()
            line = line.decode().split(",")
            print(line)
            # print(ser.in_waiting)
        
    

ser.close()
