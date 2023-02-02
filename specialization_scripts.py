import sqlite3

conn = sqlite3.connect('graduate_tracking_system.db')

lines=[]
with open("specialization data/specialization.txt", "r") as file:
    lines = file.readlines()

with open("specialization data/data_with_name.txt", "w") as file:
    for line in lines:
        # print(type(str(line)),"#####################")
        f_c = line.index(",")
        s_c = line.index(",",f_c+1)
        number = line[f_c+1:s_c]
        cursor = conn.cursor()
        # number = int(number)
        cursor.execute("SELECT name FROM COURSE WHERE number = (?)",(number,))
        records = cursor.fetchall()
        try:
            name = records[0][0]
        except IndexError:
            print(line, name, records)
            break
        newline = line[:s_c]+","+name+line[s_c:]
        file.write(newline)

conn.commit()
conn.close()