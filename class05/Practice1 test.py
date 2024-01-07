

for x in range(1,13):
    if x < 13:
        print ("\t x = " + str(x), end = "\n")
        print ("x^" + str(x), end = '')
    else:
        print("x^12", end = "\n") 
    for y in range(1,13):
        print (x*y, end = "\t")
    print()
