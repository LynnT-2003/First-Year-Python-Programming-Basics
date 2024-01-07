myList = [0,1,2]
print(myList)
print()

intList = [1,2,3,5]
for each in intList:
    print (each)
print()

for i in range (len(intList)):
    print (f"at index #{i}", end = " ")
    print (intList[i])


intList[3] = 4
for i in range (len(intList)):
    print (f"at index #{i}", end = " ")
    print (intList[i])
print()


bList = [1,2,3,4,5,6,7,8]
print(bList[2::5])
print(bList[::2])
print(bList[1::2])
print()

cList = [8,9,10,11,12,13,14]
del cList[5]
print(cList)
