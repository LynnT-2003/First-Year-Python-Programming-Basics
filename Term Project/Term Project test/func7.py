#DO NOT TOUCH!
import ReadWriteModule
data = ReadWriteModule.readFile("academicrecords")
#DO NOT TOUCH!

'NUMBER 7 IN PROGRES'
def func7():
    temp7 = [['S',0],['A',0],['A-',0],['B+',0],['B',0],['B-',0],['C+',0],['C',0],['C-',0],['D',0],['F',0]]

    total_GRWxC = 0
    totalC = 0

    for i in range(len(data)):
        data[i][5] = int(data[i][5])
        if data[i][4] == 'A':
            total_GRWxC += 4*data[i][5]
        elif data[i][4] == 'A-':
            total_GRWxC += 3.75*data[i][5]
        elif data[i][4] == 'B+':
            total_GRWxC += 3.25*data[i][5]
        elif data[i][4] == 'B':
            total_GRWxC += 3*data[i][5]
        elif data[i][4] == 'B-':
            total_GRWxC += 2.75*data[i][5]
        elif data[i][4] == 'C+':
            total_GRWxC += 2.25*data[i][5]
        elif data[i][4] == 'C':
            total_GRWxC += 2*data[i][5]
        elif data[i][4] == 'C-':
            total_GRWxC += 1.75*data[i][5]
        elif data[i][4] == 'D':
            total_GRWxC += 1*data[i][5]
        elif data[i][4] == 'F':
            total_GRWxC += 1*data[i][5]

    for i in range(len(data)):
        if data[i][5] != 0:
            totalC += data[i][5]

    GPA = total_GRWxC / totalC
    print (GPA)

func7()









