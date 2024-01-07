word=list((input("Enter Words: ").split()))
n=int(input('Enter number: '))

for c in word:
    for i in range(1, 5n+1):
        print (c[0].upper() + str(i),end = ' ')
