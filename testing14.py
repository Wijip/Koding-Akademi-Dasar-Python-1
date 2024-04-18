matriks1 = [
    [2, 1],
    [2, 3],
]
matriks2 = [
    [1, 1],
    [4, 3],
]

matriks3 = []

for x in range(0, len(matriks1)):
    row = []
    for y in range(0, len(matriks1[0])):
        total = 0
        for z in range(0, len(matriks1)):
            total = total + (matriks1[x][z] * matriks2[z][y])
        row.append(total)
    matriks3.append(row)

for x in range(0, len(matriks3)):
    for y in range(0, len(matriks3[0])):
        print (matriks3[x][y], end=' ')
    print ()