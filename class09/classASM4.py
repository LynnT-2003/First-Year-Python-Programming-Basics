def MergeAndSort(list1, list2):
    nList = []
    for each1 in list1:
        nList.append(each1)
    for each2 in list2:
        nList.append(each2)
    nList.sort(reverse = True)
    return nList


list1 = [6,4,1,1]
list2 = [9,7,3]
output = (MergeAndSort(list1, list2))
print(output)
