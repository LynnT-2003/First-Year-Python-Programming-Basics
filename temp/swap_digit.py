integer = input("Enter a 3 digit number ")

integer = int(integer)
last_digit = int(integer % 10)

integer = int(integer - last_digit)
integer = int(integer / 10)
second_digit = int(integer % 10)

integer = int(integer - second_digit)
integer = int(integer /10)
first_digit = int(integer)

total = int(first_digit + second_digit + last_digit)

print (str(last_digit))
print (str(second_digit))
print (str(first_digit))

print("The new number is " + str(last_digit) + str(second_digit) + str(first_digit))

print("The sum of the numbers is " + str(total))

