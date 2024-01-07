matrix1 = [[1,2],[1,2],[1,2],[1,2]]
matrix2 = [[1,2,3],[1,2,3]]

mat1row = len(matrix1)
mat1col = len(matrix1[0])
mat2row = len(matrix2)
mat2col = len(matrix2[0])

result = []

print(f"\nOutput matrix will be in the format: ")
for i in range (mat1row):
    result.append([])
    for j in range (mat2col):
        result[i].append('-')
print (result)
print ()

for i in range (len(result)):
    for j in range (len(result[i])):
        result[i][j] = 0

if mat1col == mat2row:
    for i in range (mat1row):
        for j in range (mat2col):
            for k in range (mat2row):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    print (result)
else:
    print("Sorry, matrices cannot be multiplied.")






                
