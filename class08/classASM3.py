List1 = []
List2 = []

nEle1 = int(input("Enter number of elements for List1: "))
for a in range (nEle1):
    List1.append(int(input(f"Enter integer element #{a} for List1: ")))

nEle2 = int(input("Enter number of elements for List2: "))
for b in range (nEle2):
    List2.append(int(input(f"Enter integer element #{b} for List2: ")))

for i in range (len(List1)):
    for j in range (len(List2)):
        if List1[i] * List2[j] < 100:
            print (List1[i] * List2[j], end = "\t")
        else:
            print ('***', end = "\t")
    print()
