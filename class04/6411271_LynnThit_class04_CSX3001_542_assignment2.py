n = int(input("Enter number: "))
print ("Output number: ",end="")

while n > 0.9:
    div = n / 10
    div = int(div)
    rem = n % 10
    rem = int(rem)
    n = div
    print (rem,end="")
