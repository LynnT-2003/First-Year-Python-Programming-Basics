print("Assume that your date of birth is Januray 1st")
UInput = input("Enter your year of birth: ")
age = int(UInput)

for counter in range(2021, age-1, -1):
    print("By December " + str(counter) + ", you are " + str(counter-age+1) + "years old.")
    
