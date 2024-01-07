'''
for i in range(mat1row):
    for j in range(mat2col):
        for k in range (mat2row):
            output[i][j] = matrix1[i][k] * matrix2[k][j]
'''

#creating function to input matrix
def matrixinput(row,col):
    output = []
    for i in range (row):
        output.append([])
        for j in range (col):
            output[i].append(int(input(f"Enter a number for Row{i} Column{j} for Matrix1: ")))
    return output

#using input matrix function
mat1row = int(input("Enter number of rows for matrix1: "))
mat1col = int(input("Enter number of columns for matrix1: "))            
matrix1 = matrixinput(mat1row, mat1col)
print()
mat2row = int(input("Enter number of rows for matrix1: "))
mat2col = int(input("Enter number of columns for matrix1: "))
matrix2 = matrixinput(mat2row, mat2col)

#display two matrices
print()
print (f"Matrix 1 = {matrix1}")
print (f"Matrix 2 = {matrix2}")
print()

def matrixMultiplication(mat1, mat2):
    for i in range (mat1row):
        for j in range (mat2col):
            for k in range (mat2row):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

if mat1col == mat2row:
    #display output matrix rows and columns
    result = []
    for i in range (mat1row):
        result.append([])
        for j in range (mat2col):
            result[i].append(0)
    print("Output will be in the format: ")
    print(result)
    print()
    #display multiplied matrix
    res = matrixMultiplication(matrix1, matrix2)
    print (res)
else:
    print("Sorry, matrices cannot be multiplied.")
