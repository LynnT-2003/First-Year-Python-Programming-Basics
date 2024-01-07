def MoDuplicate(int_list):
    newli= []
    seen = set()
    for item in int_list:
        if item not in seen:
            seen.add(item)
            newli.append(item)
        elif item in seen:
            if item%2 == 0:
                newitem = item * 20
            else:
                newitem = item * 10
            newli.append(newitem)
    print(li)
    return newli
li = [1,1,3,5,4,5,4,9,4,8,6]
print(li)
li = MoDuplicate(li)
print(li)
