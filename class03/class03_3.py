first_num = input ("Enter first number ")
second_num = input ("Enter second number ")
last_num = input ("Enter third number ")

first_num = int(first_num)
second_num = int(second_num)
last_num = int(last_num)

if first_num > second_num and first_num > last_num:
    largest = first_num
elif second_num > first_num and second_num > last_num:
    largest = second_num
elif last_num > first_num and last_num > second_num:
    largest = last_num
if first_num < second_num and first_num < last_num:
    smallest = first_num
elif second_num < first_num and second_num < last_num:
    smallest = second_num
elif last_num < first_num and last_num < second_num:
    smallest = last_num
if first_num < largest and first_num > smallest:
    mid = first_num
elif second_num < largest and second_num > smallest:
    mid = second_num
elif last_num < largest and last_num > smallest:
    mid = last_num

print (smallest)
print (mid)
print (largest)
