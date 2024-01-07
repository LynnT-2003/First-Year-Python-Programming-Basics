nList = [[2,5,99,99],[-3,8,1,2,10],[1, 7,100,10]]
oddList = [[],[],[],[],[]]
evenList = [[],[],[],[],[]]

#will only work for 5 lists (max) inside nList
#if there are less than 5 lists, empty lists will still be printed as [] in the output.
#for example, in this program:
#there are only 3 lists, the remaining two outputs in even and odd list will be printed out as [...[],[]]

def OddEvenList(nList):                      
    for x in range (len(nList)):
        for y in range (len(nList[x])):
            if (nList[x][y]) % 2 == 0:
                evenList[x].append(nList[x][y])
            else:
                oddList[x].append(nList[x][y])
    return (f"evenList={evenList}\noddList={oddList}")

print (OddEvenList(nList))
