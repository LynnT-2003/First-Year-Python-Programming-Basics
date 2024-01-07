UInput = str(input("Enter a sentence: "))

for character in UInput:
    if character.isalpha():
        print(character, end='')
    if character == " ":
        print(' ', end="")
    else:
        print('', end="")
