def linearSearch(key,ls):
    for element in ls:
        if element == key:
            return True
        return False

def binarySearch(key,ls):
    ls.sort()
    leftmost = 0
    rightmost = len(ls)-1
    c = 0
    
    while True:
        middle = (leftmost + rightmost) // 2
        c += 1
        if  key == ls[middle]:
            return f"{key} is found in the list\nIt took {c} loops to find {key} inside the list"
        elif key > ls[middle]:
            leftmost = middle + 1
        elif key < ls[middle]:
            rightmost = middle - 1
        elif leftmost > rightmost:
            return f"{key} is not found in the list."
            return False

Ulist = [1,3,3,5,7,9]
Ulist2 = [1,3,7,10,21,23,50]
print(binarySearch(21,Ulist2))
