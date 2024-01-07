print("\t", end="")

for counter in range (1,13):
    print("x^" + str(counter), end = "\t")

print()

for x in range(1,13):
    print ("x = " + str(x), end = "\t")
    for y in range(1,13):
        print (x*y, end = "\t")
    print()
