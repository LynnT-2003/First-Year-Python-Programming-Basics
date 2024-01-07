def mutablelist(list):
    list.extend([10,100])
    list.append(10)
    print(list)


LIST = [1,2,3]

print (LIST)
mutablelist(LIST)
print (LIST)
