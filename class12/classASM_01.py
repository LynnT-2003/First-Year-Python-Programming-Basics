Ulist = [1,2,3,4,5,6,3,4,5,6]

oddList = []
def NumOdd(list):
    if len(list) == 1:
        if list[0]%2 != 0:
            oddList.append(list[0])
            print(len(oddList))
        else:
            print(len(oddList))
    else:
        if list[0]%2 != 0:
            oddList.append(list[0])
            NumOdd(list[1:])
        else:
            NumOdd(list[1:])
    
NumOdd(Ulist)
