'''
#METHOD 1
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

#METHOD 2
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
'''
def moveR(letter,shift):
    outstr = ''
    for each in letter:
        if each.islower(): #check if lower case
            Ascii_ = ord(each)
            if Ascii_+shift > 122: #re-loop if out of range for lower case alphabets
                Ascii_ = abs(122-(Ascii_+shift))+96
                outstr += chr(Ascii_)
            else:
                outstr += chr(Ascii_+shift)
        elif each.isupper(): #check if upper case
            Ascii_ = ord(each)
            if Ascii_+shift > 90: #re-loop if out of range for upper case alphabets
                Ascii_ = abs(90-(Ascii_+shift))+64
                outstr += chr(Ascii_)
            else:
                outstr += chr(Ascii_+shift)
        elif each == ' ': #return space if string is space
            outstr += ' '
        else: #return the same character if the string is not an alphabet
            outstr += each
    return outstr
        

def moveL(letter,shift):
    outstr = ''
    for each in letter:
        if each.islower(): #check if lower case
            Ascii_ = ord(each)
            if Ascii_-shift < 97: #re-loop if out of range for lower case alphabets
                Ascii_ = 123-abs(97-(Ascii_-shift)) 
                outstr += chr(Ascii_)
            else:
                outstr += chr(Ascii_-shift)
        elif each.isupper(): #check if upper case
            Ascii_ = ord(each)
            if Ascii_-shift < 65: #re-loop if out of range for upper case alphabets
                Ascii_ = 91-abs(65-(Ascii_-shift)) 
                outstr += chr(Ascii_) 
            else:
                outstr += chr(Ascii_-shift)
        elif each == ' ': #return space if string is space
            outstr += ' '
        else: #return the same character if the string is not an alphabet
            outstr += each
    return outstr

def easyencrypt(letter,shift,direction):
    if direction == 'r':
        return moveR(letter,shift)
    elif direction == 'l':
        return moveL(letter,shift)
    else:
        return 'Error'

def easydecrypt(letter,shift,direction): #same shift and direction used in encrypt
    if direction == 'r':
        return moveL(letter,shift)
    elif direction == 'l':
        return moveR(letter,shift)
    else:
        return 'Error'

message = input('Enter the message you want to encrypt: ')
_shift = int(input('Enter the number you want to shift by: '))
_direction = input("Enter r for right or l for left direction: ")
encrypted = easyencrypt(message,_shift,_direction)
decrypted = easydecrypt(encrypted,_shift,_direction)
print (f"Encrypted message = {encrypted}")
print (f"Decrypted message = {decrypted}")

'''
#test
encrypted = easyencrypt('Dragonball is famous in JapanZ..!!!',3,'r')
decrypted = easydecrypt(encrypted,3,'r')
print (encrypted)
print (decrypted)'''
        
    
