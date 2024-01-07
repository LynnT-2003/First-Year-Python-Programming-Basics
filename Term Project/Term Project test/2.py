#DO NOT TOUCH!
import ReadWriteModule
data = ReadWriteModule.readFile("academicrecords")
#DO NOT TOUCH!

#print (data[48]) #test

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
else: #if course code exists
    print (f"{course} does not exist!")

#print (data[0]) #testing

'''if match2 == True:
    print (data) #for resting purposes
    print (f'{course} removed!')
elif match2 == False:
    print (f'{course} does not exist in the file!')'''
    



