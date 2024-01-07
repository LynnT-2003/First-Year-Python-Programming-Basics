UInput = input("Enter words: ")
Slength = len(UInput)
Slength = int(Slength)
tempList1 = []
tempList2 = []
conditon = False
n = 0
c = 0


for i in range (Slength):
    tempList1.append(UInput[i])

for j in range (Slength-1, 0-1, -1):
    tempList2.append(UInput[j])

if tempList1[1] == tempList2[1] or tempList1[1] == tempList2[2] or tempList1[2] == tempList2[1] or tempList1[2] == tempList2[2]:
    condition = True

if condition == True:
    print ("Okay!!")
elif condition == False:
    print ("Oh no :(")

                        
            
