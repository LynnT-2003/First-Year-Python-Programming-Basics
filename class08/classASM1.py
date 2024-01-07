List_1 = [3,4,5]
List_2 = [3,6,7,4,5]

for each in List_1:
    if each in List_1:
        condition = True
    else:
        condition = False
        break

if condition == True:
    print("Yes")
else:
    print("No")
