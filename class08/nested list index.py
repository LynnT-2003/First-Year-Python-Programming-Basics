exList = []
exList.append([0,2,4,6])
print(exList)
exList.append([8,10,12])
print(exList)

for i in range(len(exList)):
    for j in range(len(exList[i])):
        print(exList[i][j], end = ' ')

#Difference between len(exList) and len(exList[i])
#len(exList) is the number of elements(lists) in exList
#len(exList[i]) is the number of elements in list #n, in exList
