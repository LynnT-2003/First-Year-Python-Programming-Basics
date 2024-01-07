n = 1
i = 1
s_even = 0
s_odd = 0

while n > 0 or n < 0:
    n = int(input("Enter number #" + str(i) + ": "))
    i += 1
    if n % 2 == 0:
        s_even += n
    elif n % 2 > 0:
        s_odd += n

print ("The sum of all even numbers is " + str(s_even))
print ("The sum of all odd numbers is " + str(s_odd))

if s_even > s_odd:
    print ("The winner is the sum of all even numbers.")
elif s_odd < s_even:
    print ("The winner is the sum of all even numbers.")
else:
    print ("No winner here. Try again.")


        
    
