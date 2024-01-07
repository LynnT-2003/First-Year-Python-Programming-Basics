#DO NOT TOUCH!
import ReadWriteModule
data = ReadWriteModule.readFile("academicrecords")
#DO NOT TOUCH!

'NUMBER 6 WORKING (WITHOUT WRITE MODULE)'
year6 = input('Enter academic year : ') #input year 
term6 = input('Enter academic term: ') #input term 
code6 = input('Enter course code: ') #input course

match6 = False #initialise with match6 = False
for i in range (len(data)): #search if there are any records that matches all the criteria
    if data[i][2] == code6 and term6 == data[i][1] and code6 == data[i][2]:
        match6 = True #if a record that matches criteria is found, match6 will become True
        x6 = i #X marks the spot
        
print(data) #testing
print(match6) #testing

if match6 == True: #if there is a match
    new_grade = input("Enter grade result: ") #ask for the new grade result to replace the old grade
    data[x6][4] = new_grade #replace using the x6 index
elif match6 == False: #if there is no match
    print(f"Error: {code6} not found for {term6}/{year6}!") #error message

print(data) #testing

'TESTING SECOND TIME (SUCCESSFUL)'
'NUMBER 6 WORKING (WITHOUT WRITE MODULE)'
year6 = input('Enter academic year : ') #input year 
term6 = input('Enter academic term: ') #input term 
code6 = input('Enter course code: ') #input course

match6 = False #initialise with match6 = False
for i in range (len(data)): #search if there are any records that matches all the criteria
    if data[i][2] == code6 and term6 == data[i][1] and code6 == data[i][2]:
        match6 = True #if a record that matches criteria is found, match6 will become True
        x6 = i #X marks the spot
        
print(data) #testing
print(match6) #testing

if match6 == True: #if there is a match
    new_grade = input("Enter grade result: ") #ask for the new grade result to replace the old grade
    data[x6][4] = new_grade #replace using the x6 index
elif match6 == False: #if there is no match
    print(f"Error: {code6} not found for {term6}/{year6}!") #error message

print(data) #testing

        
