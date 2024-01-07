
UInput = str(input("Enter a message: "))
print()
outstr = ''
for character in UInput:
    if character.isupper():
        if character == " ":
            outstr += " "
        else:
            Ascii_ = ord(character)
            if Ascii_+3 > 90:
                Ascii_ = (Ascii_+3-90)+64
                outstr += chr(Ascii_)
            else:
                outstr += chr(Ascii_+3)
    else:
        outstr += character
print (outstr)



