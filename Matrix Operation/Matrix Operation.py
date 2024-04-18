def matrix_penjumlahan():
    A = [
        [4,7],
        [5,8]
    ]

    B = [
        [9,3],
        [6,3]
    ]

    C = [
        [0,0],
        [0,0]
    ]

    for i in range(2):
        for j in range(2):
            C[i][j] = A[i][j] + B[i][j]

    print("Hasil Penjumlahan matriks: ")
    for row in C:
        print(row)

def pengurangan_matrix():
    A = [
        [4, 7],
        [5, 8]
    ]

    B = [
        [9, 3],
        [6, 3]
    ]

    C = [
        [0, 0],
        [0, 0]
    ]

    for i in range(2):
        for j in range(2):
            C[i][j] = A[i][j] - B[i][j]

    print("Hasil Pengurangan Matriks")
    for row in C:
        print(row)

def perkalian_matrix():
    A = [
        [1, 2],
        [3, 4]
    ]

    B = [
        [5, 6],
        [7, 8]
    ]

    C = [
        [0, 0],
        [0, 0]
    ]

    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i][j] += A[i][k] * B[k][j]

    print("Hasil perkalian matriks")
    for row in C:
        print(row)

while True:
    print("==============================")
    print("Operasi Matriks")
    print("1. Penjumalahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Exit")
    print("==============================")
    pilih = int(input("Masukkan Pilihan (1-4) : "))
    if pilih == 1:
        matrix_penjumlahan()
    elif pilih == 2:
        pengurangan_matrix()
    elif pilih == 3:
        perkalian_matrix()
    elif pilih == 4:
        break