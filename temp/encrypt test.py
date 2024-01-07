UInput = str(input("Enter a message: "))
outstr = ''
for character in UInput:
    if character.isupper():
        if character == " ":
            outstr += " "
        else:
            Ascii_ = ord(character)
            if Ascii_+3 > 90:
                Ascii_ = 90-(Ascii_+3)+64
                outstr += chr(Ascii_+3)
            else:
                outstr += chr(Ascii_+3)
    else:
        outstr += character
print (outstr)


