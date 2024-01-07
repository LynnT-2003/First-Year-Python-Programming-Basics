x1 = input ("Enter the first number: ")
x2 = input ("Enter the second number: ")
x3 = input ("Enter the third number: ")
x4 = input ("Enter the fourth number: ")

x1 = int(x1)
x2 = int(x2)
x3 = int(x3)
x4 = int(x4)

total = x1 + x2 + x3 + x4
print ("The sum is " + str(total))

if total > 0:
    if total % 2 == 0:
        print ("The sum is Positive Even.")
    else:
        print ("The sum is Positive Odd.")
elif total < 0:
    if total % 2 == 0:
        print ("The sum is Negative Even.")
    else:
        print ("The sum is Negative Odd.")
else:
    print ("Zero")
