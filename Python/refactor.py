with open("log_files/9_8_0846.txt", "r") as file:
    with open("log_files/9_8_0846_refactored.txt", "w") as file2:
        line = file.readline()
        while line != " ":
            file2.write(line.strip()+file.readline())
            line = file.readline()