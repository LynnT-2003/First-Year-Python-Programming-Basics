#matrix 1
matrix1 = []
matrix1row = int(input("Enter number of rows for matrix1: "))
matrix1col = int(input("Enter number of columns for matrix1: "))
for i in range (matrix1row):
    matrix1.append([])
    for j in range (matrix1col):
        matrix1[i].append(int(input(f"Enter a number for Row{i} Column{j} for Matrix1: ")))

#matrix 2
matrix2 = []
matrix2row = int(input("Enter number of rows for matrix2: "))
matrix2col = int(input("Enter number of columns for matrix2: "))
for i in range (matrix2row):
    matrix2.append([])
    for j in range (matrix2col):
        matrix2[i].append(int(input(f"Enter a number for Row{i} Column {j} for Matrix2: ")))

print()
print (f"Matrix 1 = {matrix1}")
print (f"Matrix 2 = {matrix2}")

mat1row = len(matrix1)
mat1col = len(matrix1[0])
mat2row = len(matrix2)
mat2col = len(matrix2[0])

result = []

print(f"\nOutput matrix will be in the format: ")
for i in range (mat1row):
    result.append([])
    for j in range (mat2col):
        result[i].append(0)
print (result)
print ()

if mat1col == mat2row:
    for i in range (mat1row):
        for j in range (mat2col):
            for k in range (mat2row):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    print (result)
else:
    print("Sorry, matrices cannot be multiplied.")






                
