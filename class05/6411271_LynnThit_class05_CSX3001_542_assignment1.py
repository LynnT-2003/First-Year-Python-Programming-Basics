n = 0
rem = 0
div = 0

print()
print("a) 1st expected output (only even numbers): ")
print()

for i in range(1,10):
    for j in range(1,10):
        if (i*j)%2 == 0:
           print('%2d' % (i*j), end = " ")
        else:
            print("-- ", end = "")
    print ()

print ()
print()
print("b) 2nd expected output(only even numbers and both digits must be even numbers):")
print()

for i in range(1,10):
    for j in range(1,10):
        if (i*j)%2 == 0:
            rem = int((i*j))%10
            div = int((i*j))/10
            rem = int(rem)
            div = int(div)
            if rem%2 == 0 and div%2 == 0:
                print('%2d' % (i*j), end = " ")
            else:
                print("-- ", end = "")
        else:
            print("-- ", end = "")
    print ()
