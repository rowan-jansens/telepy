import serial.tools.list_ports


ports = list(serial.tools.list_ports.comports())
for p in ports:
    print(str(p)[0:4])
