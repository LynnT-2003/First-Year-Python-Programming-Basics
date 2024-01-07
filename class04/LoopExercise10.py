n = int(input("n: "))

for k in range(n+1):
    for c in range (n-k):
        print (" ", end="")
    for c in range (2*k-1):
        print ("*", end="")
    print ()

