import numpy as np


data_entries = 27
data_buffer  = 200
data = np.zeros([data_buffer, data_entries], dtype = np.float64)
x = np.arange(-1 * data_buffer, 0, 1)




def fetch_serial_data():
    global GC, data, x, data_rate, ser
    while (ser.in_waiting > 0):
        line = ser.readline()
        line = np.asarray(line.decode().rstrip('\n').split(","), dtype=np.single)
        # print(line)
        data = np.append(data, [line], axis=0)
        data = data[1:, :]
        data_rate = (int(1 / ((np.mean(np.diff(data[180:, 0]))) / 1000)))
        if data_rate == 0:
            data_rate = 1


    GC.update_plot("bar_alt", x / data_rate, data[:,11])
    GC.update_plot("kf_alt", x / data_rate, data[:,21])

    GC.update_plot("temp", x / data_rate, data[:,7])

    GC.update_plot("x_accel", x / data_rate, data[:,1])
    GC.update_plot("y_accel", x / data_rate, data[:,2])
    GC.update_plot("z_accel", x / data_rate, data[:,3])
    GC.update_plot("x_gyr", x / data_rate, data[:,4])
    GC.update_plot("y_gyr", x / data_rate, data[:,5])
    GC.update_plot("z_gyr", x / data_rate, data[:,6])
    GC.update_plot("x_euler", x / data_rate, data[:,8])
    GC.update_plot("y_euler", x / data_rate, data[:,9])
    GC.update_plot("z_euler", x / data_rate, data[:,10])


    #     with open('readme.txt', 'w') as f:
    # f.write('readme')