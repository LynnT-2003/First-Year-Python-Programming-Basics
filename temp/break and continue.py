countL = 0
nLine = 10
print("There is an example")
while countL < 10:
    countL += 1
    if countL %3 == 0:
        continue
    
#Replace continue with break and see what happens

    print("statement #" + str(countL))
print("Last statement")
