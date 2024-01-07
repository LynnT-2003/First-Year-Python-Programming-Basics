numberA = [1, 52,36, 25, 8, -12]
numberB = [3, -54, 232, 4, 76, 340]
minimum = 9999

for i in range(len(numberA)):
    firstOp = numberA[i]
    for h in range (i+1, len(numberA)):
        difference = firstOp - numberA[h]
        if abs(difference) < minimum:
            minimum = abs(difference)
    for j in numberB:
        difference = firstOp - j
        if abs(difference) < minimum:
            minimum = abs(difference)

for a in range(len(numberB)):
    firstOp = numberB[a]
    for b in range (a+1, len(numberB)):
        difference = firstOp - numberB[b]
        if abs(difference) < minimum:
            minimum = abs(difference)
    for c in numberA:
        difference = firstOp - c
        if abs(difference) < minimum:
            minimum = abs(difference)            

print ("The lowest different between two numbers is " + str(minimum))
