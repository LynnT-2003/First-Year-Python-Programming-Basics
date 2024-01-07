#2x2 martix
matrixA = [[1,3],[5,7]]

#3x3 matrix
matrixB= [[0.5,1.6,7.9],[2.2,4.0,5.6],[3.5,9.8,2.9]]

nRowB = len(matrixB)
nColumnB = len(matrixB[0])

for row in range (nRowB):
    for col in range (nColumnB):
        print(matrixB[row][col], end=' ')
    print()
