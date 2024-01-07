NumList = [1, 4.9, 4, "Five", 6, 7, "Eight", 100.2, 15]
intList = []
alphaList = []

for i in range(len(NumList)):
    if str(NumList[i]).isdigit():
        intList.append(NumList[i])
    elif str(NumList[i]).isalpha():
        alphaList.append(NumList[i])

print (intList)
print (alphaList)
        
