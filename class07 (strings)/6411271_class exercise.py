Ulist = []
total = 0
multiple = 1
num = 0

while num < 10:
    num = int(input("How many numbers? (Enter at least 10): "))

#user input
for i in range (num):
    elements = float(input(f"Enter number #{i+1}: "))
    Ulist.append(elements)

#finding and printing the sum and multiple of all the numbers 
for each in Ulist:
    total += each
    multiple = multiple * each
print(f"\nThe sum of all the numbers is {total}")
print(f"The multiple of all the numbers is {multiple}")

#finding and printing the smallest and largest number
small = 99999999999999999999
large = -99999999999999999999
for each in Ulist:
    if each > large:
        large = each
    if each < small:
        small = each
print(f"The smallest number is {small}")
print(f"The largest number is {large}")

    
    

