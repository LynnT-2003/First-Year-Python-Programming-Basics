nList= [[1,2,3],[4,5,6],[7,8,9]]

#print the whole nList
print(nList)

#print each list inside nList 1
for eachL in nList:
    print(eachL, end = '')

print()

#print each list inside nList 2
for i in range(len(nList)):
    print(nList[i], end = '')
print()

#test
print(nList[1])
print(nList[2][1])

nList[2][1] += 2

print(nList[2][1])
print(nList[2])

