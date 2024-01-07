import ReadWriteModule

def addrow():
    data.append([])

def addelement(row,ele):
    data[row].append(ele)

def addrecord(n):
    addrow()
    for i in range (n):
        addelement(len(data)-1,input(f"Enter element{i+1}: "))

data = ReadWriteModule.readFile("test")
print (data)
print(len(data))

#addrecord(int(input("Enter number of elemnts to add in the new record: ")))
temp = []
n = int(input("Enter number of elemnts to add in the new record: "))
for i in range (n):
    temp.append(input(f"Enter element{i+1}: "))
    
match = False
for each in temp:
    for j in range (len(data)-1):
        if data[j][1] == each:
            print ('match found')
            match = True

if match == False:
    data.append(temp)
    

print (f"\nExpected outcome in csv: {data}\n") #havent used write module
print (temp)

'''
print(data)
print(len(data))
print(data)'''

'''
data[len(data)-1].append(10)
data[len(data)-1].append(20)
print(data)
print(len(data))
'''


''' #BEGINNING

import ReadWriteModule

def addrow():
    data.append([])

def addelement(row,ele):
    data[row].append(ele)

def addrecord(n):
    addrow()
    for i in range (n):
        addelement(len(data)-1,input(f"Enter element{i+1}: "))

data = ReadWriteModule.readFile("test")
print (data)
print(len(data))

addrecord(int(input("Enter number of elemnts to add in the new record: ")))

print (f"\nExpected outcome in csv: {data}\n") #havent used write module

'''






