print("Print equilateral triangle Pyramid using asterisk symbol ")
# printing full Triangle pyramid using stars
size = 7
for i in range(0, size):
    for j in range(0, size):
        print(end=" ")
    # decrementing m after each loop
    for j in range(0, i + 1):
        print("* ", end=' ')
    print(" ")
