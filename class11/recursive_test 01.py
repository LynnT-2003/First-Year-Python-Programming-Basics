def printHarry(n):
    output = ''
    if n != 0:
        print ('Harry')
        printHarry(n-1)

UInput = int(input("Enter number of times to print out string: "))
printHarry(UInput)
