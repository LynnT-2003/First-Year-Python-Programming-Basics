numA = int(input("Enter numA: "))
numB = int(input("Enter numB: "))
sum_ = 0

if numA < numB:
    for each in range (numA, numB+1, 1):
        if each%3!=0 or each%7!=0: 
            
            if sum_  < 5*numB:
                sum_ += each
                print (each, end=" ")
elif numB < numA:
    for each in range (numB, numA+1, 1):
        if each%3!=0 or each%7!=0: 
            
            if sum_  < 5*numA:
                sum_ += each
                print (each, end=" ")
