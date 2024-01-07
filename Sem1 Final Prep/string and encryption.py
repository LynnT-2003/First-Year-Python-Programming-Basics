def splitEx(uinput):
    count= 0
    list1 = uinput.split()
    for each in list1:
        if len(each) > 4 and ((each[0] == each[-1] and each [1] == each[-2])or(each[0] == each[-2] and each [1] == each[-1])):
            count += 1
    print(f"The number of words that meets the requirements is {count}.")

def concatenate(uinput,n):
    lst = uinput.split()
    output = ''
    for each in lst:
        for i in range (1,n+1):
            if i % 2 == 0:
                output += each.upper() + str(i) + ' '
            else:
                output += each.lower() + str(i) + ' '
    print(output)

def moveR(letter,shift):
    outstr = ''
    for each in letter:
        if each.islower(): #if the string is a lowercase alphabet
            outstr += lowerR(each,shift)
        elif each.isupper(): #if the string is an uppercase alphabet
            outstr += upperR(each,shift)
        elif each == ' ': #if the character is a space
            outstr += ' '
        else: #if the character is not an alphabet 
            outstr += each
    return outstr

def lowerR(LRstring,LRshift):
    LRoutstr = ''
    for LRletter in LRstring:
        Ascii_lowerR = ord(LRletter)
        if Ascii_lowerR + LRshift > 122:
            Ascii_lowerR = abs(122-(Ascii_lowerR+LRshift))+96
            LRoutstr += chr(Ascii_lowerR)
        else:
            LRoutstr += chr(Ascii_lowerR + LRshift)
    return LRoutstr

def upperR(URstring,URshift):
    URoutstr = ''
    for URletter in URstring:
        URAscii_ = ord(URletter)
        if URAscii_+URshift > 90: #re-loop if out of range for upper case alphabets
            URAscii_ = abs(90-(URAscii_+URshift))+64
            URoutstr += chr(URAscii_)
        else:
            URoutstr += chr(URAscii_+URshift)
    return URoutstr

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


'''UInput = input("Enter words or a sentence: ")
splitEx(UInput)

concatenate(input("Enter words: "),int(input("Enter a value for n: ")))'''
print(moveR('abcdefzABCDEFZ', 3))
