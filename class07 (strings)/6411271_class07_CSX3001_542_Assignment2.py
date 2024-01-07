str_list=list((input("Enter Words:").split()))
n=len(str_list)
count=0
output=''
lst = []

for i in range(n):
    lst.append(str_list[i])
    for j in range(i+1, n, 1):
        if str_list[j] == str_list[i]:
            del str_list[i]

print(lst)

for each in lst:
    output += each

#I cannot do this program correctly.
#Sometimes it says IndexError: list index out of range.
#Sometimes it doesn't.
