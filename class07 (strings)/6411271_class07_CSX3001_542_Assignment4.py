lst=list((input("Enter Words: ").split()))
n=int(input('Enter number: '))

for c in lst:
    for i in range(1,n+1):
        if i%2 == 0:
            print (c[0].upper()+str(i),end=' ')
        else:
            print (c[0].lower()+str(i),end=' ')
