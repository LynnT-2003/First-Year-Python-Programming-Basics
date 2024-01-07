#DO NOT TOUCH!
import ReadWriteModule
data = ReadWriteModule.readFile("academicrecords")
#DO NOT TOUCH!

'NUMBER 4 WORKING (WITHOUT WRITE MODULE'
grade = input("Enter grade to look up: ")

match4 = False
temp4 = [] #store indices of rows where the grade is A
for i in range (len(data)):
    if data[i][4] == grade:
        match4 = True
        temp4.append(i)

if match4 == True:
    for each in temp4:
        print(f"{data[each][2]} ({data[each][3]}) {data[each][4]}")
elif match4 == False:
    print(f"Error: No academic records found for {grade} grade!")

'TESTING SECOND TIME (SUCCESSFUL)'
'NUMBER 4 WORKING (WITHOUT WRITE MODULE'
grade = input("Enter grade to look up: ")

match4 = False
temp4 = [] #store indices of rows where the grade is A
for i in range (len(data)):
    if data[i][4] == grade:
        match4 = True
        temp4.append(i)

if match4 == True:
    for each in temp4:
        print(f"{data[each][2]} ({data[each][3]}) {data[each][4]}")
elif match4 == False:
    print(f"Error: No academic records found for {grade} grade!")


               
