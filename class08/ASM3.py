nList = [[],[],[]]
oddList = [[],[],[]]
evenList = [[],[],[]]

#This program only works for 3 Lists inside of a list

nEle1 = int(input("Enter number of elements for List_1 of the list: "))
for i in range (nEle1):
    nList[0].append(float(input(f"Enter element #{i} for List_1 of the list: ")))
print()
nEle2 = int(input("Enter number of elements for List_2 of the list: "))
for j in range (nEle2):
    nList[1].append(float(input(f"Enter element #{j} for List_2 of the list: ")))
print()
nEle3 = int(input("Enter number of elements for List_3 of the list: "))
for k in range (nEle3):
    nList[2].append(float(input(f"Enter element #{k} for List_3 of the list: ")))
    
                       
for x in range (len(nList)):
    for y in range (len(nList[x])):
        if (nList[x][y]) % 2 == 0:
            evenList[x].append(nList[x][y])
        else:
            oddList[x].append(nList[x][y])

print (evenList)
print (oddList)
