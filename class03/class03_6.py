num = input("Enter 3-digit number ")

first_digit = int(int(num) / 100)

if int(first_digit) % 2 == 0:
    print("even")
else:
    print("odd")
