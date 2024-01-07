lst = []
intList = []
strList = []
floatList = []
resultList = []

def sorting(lst):
    for i in range(len(lst)):
        if str(lst[i]).isdigit():
            intList.append(int(lst[i]))
        elif str(lst[i]).isalpha():
            strList.append(lst[i])
        else:
            floatList.append(float(lst[i]))
    resultList.append(intList)
    resultList.append(strList)
    resultList.append(floatList)
    return resultList


nEle = int(input("Enter number of elements for List: "))
for a in range (nEle):
    lst.append(input(f"Enter element #{a+1} for List: "))


print(sorting(lst)[0])
print(sorting(lst)[1])
print(sorting(lst)[2])
        
