F = input ("Enter Fahrenheit: ")

F = float(F)

K = ((F-32)*5/9) + 273.15

if K < 280:
    print ("Too cold to live")
else:
    print ("The temperature is " + str(K) + " Kelvin")
