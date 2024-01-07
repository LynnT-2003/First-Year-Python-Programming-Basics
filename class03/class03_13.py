age = input("Please enter your age ")
age = int(age)

if age < 2:
    print("baby")
elif age <= 4 and age > 2:
    print("toddler")
elif age > 4 and age <= 13:
    print("kid")
elif age >13 and age <=20:
    print("teen")
elif age > 20 and age <= 64:
    print ("adult")
else:
    print ("elder")
