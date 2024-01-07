#DO NOT TOUCH!
import ReadWriteModule
data = ReadWriteModule.readFile("academicrecords")
#DO NOT TOUCH!

#print (data[48]) #test

'REMOVING RECORD COMPLETE (WITHOUT WRITE MODULE)'
match2 = False
course = input('Enter course code: ')
for i in range (len(data)): #searching if any row contains the course code
    #print (data[i][2]) #testing
    if (data[i][2]) == course: #searching if any row contains the course code
        print ('Match found!') #testing purposes
        x = i #x = the index for the row that contains the course code
        match2 = True

if match2 == True: #if course code exists
    data.remove(data[x]) #remove the tow that contains the course using the value of x
    print(f"{course} removed.")
    print (data) #testing
else: #if course code does not exist
    print (f"{course} does not exist!")

#print (data[0]) #testing

'TESTING SECOND TIME (SUCCESSFUL)'
'REMOVING RECORD COMPLETE (WITHOUT WRITE MODULE)'
match2 = False
course = input('Enter course code: ')
for i in range (len(data)): #searching if any row contains the course code
    #print (data[i][2]) #testing
    if (data[i][2]) == course: #searching if any row contains the course code
        print ('Match found!') #testing purposes
        x = i #x = the index for the row that contains the course code
        match2 = True

if match2 == True: #if course code exists
    data.remove(data[x]) #remove the tow that contains the course using the value of x
    print(f"{course} removed.")
    print (data) #testing
else: #if course code does not exist
    print (f"{course} does not exist!")



