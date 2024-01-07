#DO NOT TOUCH!
import ReadWriteModule
data = ReadWriteModule.readFile("academicrecords")
#DO NOT TOUCH!

'ADDING RECORD COMPLETE (WITHOUT USING WRITE MODULE)'
temp = []

temp.append(input("Enter academic year: "))
temp.append(input("Enter academic term: "))
temp.append(input("Enter course code: "))
    
match = False

for j in range (len(data)): #checking if the course code of the same semester and year exists
    if data[j][0] == temp[0] and data[j][1] == temp[1] and data[j][2] == temp[2]:
        match = True 

if match == False: #if the course code of the same semester and year doesn't exist
    temp.append(input("Enter section number: ")) #keep asking for other data
    temp.append(input("Enter grade result: ")) #keep asking for other data
    temp.append(input("Enter course credit: ")) #keep asking for other data
    data.append(temp) #append all the data together into the data list
    print (data)
    print (f"{temp[2]} added.")
elif match == True: #if the course code of the same semester and year exists
    print(f"{temp[2]} already exists in {temp[1]}/{temp[0]}.")
    
#print (temp) #testing
###################################################################################################

'TESTING FOR TWO SECOND TIME IN ONE RUN'
'ADDING RECORD COMPLETE (WITHOUT USING WRITE MODULE)'
temp = []

temp.append(input("Enter academic year: "))
temp.append(input("Enter academic term: "))
temp.append(input("Enter course code: "))
    
match = False

for j in range (len(data)): #checking if the course code of the same semester and year exists
    if data[j][0] == temp[0] and data[j][1] == temp[1] and data[j][2] == temp[2]:
        match = True 

if match == False: #if the course code of the same semester and year doesn't exist
    temp.append(input("Enter section number: ")) #keep asking for other data
    temp.append(input("Enter grade result: ")) #keep asking for other data
    temp.append(input("Enter course credit: ")) #keep asking for other data
    data.append(temp) #append all the data together into the data list
    print (data)
    print (f"{temp[2]} added.")
elif match == True: #if the course code of the same semester and year exists
    print(f"{temp[2]} already exists in {temp[1]}/{temp[0]}.")
