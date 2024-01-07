x1 = input("Enter x1: ")
x2 = input("Enter x2: ")
x3 = input("Enter x3: ")

x1 = int(x1)
x2 = int(x2)
x3 = int(x3)
100
if x1 % x3 == 0:
    if x2 % x3 == 0:
        print ("x3 is a factor of both x1 and x2")
    else:
        print ("x3 is a factor of x1")
elif x2 % x3 == 0:
    if x1 % x3 == 0 :
        print ("x3 is a factor of both x1 and x2")
    else:
        print ("x3 is a factor of x2")
else:
    print ("x3 is neither a factor of x1 nor x2")
