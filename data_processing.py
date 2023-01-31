file = open("csv/courses.txt", "r")
Lines = file.readlines()
file2 = open("csv/data.txt", "w")
for line in Lines:
    if line[:4] == "INLS":
        writeLine = "INLS, "+line[5:8]+", "
        pare_idx = line.find("(")
        writeLine += line[10:pare_idx-1] + ", "
        credits = "3"
        if line[pare_idx+1] == "1":
            credits = "1.5"
        file2.writelines(writeLine + credits + ", 0\n")

