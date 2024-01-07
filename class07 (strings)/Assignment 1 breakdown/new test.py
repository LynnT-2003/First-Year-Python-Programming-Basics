UInput = input("Enter words: ")
Slength = len(UInput)
Slength = int(Slength)
tempList1 = []
tempList2 = []
conditon = False
n = 0
c = 0
v = 0

for loop in range (Slength):

    for i in range (Slength):
        if UInput[i] != " ":
            tempList1.append(UInput[i])
            v += 1
        else:
            break

    for j in range (Slength-1, 0-1, -1):
        if UInput[j] != " ":
            tempList2.append(UInput[j])
            v += 1
        else:
            break

    for counter in range (0,2):
        if tempList1[counter] == tempList2[counter]:
            condition = True
        else:
            condition = False

    print(v)

    
    if condition == True:
        c = c + 1
        c = int(c)

print(c)
