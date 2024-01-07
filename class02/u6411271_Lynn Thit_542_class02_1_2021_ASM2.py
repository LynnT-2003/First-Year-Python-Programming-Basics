num = input("Enter 3-digit number ")

while int(num) > 999:
    num = input("Please re-enter a 3-digit number ")
    if int(num) < 999:
        break

first_remainder = int(num)%100

first_num = int(first_remainder)%10
second_num = int(first_remainder)/10
last_num = int(num)/100

first = int(first_num)
second = int(second_num)
last = int(last_num)

sum = first + second + last

print (str(first) + str(second) + str(last))
print ("The sum value is " + str(sum))







