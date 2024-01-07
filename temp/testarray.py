largest = 0
smallest = 99999999999999999
second_largest = 0
second_smallest = 0
big = 0
small = 99999999999999999

c = 0

n = int(input("Enter number of real numbers: "))


while c < n:
    c += 1
    num = int(input("Number" + str(c) + ": "))
    if num > int(largest):
        largest = num

while c < n + n:
    c += 1
    num = int(input("Enter the same exact number as before for Number" + str(c-n) + " because I dont know how to use arrays in Python: "))
    if num > int(big) and num < int(largest):
        big = num
        second_largest = num

print(largest)
print(second_largest)

