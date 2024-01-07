ls = [1,8,2,10,5,7]

n = len(ls)
for i in range(n):
    for j in range(n-i-1):
        if ls[j] > ls[j+1]:
            ls[j],ls[j+1] = ls[j+1],ls[j]

print(ls)

for i in range(len(ls)):
    for j in range(i+1,len(ls)):
        if ls[j] > ls[i]:
            ls[i],ls[j] = ls[j],ls[i]
print(ls)


