def binarySearchC(key, List):
    List.sort()
    n = len(List)
    leftmost = 0
    rightmost = n-1
    c = 0
    while True:
        middle = (leftmost + rightmost) // 2
        c += 1
        if key == List[middle]:
            print(f"{key} found after {c} loops.")
            return c
            break
        elif key < List[middle]:
            rightmost = middle - 1
        elif key > List[middle]:
            leftmost = middle + 1

        if leftmost > rightmost:
            return 'Not found sir'
        

Ulist = [1,2,3,4,5,6,7]

binarySearchC(4,Ulist)
