nList = [[2,5,99,99],[-3,8,1,2,10],[1, 7,100,10],[1,4]]
oddList = []
evenList = []

def OddEvenList(nList):                      
    for x in range (len(nList)):
        oddList.append([])
        evenList.append([])
        for y in range (len(nList[x])):
            if (nList[x][y]) % 2 == 0:
                evenList[x].append(nList[x][y])
            else:
                oddList[x].append(nList[x][y])
    return oddList,evenList

oList,eList = (OddEvenList(nList))
print(oList)
print(eList)

