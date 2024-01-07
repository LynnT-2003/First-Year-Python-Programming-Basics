intList = []
oddList = []
evenList = []

def OnlyOdd(intList):
    for i in range (len(intList)):
        if intList[i] % 2 != 0:
            oddList.append(intList[i])
    return oddList

def OnlyEven(intList):
    for i in range (len(intList)):
        if intList[i] % 2 == 0:
            evenList.append(intList[i])
    return evenList

Ulist = input("Enter integers: ").split()
for each in Ulist:
    each = int(each)
    intList.append(each)

oddcount = 0
evencount = 0
for eachnum in intList:
    if eachnum % 2 == 0:
        evencount += 1
    elif eachnum % 2 != 0:
        oddcount += 1
if oddcount > evencount:
    output = (OnlyOdd(intList))
    print (output)
elif evencount > oddcount:
    output = (OnlyEven(intList))
    print (output)


