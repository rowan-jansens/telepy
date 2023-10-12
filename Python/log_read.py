import numpy as np

with open("log_files/9_8_0846.txt", "r") as file:
    lines = file.readlines()

    for line in lines:
        line = np.asarray(line.strip('\n').split(",")[:-1], dtype=np.float32)
        print(line)
        print(line[15])