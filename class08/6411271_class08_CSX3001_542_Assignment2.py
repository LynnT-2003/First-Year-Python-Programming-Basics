List = []
newL = []
total = 0

nEle = int(input("Enter number of elements for List: "))

if nEle != 0:
    for i in range (nEle):
        ele = int(input(f"Enter element {i} for List: "))
        List.append(ele)

    for each in List:
        if each != 13:
            newL.append(each)
        else:
            break

    for each2 in newL:
        total += each2
        
    print(f"The sum is {total}.")

else:
    print(f"The sum is 0.")
