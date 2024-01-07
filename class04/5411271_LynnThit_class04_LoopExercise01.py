sum = 0
c = 0

while True:
    number = int(input("Enter a positive integer (to terminate enter a negative number): "))
    if number>=0:
        sum = sum + number
        c = c + 1
    else:
        print ("The total of positive number entered is " + str(c))
        print ("The sum of all positive integer(s) is " + str(sum))
        break
    
