List1 = [3,5,7,8,9,0]
List2 = [5,0,0]

n1 = len(List1)
n2 = len(List2)

condition = False

if n2 > n1:
    for each1 in List1:
        if each1 in List2:
            condition = True
        else:
            condition = False
            break
    if condition == True:
        print("Yes List_1 is a subset of List_2.")
    else:
        print("No List_1 is not a subset of List_2.")
elif n1 > n2:
    for each2 in List2:
        if each2 in List1:
            condition = True
        else:
            condition = False
            break
    if condition == True:
        print("Yes List_2 is a subset of List_1.")
    else:
        print("No List_2 is not a subset of List_1.")
elif n1 == n2:
    for c in range (n1):
        if List1[c] in List2:
            condition = True
        else:
            condition = False
    if condition == True:
        print("The two lists are the same.")
    else:
        print("The two lists have the same number of elements but are not a subset of each other")
            
    


