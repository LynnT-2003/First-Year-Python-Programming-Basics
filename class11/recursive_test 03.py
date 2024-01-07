def toDigit(n):
    List = []
    for each in str(n):
        List.append(int(each))
    return List

def sumdigits(L):
    if len(L) == 0:
        return 0
    else:
        if L[0] > 0:
            return int(L[0]) + sumdigits(L[1:])
        else:
            return sumdigits(L[1:])

print (toDigit(3456))
print (sumdigits(toDigit(345)))

'''
#Test 2

def sumdigits(L):
    if
'''
