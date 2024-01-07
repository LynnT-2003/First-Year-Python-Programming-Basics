List1 = []
List2 = []
Lst = []

nEle1 = int(input("Enter number of elements for List1: "))
for a in range (nEle1):
    List1.append(int(input(f"Enter integer element #{a} for List1: ")))

nEle2 = int(input("Enter number of elements for List2: "))
for b in range (nEle2):
    List2.append(int(input(f"Enter integer element #{b} for List2: ")))

Lst.append(List1)
Lst.append(List2)
print(f"\nNested List ==> {Lst}")

print("\nOutput #1")

for i in range (len(Lst[0])):
    for j in range (len(Lst[1])):
        if Lst[0][i] * Lst[1][j] < 100:
            print (Lst[0][i] * Lst[1][j], end = "\t")
        else:
            print ('***', end = "\t")
    print()

print("\nOutput #1")


for i in range (len(Lst[1])):
    for j in range (len(Lst[0])):
        if Lst[1][i] * Lst[0][j] < 100:
            print (Lst[1][i] * Lst[0][j], end = "\t")
        else:
            print ('***', end = "\t")
    print()
