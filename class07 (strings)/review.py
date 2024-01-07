#Clonging list

FirstList = [10, 20, 30]
SecondList = []

for each in FirstList:
    SecondList.append(each)
    
SecondList[2] += 5
FirstList.append(40)
SecondList.append(45)

print (FirstList)
print (SecondList)


print (FirstList)
print (SecondList)
