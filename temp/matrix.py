mat1=[]
mat2=[]
def matrixinput(matrix):
    
    row=int(input('Enter rows:'))
    col=int(input('Enter column:'))
    matrix =[]
    column=[]
    print(row,col)

    matrix= []
    for i in range(0,row):
        matrix.append([])
        for j in range(0,col):
            matrix[i].append('-')
    print(matrix)

    for i in range (0,row):
        for j in range (0,col):
            print ('Enter number for row: ',i+1,'and column: ',j+1)
            matrix[i][j] = int(input())
            print(matrix)
    return matrix

mat1=matrixinput(mat1)
mat2=matrixinput(mat2)

print ('First matrix',mat1)
print ('Second matrix',mat2)

mat1row=len(mat1)
mat1col=len(mat1[0])
mat2row=len(mat2)
mat2col=len(mat2[0])
print('Creat an output matrix.')
result = []
for i in range(0,mat1row):
    result.append([])
    for j in range(0,mat2col):
        result[i].append(0)
    print(result[i])

    
def matrixMultiplication(x,y):
    for i in range(len(x)):
        for j in range(len(y[0])):
            for k in range(len(y)):
                result[i][j] += x[i][k] * y[k][j]
    return result
   
print('Result')
if mat1col == mat2row:
    result=matrixMultiplication(mat1,mat2)
    for r in result:
        print(r)
else:
    print('Sorry. Matrices cannot be multiplied')
