List = [10, 20, 10, 30,]
List2 = []

for each in range(len(List)):
    List2.append(List[each])
List2.append(0)


for x in range(len(List)):
    for y in range(1, len(List2)):
        if List[x] == List2[y]:
            del List[x]

print (List2)
    
