def easyencrypt(letter,shift,direction):
    outstr = ''
    if direction == 'r':
        for each in letter:
            if each.islower():
                Ascii_ = ord(each)
                if Ascii_+shift > 122:
                    Ascii_ = abs(122-(Ascii_+shift))+96
                    outstr += chr(Ascii_)
                else:
                    outstr += chr(Ascii_+shift)
            elif each.isupper():
                Ascii_ = ord(each)
                if Ascii_+shift > 90:
                    Ascii_ = abs(90-(Ascii_+shift))+64
                    outstr += chr(Ascii_)
                else:
                    outstr += chr(Ascii_+shift)
            elif each == ' ':
                outstr += ' '
            else:
                outstr += each
        return outstr
    #same as decrypt in direction R
    elif direction == 'l':
        for each in letter:
            if each.islower():
                Ascii_ = ord(each)
                if Ascii_-shift < 97: 
                    Ascii_ = 123-abs(97-(Ascii_-shift)) 
                    outstr += chr(Ascii_) 
                else:
                    outstr += chr(Ascii_-shift)
            elif each.isupper():
                Ascii_ = ord(each)
                if Ascii_-shift < 65:
                    Ascii_ = 91-abs(65-(Ascii_-shift)) 
                    outstr += chr(Ascii_) 
                else:
                    outstr += chr(Ascii_-shift)
            elif each == ' ':
                outstr += ' '
            else:
                outstr += each
        return outstr        

def easydecrypt(en_strs,shift,direction):
    outstr = ''
    if direction == 'r':
        for each in en_strs:
            if each.islower():
                Ascii_ = ord(each)
                if Ascii_-shift < 97: 
                    Ascii_ = 123-abs(97-(Ascii_-shift)) 
                    outstr += chr(Ascii_) 
                else:
                    outstr += chr(Ascii_-shift)
            elif each.isupper():
                Ascii_ = ord(each)
                if Ascii_-shift < 65:
                    Ascii_ = 91-abs(65-(Ascii_-shift)) 
                    outstr += chr(Ascii_) 
                else:
                    outstr += chr(Ascii_-shift)
            elif each == ' ':
                outstr += ' '
            else:
                outstr += each
        return outstr
    #same as encrypt in direction R
    elif direction == 'l':
        for each in en_strs:
            if each.islower():
                Ascii_ = ord(each)
                if Ascii_+shift > 122:
                    Ascii_ = abs(122-(Ascii_+shift))+96
                    outstr += chr(Ascii_)
                else:
                    outstr += chr(Ascii_+shift)
            elif each.isupper():
                Ascii_ = ord(each)
                if Ascii_+shift > 90:
                    Ascii_ = abs(90-(Ascii_+shift))+64
                    outstr += chr(Ascii_)
                else:
                    outstr += chr(Ascii_+shift)
            elif each == ' ':
                outstr += ' '
            else:
                outstr += each
        return outstr
        
encrypted = easyencrypt('Dragonball is famous in JapanZ..!!!',3,'r')
print(easyencrypt('Dragonball is famous in JapanZ..!!!',3,'r'))
print(easydecrypt(encrypted,3,'r'))
        
    
