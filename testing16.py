def determinan_a():
    det = 0
    if s == 1:
        print("\nHasil determinan dari matriks A adalah ", a[i][j])
    elif s == 2:
        det = a[0][0] * a[1][1] - a[0][1] * a[1][0]
        print("\nHasil determinan dari matriks A adalah ", det)
    elif s == 3:
        det = a[0][0] * a[1][1] * a[2][2] \
              + a[0][1] * a[1][2] * a[2][0] \
              + a[0][2] * a[1][0] * a[2][1] \
              - a[2][0] * a[1][1] * a[0][2] \
              - a[2][1] * a[1][2] * a[0][0] \
              - a[2][2] * a[1][0] * a[0][1]
        print("\nHasil determinan dari matriks A adalah ", det)


# =======================================================
def determinan_b():
    det = 0
    if s == 1:
        print("\nHasil determinan dari matriks B adalah ", b[i][j])
    elif s == 2:
        det = b[0][0] * b[1][1] - b[0][1] * b[1][0]
        print("\nHasil determinan dari matriks B adalah ", det)
    elif s == 3:
        det = b[0][0] * b[1][1] * b[2][2] \
              + b[0][1] * b[1][2] * b[2][0] \
              + b[0][2] * b[1][0] * b[2][1] \
              - b[2][0] * b[1][1] * b[0][2] \
              - b[2][1] * b[1][2] * b[0][0] \
              - b[2][2] * b[1][0] * b[0][1]
        print("\nHasil determinan dari matriks B adalah ", det)


s = int(input("Masukkan Ordo: "))  # s =  ordo
a = [x[:] for x in [[0] * s] * s]  # a = matriks A
b = [x[:] for x in [[0] * s] * s]  # b = matriks B

print("\nMasukkan", s * s, "Elemen dalam Matriks\n")

# INPUTAN ELEMEN

print("================== Matriks A ==================")
for i in range(0, s):
    for j in range(0, s):
        print("Elemen ke", [i + 1], [j + 1], ":")
        a[i][j] = int(input())

print("\nMatrik A")
for i in range(0, s):
    print("|\t", end='')
    for j in range(0, s):
        print(a[i][j], end='\t')
    print("|")

print()

print("================== Matriks B ==================")
for i in range(0, s):
    for j in range(0, s):
        print("Elemen ke", [i + 1], [j + 1], ":")
        b[i][j] = int(input())

print("\nMatriks B")
for i in range(0, s):
    print("|\t", end='')
    for j in range(s):
        print(b[i][j], end='\t')
    print("|")
print()
while True:
    try:
        pilihan1 = input("Matrix apa yang dihitung?[A/B] = ")
    except ValueError:
        continue
    if pilihan1 == "A":
        break
    elif pilihan1 == "B":
        break
    else:
        print("Pilihan Salah")
        continue
if pilihan1 == "A":
    determinan_a()
elif pilihan1 == "B":
    determinan_b()
else:
    print("Pilihan Salah")