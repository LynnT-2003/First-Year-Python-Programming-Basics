string = input("Write a sentence: ")

for character in string:
    if character.isupper():
        print (character.lower(), end="")
    else:
        print (character, end="")
