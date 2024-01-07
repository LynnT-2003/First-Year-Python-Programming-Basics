import math

def fac(n):
    if n <= 1:
        return 1
    else:
        return n*fac(n-1)

def printHarry(n):
    if n == 1:
        print ('Harry')
    else:
        print ('Harry')
        printHarry(n-1)

def listsum(numlist):
    if len(numlist) == 1:
        return numlist[0]
    else:
        return numlist[0] + listsum(numlist[1:])

def digitsum(n):
    r = n%10
    if n < 10:
        return int(n)
    else:
        return int(r)+digitsum(math.floor((n/10)))

def sumpositive(numlist):
    if len(numlist) == 1:
        if numlist[0] > 0:
            return numlist[0]
        else:
            return 0
    else:
        if numlist[0] > 0:
            return numlist[0] + sumpositive(numlist[1:])
        else:
            return sumpositive(numlist[1:])

def sum_series(n):
    if n <= 0:
        return 0
    else:
        return n + sum_series(n-2)

def power(x,y):
    if y < 0:
        return power(x,int(input("Pls enter a postive value for y!\n")))
    if y == 0:
        return 1 
    else:
        return x* power(x,y-1)
        
print(fac(5))
printHarry(6)
print(listsum([1,2,3,4,5,7,-3,-4,-5,-8]))
print(digitsum(1234567))
print(sumpositive([1,2,3,4,56,7,-3,-4,-5,-8]))
print(sum_series(10))
print(power(2,int(input("Enter a value for y: "))))
