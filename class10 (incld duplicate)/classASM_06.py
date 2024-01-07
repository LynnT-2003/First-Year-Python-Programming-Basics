def easyencrypt(letter,shift):
    outstr = ''
    lower_letter = letter.lower()
    for each in lower_letter:
        if each == ' ':
            outstr += ''
        Ascii_ = ord(each)
        if Ascii_+shift > 122:
            Ascii_ = 122-(Ascii_+shift)+96
            outstr += chr(Ascii_+shift)
        else:
            outstr += chr(Ascii_+shift)
    return outstr

def easydecrypt(en_strs,shift):
    outstrD = ''
    lower = en_strs.lower()
    for each in lower:
        Ascii_ = ord(each)
        if Ascii_-shift < 97:
            Ascii_ = abs(97-(Ascii_-shift))+96
            outstrD += chr(Ascii_-shift)
        else:
            outstrD += chr(Ascii_-shift)
    return outstrD

print(easyencrypt('Dragonball is famous in Japan',3))
encrypted = easyencrypt('Dragonball is famous in Japan',3)
print(easydecrypt(encrypted,3))
        
    
