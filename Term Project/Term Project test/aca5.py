#DO NOT TOUCH!
import ReadWriteModule
data = ReadWriteModule.readFile("academicrecords")
#DO NOT TOUCH!

'NUMBER 5 WORKING (WITHOUT WRITE MODULE)'
temp5 = [['S',0],['A',0],['A-',0],['B+',0],['B',0],['B-',0],['C+',0],['C',0],['C-',0],['D',0],['F',0]]

for i in range (len(data)): #check grade result in every row
    if data[i][4] == 'S':
        temp5[0][1] += 1 #store count of the grade result from if statement
    elif data[i][4] == 'A':
        temp5[1][1] += 1 #store count of the grade result from if statement
    elif data[i][4] == 'A-':
        temp5[2][1] += 1 #store count of the grade result from if statement
    elif data[i][4] == 'B+':
        temp5[3][1] += 1 #store count of the grade result from if statement
    elif data[i][4] == 'B-':
        temp5[4][1] += 1 #store count of the grade result from if statement
    elif data[i][4] == 'B':
        temp5[5][1] += 1 #store count of the grade result from if statement
    elif data[i][4] == 'C+':
        temp5[6][1] += 1 #store count of the grade result from if statement
    elif data[i][4] == 'C-':
        temp5[7][1] += 1 #store count of the grade result from if statement
    elif data[i][4] == 'C':
        temp5[8][1] += 1 #store count of the grade result from if statement
    elif data[i][4] == 'D':
        temp5[9][1] += 1 #store count of the grade result from if statement
    elif data[i][4] == 'F':
        temp5[10][1] += 1 #store count of the grade result from if statement

norecord = True #initialise with the condition that there are no academic records
for k in range (len(temp5)):
    if temp5[k][1] != 0:
        norecord = False #if at least one row has a valid grade result, norecord will become False

if norecord == False: 
    for j in range (len(temp5)): #print grade results and the count ONLY if count > 0
        if temp5[j][1] > 0:
            print (f"Grade{temp5[j][0]}\t{temp5[j][1]}")
elif norecord == True:
    print("Error: No academic records found!") #print error message 

'TESTING SECOND TIME (SUCCESSFUL)'
'NUMBER 5 WORKING (WITHOUT WRITE MODULE)'
temp5 = [['S',0],['A',0],['A-',0],['B+',0],['B',0],['B-',0],['C+',0],['C',0],['C-',0],['D',0],['F',0]]

for i in range (len(data)): #check grade result in every row
    if data[i][4] == 'S':
        temp5[0][1] += 1 #store count of the grade result from if statement
    elif data[i][4] == 'A':
        temp5[1][1] += 1 #store count of the grade result from if statement
    elif data[i][4] == 'A-':
        temp5[2][1] += 1 #store count of the grade result from if statement
    elif data[i][4] == 'B+':
        temp5[3][1] += 1 #store count of the grade result from if statement
    elif data[i][4] == 'B-':
        temp5[4][1] += 1 #store count of the grade result from if statement
    elif data[i][4] == 'B':
        temp5[5][1] += 1 #store count of the grade result from if statement
    elif data[i][4] == 'C+':
        temp5[6][1] += 1 #store count of the grade result from if statement
    elif data[i][4] == 'C-':
        temp5[7][1] += 1 #store count of the grade result from if statement
    elif data[i][4] == 'C':
        temp5[8][1] += 1 #store count of the grade result from if statement
    elif data[i][4] == 'D':
        temp5[9][1] += 1 #store count of the grade result from if statement
    elif data[i][4] == 'F':
        temp5[10][1] += 1 #store count of the grade result from if statement

norecord = True #initialise with the condition that there are no academic records
for k in range (len(temp5)):
    if temp5[k][1] != 0:
        norecord = False #if at least one row has a valid grade result, norecord will become False

if norecord == False: 
    for j in range (len(temp5)): #print grade results and the count ONLY if count > 0
        if temp5[j][1] > 0:
            print (f"Grade{temp5[j][0]}\t{temp5[j][1]}")
elif norecord == True:
    print("Error: No academic records found!") #print error message 
