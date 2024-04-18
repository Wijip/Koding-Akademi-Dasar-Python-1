matrix1 = [
    [4,0],
    [2,1],
]

matrix2 = [
    [4,1],
    [7,5],
]

matrix3 =[]

for m in range(0, len(matrix1)):
    for n in range(0, len(matrix2[0])):
        print(matrix1[m][n] + matrix2[m][n], end='')
    print(' ')

print("\npengurangan")
for a in range(0, len(matrix1)):
    for b in range(0, len(matrix2[0])):
        print(matrix1[a][b] - matrix2[a][b], end='')
    print(' ')

print("\nperkalian")
for x in range(0, len(matrix1)):
    row = []
    for y in range(0, len(matrix1[0])):
        total = 0
        for z in range(0, len(matrix1[0])):
            total = total + (matrix1[x][z] * matrix2[z][y])
        row.append(total)
    matrix3.append(row)
for x in range(0, len(matrix3)):
    for y in range(0, len(matrix3[0])):
        print(matrix3[x][y], end=' ')
    print()