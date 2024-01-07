def bubbleSort(ls):
    for i in range(len(ls)): #also works with range(len(ls)-1)
        for j in range(0,len(ls)-1-i): # -i is included for efficiency
            if ls[j] > ls[j+1]:
                ls[j+1],ls[j] = ls[j],ls[j+1] #largest number will be sent to the last array
    return ls
print(bubbleSort([2,3,1,8,7]))

def binSearch(ls,key):
    ls.sort()
    leftmost = 0
    rightmost = len(ls)-1
    count = 0

    while True:
        middle = round((leftmost + rightmost)/2) #rounds down
        count += 1
        if ls[middle] == key:
            print(count)
            return True
        elif key > ls[middle]:
            leftmost = middle + 1
        elif key < ls[middle]:
            rightmost = middle -1
        if leftmost > rightmost:
            return False
        
list1 = [1,2,5,6,9,11,8]
print(binSearch(list1,2))
        
        
