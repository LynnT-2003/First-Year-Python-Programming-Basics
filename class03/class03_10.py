num = input ("Enter 3-digit number ")

first_num = int(int(num)/100)
second_num = int(int(int(num)%100)/10)
third_num = int(int(int(num)%100)%10)

total = int(first_num) + int(second_num) + int(third_num)

print(first_num)
print(second_num)
print(third_num)
print(total)
