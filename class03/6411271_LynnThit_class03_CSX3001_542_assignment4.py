shopping = input("Enter shopping: ")
hours = input ("Enter hours: ")
minutes = input ("Enter minutes: ")

shopping = int(shopping)
hours = int(hours)
minutes = int(minutes)

if shopping >= 500 and shopping<1500:
    payhours = hours - 2
    payhours = int(payhours)
    payminutes = payhours * 60 + minutes
    num = payminutes / 30
    if payminutes % 30 > 0:
        num = num + 1
        num = int(num)
    else:
        num = num
        num = int(num)
    fees = num*30
    print ("The parking fee for the first 2 hours is free. You have to pay " + str(fees) + " baht for the parking fee.")
elif shopping < 500:
    payhours = hours - 1
    payhours = int(payhours)
    payminutes = payhours * 60 + minutes
    num = payminutes / 30
    if payminutes % 30 > 0:
        num = num + 1
        num = int(num)
    else:
        num = num
        num = int(num)
    fees = num*30
    print ("The parking fee for the first 1 hour is free. You have to pay " + str(fees) + " baht for the parking fee.")
elif shopping >= 1500:
    print ("The parking fee is 120 baht.")

