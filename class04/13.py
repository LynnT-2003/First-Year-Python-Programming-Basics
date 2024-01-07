uInput = int(input("n: "))
n = uInput
for x in range(n):
    for i in range(n-x):
        print (" ", end="")
    for i in range(x):
        print ("*",end="")
    for i in range(x+1):
        print ("*", end="")
    print ()      
