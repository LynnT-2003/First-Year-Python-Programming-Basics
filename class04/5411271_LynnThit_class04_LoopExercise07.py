s = 0

n = int(input("Input number: "))

while (n != 0): 
     s = s + (n % 10)
     n = n//10

print ("The sum of each digit is " + str(s))

