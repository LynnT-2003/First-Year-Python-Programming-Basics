List1 = []
List2 = []
condition = False

nEle1 = int(input("Enter number of elements in List1: "))
for a in range (nEle1):
    List1.append(int(input(f"Enter integer element #{a+1} for List1: ")))

nEle2 = int(input("Enter number of elements in List2: "))
for b in range (nEle2):
    List2.append(int(input(f"Enter integer element #{b+1} for List2: ")))

for each in List1:
    if each in List2:
        condition = True
    else:
        condition = False
        break

if condition == True:
    print("Yes, List#1 is a subset of List#2!")
else:
    print("No, List#1 is not a subset of List#2!")
