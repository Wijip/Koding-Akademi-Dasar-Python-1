# Matriks input
matrix = [[4, 5], [2, 6]]

# Mencari determinan matriks
det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

# Mengecek apakah matriks memiliki invers
if det == 0:
    print("Matriks tidak memiliki invers")
else:
    # Mencari matriks kofaktor
    cofactor_matrix = [[matrix[1][1], -matrix[0][1]], [-matrix[1][0], matrix[0][0]]]

    # Mencari matriks adjoin
    adjoint_matrix = [[cofactor_matrix[0][0], cofactor_matrix[1][0]], [cofactor_matrix[0][1], cofactor_matrix[1][1]]]

    # Mencari matriks invers
    inverse_matrix = [[adjoint_matrix[0][0] / det, adjoint_matrix[0][1] / det],
                      [adjoint_matrix[1][0] / det, adjoint_matrix[1][1] / det]]

    # Output matriks invers
    print("Matriks invers: ")
    for row in inverse_matrix:
        print(row)
