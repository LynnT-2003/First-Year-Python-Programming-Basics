def factorial(n):
    output = 1
    if n == 0 or n == 1:
        return output
    for i in range (2, n+1):
        output = output * i
    return output

def combination(n,r):
    N = factorial(n)
    R = factorial(r)
    NR = factorial(n-r)
    return N/(R*NR)

result = combination(9,3)
print (result)

        
