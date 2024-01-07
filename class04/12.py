uInput = int(input("n: "))
n = uInput
i = 0
for x in range(n+1):
    for i in range(n-x):
        print (" ", end="")
    for i in range(x):
        print ("*",end="")
    print ()     
