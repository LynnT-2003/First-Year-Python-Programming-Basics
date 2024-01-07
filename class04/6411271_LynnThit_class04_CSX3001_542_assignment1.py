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
    num = int(input("Please enter the same exact number as before for Number" + str(c-n) + ": "))
    if num > int(big) and num < int(largest):
        big = num
        second_largest = num

print("The first highest number is " + str(largest))
print("The first highest number is " + str(second_largest))

#i think it is impossible/inefficient without using arrays

















