def easyencrypt(letter,shift):
    outstr = ''
    lower_letter = letter.lower()
    for each in lower_letter:
        Ascii_ = ord(each)
        if Ascii_+shift > 122:
            Ascii_ = 122-(Ascii_+shift)+96
            outstr += chr(Ascii_+shift)
        else:
            outstr += chr(Ascii_+shift)
    return outstr

LETTER = (input("Enter message: "))
SHIFT = int(input("Enter number you want to shift by: "))
print (easyencrypt(LETTER,SHIFT)) 
        
