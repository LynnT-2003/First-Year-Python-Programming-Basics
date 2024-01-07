for n in range (1,13):
    print ("\tx*" + str(n), end = "")

print ("\n")

for i in range (1, 13):
    print ("x = " + str(i), end = "\t")
    for j in range (1,13):
        print (i * j, end ="\t")
    print ("\n")
