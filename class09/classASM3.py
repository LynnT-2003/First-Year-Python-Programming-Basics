def FindSumAvg(list_x):
    total = 0
    average = 0
    for each in list_x:
        total += each
    average = total / (len(list_x))
    return total,average


list_x = []
Ulist = (input("Enter integers: ").split())
for num in Ulist:
    num = int(num)
    list_x.append(num)

summation,avg = FindSumAvg(list_x)
print(f"The summation is {summation}!\nThe average is {avg}!")
