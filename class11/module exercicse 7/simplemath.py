def fac(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fac(n-1)

def avglist(numlist):
    total = 0
    for each in numlist:
        total += each
    return total / len(numlist)

def sumofoddpos(numlist):
    if len(numlist) == 0:
        return 0
    else:
        return numlist[0] + sumofoddpos(numlist[2:])

def sumofevenpos(numlist):
    if len(numlist) == 0:
        return 0
    else:
        return numlist[1] + sumofevenpos(numlist[2:])

'''lst = [1,2,3,4,2,1]
print (sumofoddpos(lst))
print (sumofevenpos(lst))
print (fac(4))
print (avglist(lst))'''
