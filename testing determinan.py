matrix1 = [
    [4,5],
    [2,6]
]
matrix2 = [
    [1,2],
    [3,4]
]

determinan1 = matrix1[0][0] * matrix1[1][1] - matrix1[0][1] * matrix1[1][0]
determinan2 = matrix2[0][0] * matrix2[1][1] - matrix2[0][1] * matrix2[1][0]

print(determinan1)
print(determinan2)


# 4 * 6 - 5 * 2 = 24 - 10 = 14