UInput = input("Enter a string: ")

upper = 0
lower = 0
space = 0

outstr = ''

print()

for character in UInput:
    if character.isupper():
        upper += 1
    elif character.islower():
        lower += 1
    elif character == " ":
        space += 1

print(str(upper) + " Uppercase")
print(str(lower) + " Lowercase")
print(str(space) + " Spaces")

for character in UInput:
    if character.isupper():
        outstr += character.lower()
    elif character.islower():
        outstr += character.upper()
    else:
        outstr += character
print (outstr)
