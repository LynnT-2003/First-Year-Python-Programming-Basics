print ("\t", end="")
for i in range (1,13):
    print ("x *" + str(i) , end="\t")
print ("\n")


for x in range (1, 13):
    print ("x = " + str(x), end = "\t")
    for y in range (1, 13):
        print (x*y, end = "\t")
    print ()
