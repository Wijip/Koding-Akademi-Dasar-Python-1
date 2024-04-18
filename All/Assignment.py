import sys,os
import time,math
def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
def clearScreen():
    os.system("cls")
while True:
    print("==================================================================")
    print("=                          ASSIGNMENT                            =")
    print("==================================================================")
    print("= 1. Variable data types                                         =")
    print("= 2. Input & Output                                              =")
    print("= 3. Operator                                                    =")
    print("= 4. Mathematical function                                       =")
    print("= 5. IF Statement                                                =")
    print("= 6. Looping                                                     =")
    print("= 7. List                                                        =")
    print("= 8. Matrix Operation                                            =")
    print("= 9. Tuples                                                      =")
    print("= 10. Dictionary                                                 =")
    print("= 11. Dictionary Function                                        =")
    print("= 12. Project 1                                                  =")
    print("= 13. Exit                                                       =")
    print("==================================================================")
    pilih = int(input("Pilih Assignment yang akan di jalankan 1-13 \t: "))
    print("==================================================================")
    if pilih == 1:
        print("==================================================================")
        print("=                      VARIABLE DATA TYPE                        =")
        print("==================================================================")
        print("= 1. Assignment 1                                                =")
        print("= 2. Assignment 2                                                =")
        print("==================================================================")
        while True:
            try:
                a1 = int(input("Pilih Assignment yang akan dijalankan \t: "))
            except ValueError:
                continue
            if a1 == 1:
                break
            elif a1 == 2:
                break
            else:
                print("Pilihan Anda tidak ada ..!!")
                continue
        if a1 == 1:
            print("==================================================================")
            print("=                        ASSIGNMENT 1                            =")
            print("==================================================================")
            integer = 10
            float = 0.5
            char = 'K'
            string = "Koding Akademi"
            boolean = True
            kata1 = "Type Integer\t= "
            kata2 = "Type Float\t\t= "
            kata3 = "Type Char\t\t= "
            kata4 = "Type String\t\t= "
            kata5 = "Type Boolean\t= "
            gabung3 = kata3 + char + '\n'
            gabung4 = kata4 + string + '\n'

            print("Type Integer\t\t=",integer)
            print("Type Float\t\t=",float)
            typingPrint(gabung3)
            typingPrint(gabung4)
            print("Type Boolean\t\t=",boolean)

            # print("Type Char\t\t=",char)
            # print("Type String\t\t=",string)

            print("==================================================================")
            time.sleep(2)
            lanjut = input("Tekan enter untuk lanjut")
            print("==================================================================")
        elif a1 == 2:
            print("==================================================================")
            print("=                        ASSIGNMENT 2                            =")
            print("==================================================================")
            print("Konversi Integer to Float")
            num1 = 10
            K1 = float(num1)
            print("Hasil Convert \t: ")
            print("\nKonversi Float to Integer",K1)
            num2 = 3.4
            K2 = int(num2)
            print("Hasil Konveris\t:",K2)
            print("\nKonversi Integer to Hexa")
            num3 = int(input("Masukkan Angka \t:"))
            K3 = hex(num3)
            print("Hasil Konversi",K3)
            print("\nKonversi Integer to String")
            num4 = int(input("Masukkan Angka \t:"))
            K4 = str(num4)
            print("Hasil Konversi",K4)
            print("==================================================================")
            time.sleep(2)
            lanjut = input("Tekan enter untuk lanjut")
            print("==================================================================")
    elif pilih == 2:
        print("==================================================================")
        print("=                        INPUT & OUTPUT                          =")
        print("==================================================================")
        nama = str(input("Masukkan Nama\t= "))
        umur = int(input("Masukkan Umur\t= "))
        almt = str(input("Masukkan Alamat\t= "))
        print("=================================================")
        print("Hallo",nama,"Selamat datang di Koding Akademi\nBerikut Identitas anda:")
        print("\nNama\t=",nama)
        print("Umur\t=",umur)
        print("Alamat\t=",almt)
        print("=================================================")
        time.sleep(2)
        lanjut = input("Tekan enter untuk lanjut")
        print("=================================================")

    elif pilih == 3:
        print("==================================================================")
        print("=                           OPERATOR                             =")
        print("==================================================================")
        print("= 1. Assignment 1                                                =")
        print("= 2. Assignment 2                                                =")
        print("= 3. Assignment 3                                                =")
        print("==================================================================")
        while True:
            try:
                a2 = int(input("Pilih Assignment yang akan dijalankan \t: "))
            except ValueError:
                continue
            if a2 == 1:
                break
            elif a2 == 2:
                break
            elif a2 == 3:
                break
            else:
                print("Pilihan anda tidak ada ..!!")
                continue
        if a2 == 1:
            print("==================================================================")
            print("=                        ASSIGNMENT 1                            =")
            print("==================================================================")
            angka1 = int(input("Masukkan Angka : "))
            for i in range(5):
                time.sleep(1)
                print("=================================================")
                print("Angka Sebelum dilakukan penambahan",angka1)
                angka1 += 1
                print("Angka Sesudah dilakukan penambahan",angka1)
                print("=================================================")
            time.sleep(2)
            lanjut = input("Tekan enter untuk lanjut")
            print("=================================================")
        elif a2 == 2:
            print("==================================================================")
            print("=                        ASSIGNMENT 2                            =")
            print("==================================================================")
            angka2 = int(input("Masukkan Angka : "))
            for angka in range(5):
                time.sleep(1)
                print("=================================================")
                print("Angka sebelum dilakukan pengurangan",angka2)
                angka2 -= 1
                print("Angka Setelah dilakukan pengurangan",angka2)
                print("=================================================")
            time.sleep(2)
            lanjut = input("Tekan enter untuk lanjut")
            print("=================================================")
        elif a2 == 3:
            print("==================================================================")
            print("=                        ASSIGNMENT 3                            =")
            print("==================================================================")
            num1 = int(input("Masukkan Angka 1 : "))
            num2 = int(input("Masukkan Angka 2 : "))
            num3 = int(input("Masukkan Angka 3 : "))
            num4 = int(input("Masukkan Angka 4 : "))

            print("=================================================")
            print("=       PERBANDINGAN ANGKA 1 DAN ANGKA 3        =")
            print("=================================================")
            P1 = num1 > num3

            print("Angka 1 lebih besar dari Angka 3        =",P1)
            P2 = num1 < num3
            print("Angka 1 Lebih Kecil dari Angka 3        =",P2)
            P3 = num1 == num3
            print("Angka 1 Sama dengan Angka 3             =",P3)
            P4 = num1 != num3
            print("Angka 1 Tidak sama dengan Angka 3       =",P4)
            P5 = num1 >= num3
            print("Angka 1 Lebih besar sama dengan Angka 3 =",P5)
            P6 = num1 <= num3
            print("Angka 1 Lebih kecil sama dengan Angka 3 =",P6)
            print("\n=================================================")
            print("=       PERBANDINGAN ANGKA 2 DAN ANGKA 4        =")
            print("=================================================")
            K1 = num2 > num4
            K2 = num2 < num4
            K3 = num2 == num4
            K4 = num2 != num4
            K5 = num2 >= num4
            K6 = num2 <= num4
            print("Angka 2 Lebih besar dari Angka 4        =",K1)
            print("Angka 2 Lebih kecil dari Angka 4        =",K2)
            print("Angka 2 Sama dengan Angka 4             =",K3)
            print("Angka 2 Tidak sama dengan Angka 4       =",K4)
            print("angka 2 Lebih besar sama dengan Angka 4 =",K5)
            print("Angka 2 Lebih kecil sama dengan Angka 4 =",K6)
            print("=================================================")
            time.sleep(2)
            lanjut = input("Tekan enter untuk lanjut")
            print("=================================================")

    elif pilih == 4:
        print("==================================================================")
        print("=                     MATHEMATICAL FUNCTION                      =")
        print("==================================================================")
        print("= 1. Assignment 1                                                =")
        print("= 2. Assignment 2                                                =")
        print("==================================================================")
        while True:
            try:
                aa = int(input("Pilih Assignment yang akan dijalankan \t: "))
            except ValueError:
                continue
            if aa == 1:
                break
            elif aa == 2:
                break
            else:
                print("Invalid")
                continue
        if aa == 1:
            print("==================================================================")
            print("=                        ASSIGNMENT 1                            =")
            print("==================================================================")
            y = int(input("Masukkan Nilai dari Y : "))
            process = (math.sqrt(math.pow(5, 2)) / (y + 1)) + (2 * (math.pow(y, 2)))
            print(round(process, 2))
            input("tekan enter untuk lanjut")
        elif aa == 2:
            print("==================================================================")
            print("=                        ASSIGNMENT 2                            =")
            print("==================================================================")
            a = int(input("Masukkan angka 1 : "))
            b = int(input("Masukkan angka 2 : "))
            c = int(input("Masukkan angka 3 : "))
            d = (b**2) - (4*a*c)

            x1 = (-b + math.sqrt(d)) / (2 * a)
            x2 = (-b - math.sqrt(d)) / (2 * a)

            print('Solusinya adalah {0} dan {1}'.format(x1, x2))
            print("=================================================")
            time.sleep(2)
            lanjut = input("Tekan enter untuk lanjut")
            print("=================================================")
        else:
            print("Invalid")

    elif pilih == 5:
        print("==================================================================")
        print("=                        IF STATEMENT                            =")
        print("==================================================================")
        print("= 1. Assignment 1                                                =")
        print("= 2. Assignment 2                                                =")
        print("==================================================================")
        while True:
            try:
                a3 = int(input("Pilih Assignment yang akan dijalankan \t: "))
            except ValueError:
                continue
            if a3 == 1:
                break
            elif a3 == 2:
                break
            else:
                print("Pilihan Anda tidak ada ..!!")
                continue
        if a3 == 1:
            print("==================================================================")
            print("=                        ASSIGNMENT 1                            =")
            print("==================================================================")
            nilai = int(input("Masukkan Nilai : "))
            if nilai <= 50:
                print("Nilai D")
            elif nilai <= 70:
                print("Nilai C")
            elif nilai <= 80:
                print("Nilai B")
            else:
                print("Nilai A")
            print("=================================================")
            time.sleep(2)
            lanjut = input("Tekan enter untuk lanjut")
            print("=================================================")
        elif a3 == 2:
            print("==================================================================")
            print("=                        ASSIGNMENT 2                            =")
            print("==================================================================")
            angka3 = int(input("Masukkan Angka : "))
            if angka3 % 2 != 0:
                print("Bilangan Ganjil")
            else:
                print("Bilangan Genap")
            print("=================================================")
            time.sleep(2)
            lanjut = input("Tekan enter untuk lanjut")
            print("=================================================")

    elif pilih == 6:
        print("==================================================================")
        print("=                          LOOPING                               =")
        print("==================================================================")
        print("= 1. Assignment 1                                                =")
        print("= 2. Assignment 2                                                =")
        print("= 3. Assignment 3                                                =")
        print("==================================================================")
        while True:
            try:
                a4 = int(input("Pilih Assignment yang akan dijalankan \t: "))
            except ValueError:
                continue
            if a4 == 1:
                break
            elif a4 == 2:
                break
            elif a4 == 3:
                break
            else:
                print("Pilihan anda tidak ada ..!!")
                continue
        if a4 == 1:
            print("==================================================================")
            print("=                        ASSIGNMENT 1                            =")
            print("==================================================================")
            angka4 = 0
            print(angka4)
            while angka4 < 10:
                time.sleep(1)
                angka4 += 1
                print(angka4)
            print("=================================================")
            time.sleep(2)
            lanjut = input("Tekan enter untuk lanjut")
            print("=================================================")
        elif a4 == 2:
            print("==================================================================")
            print("=                        ASSIGNMENT 2                            =")
            print("==================================================================")
            score = 0
            end_score = 10
            print(score)
            while score < 10:
                time.sleep(1)
                score += 1
                print(score)
                # time.sleep(1)
                if score == end_score:
                    typingPrint("Kamu berhasil memenangkan permainan ini\n")
            print("=================================================")
            time.sleep(2)
            lanjut = input("Tekan enter untuk lanjut")
            print("=================================================")
        elif a4 == 3:
            print("==================================================================")
            print("=                        ASSIGNMENT 3                            =")
            print("==================================================================")
            row = 5
            for i in range(0, row):
                for j in range(0,i + 1):
                    print("* ", end=' ')
                print("")
            print("")
            time.sleep(1)
            for i in range(row,0,-1):
                for j in range(0, i -1):
                    print("* ",end="")
                print("")
            print("")
            time.sleep(1)
            for i in range(row):
                for j in range(row):
                    print("* ",end="")
                print("")
            print("=================================================")
            time.sleep(2)
            lanjut = input("Tekan enter untuk lanjut")
            print("=================================================")

    elif pilih == 7:
        print("==================================================================")
        print("=                           LIST                                 =")
        print("==================================================================")
        pesanan = []
        print("====================================")
        print("=               Menu               =")
        print("====================================")
        menu = ["Silahkan pilih Menu Makanan","1. Nasi Goreng","2. Mie Goreng",
                "3. Es Jeruk","4. Jus Mangga","5. Pisang Goreng","6. Es Teh"
                ]
        for m in menu:
            print(m)
        pilihan = input("Silahkan ketikkan menu yang akan dipesan = ")
        pesanan.append(pilihan)
        while True:
            lagi = input("Masih ingin memesan lagi? = ")
            print("")
            if lagi == 'ya' or lagi == 'iya':
                for m in menu:
                    print(m)
                pilihan = input("Silahkan ketikkan menu yang akan dipesan = ")
                pesanan.append(pilihan)
            elif lagi == 'tidak' or lagi == 'Tidak':
                print("Menu pesanan Anda : ")
                for p in pesanan:
                    print(p)
                jumlah = len(pesanan)
                total = jumlah*20000
                print("Total Harga =",total)
                print("=================================================")
                time.sleep(2)
                lanjut = input("Tekan enter untuk lanjut")
                print("=================================================")
                break

    elif pilih == 8:
        print("==================================================================")
        print("=                     MATRIX OPERATION                           =")
        print("==================================================================")
        print("= 1. Assignment 1                                                =")
        print("= 2. Assignment 2                                                =")
        print("==================================================================")
        while True:
            try:
                b1 = int(input("Pilih Assignment yang akan dijalankan \t: "))
            except ValueError:
                continue
            if b1 == 1:
                break
            elif b1 == 2:
                break
            else:
                print("Pilihan anda tidak ada ..!!")
                continue
        if b1 == 1:
            print("==================================================================")
            print("=                        ASSIGNMENT 1                            =")
            print("==================================================================")
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
            print("=================================================")
            time.sleep(2)
            lanjut = input("Tekan enter untuk lanjut")
            print("=================================================")
        elif b1 == 2:
            print("==================================================================")
            print("=                        ASSIGNMENT 2                            =")
            print("==================================================================")
            matrix = [[4, 5],[2, 6]]
            print("Matrix")
            print(matrix)
            input("Tekan enter untuk lanjut")

            # mencari determinan matrix
            det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
            if det == 0:
                print("Matrix tidak memiliki invers")
            else:
                cofactor_matrix = [[matrix[1][1], -matrix[0][1]], [-matrix[1][0], matrix[0][0]]]

                # Mencari matriks adjoin
                adjoint_matrix = [[cofactor_matrix[0][0], cofactor_matrix[1][0]],
                                  [cofactor_matrix[0][1], cofactor_matrix[1][1]]]

                # Mencari matriks invers
                inverse_matrix = [
                [adjoint_matrix[0][0] / det, adjoint_matrix[0][1] / det],
                                  [adjoint_matrix[1][0] / det, adjoint_matrix[1][1] / det]
                                  ]

                # Output matriks invers
                print("Matriks invers: ")
                for row in inverse_matrix:
                    print(row)

            print("=================================================")
            time.sleep(2)
            lanjut = input("Tekan enter untuk lanjut")
            print("=================================================")


    elif pilih == 9:
        print("==================================================================")
        print("=                          TUPLES                                =")
        print("==================================================================")
        print("= 1. Assignment 1                                                =")
        print("= 2. Assignment 2                                                =")
        print("= 3. Assignment 3                                                =")
        print("==================================================================")
        while True:
            try:
                a5 = int(input("Masukkan Assignment yang akan dijalankan \t: "))
            except ValueError:
                continue
            if a5 == 1:
                break
            elif a5 == 2:
                break
            elif a5 == 3:
                break
            else:
                print("Pilihan anda tidak ada ..!!")
                continue

        if a5 == 1:
            print("==================================================================")
            print("=                        ASSIGNMENT 1                            =")
            print("==================================================================")
            days = "senin","selasa","rabu","kamis","jumat","sabtu","minggu"
            print(days)
            lanjut = input("Tekan enter untuk lanjut")
            for d in days:
                print(d)
            print("=================================================")
            time.sleep(2)
            lanjut = input("Tekan enter untuk lanjut")
            print("=================================================")
        elif a5 == 2:
            print("==================================================================")
            print("=                        ASSIGNMENT 2                            =")
            print("==================================================================")
            days = "senin","selasa","rabu","kamis","jumat","sabtu","minggu"
            print(days)
            lanjut = input("Tekan enter untuk lanjut")
            (day1, day2, day3, day4, day5, day6, day7) = days
            print(day1,"\n")
            print(day2,"\n")
            print(day3,"\n")
            print("=================================================")
            time.sleep(2)
            lanjut = input("Tekan enter untuk lanjut")
            print("=================================================")
        elif a5 == 3:
            print("==================================================================")
            print("=                        ASSIGNMENT 3                            =")
            print("==================================================================")
            days = "senin","selasa","rabu","kamis","jumat","sabtu","minggu"
            items = "pensi","buku","laptop","PC dekstop"
            print(days)
            print(items)
            lanjut = input("Tekan enter untuk lanjut")
            combine = days + items
            print(combine)
            print("=================================================")
            time.sleep(2)
            lanjut = input("Tekan enter untuk lanjut")
            print("=================================================")

    elif pilih == 10:
        print("==================================================================")
        print("=                        DICTIONARY                              =")
        print("==================================================================")
        print("= 1. Assignment 1                                                =")
        print("= 2. Assignment 2                                                =")
        print("==================================================================")
        while True:
            try:
                d1 = int(input("Pilih Assignment yang akan dijalankan \t: "))
            except ValueError:
                continue
            if d1 == 1:
                break
            elif d1 == 2:
                break
            else:
                print("Pilihan Anda tidak ada ..!!")
                continue
        if d1 == 1:
            print("==================================================================")
            print("=                        ASSIGNMENT 1                            =")
            print("==================================================================")
            typingPrint("Pada Assignment Dictionary ke 1 membuat program sederhana dengan menerima inputan\n"
                        "berupa biodata yang terdiri dari nama,usia,alamat,username, dan password\n"
                        "kemudian data yang diterima dari input tersebut disimpan didalam Dictionary dan ditampilkan\n"
                        "setelah user melakukan input data tersebut\n")
            akun = {} #dictionary kosong
            nama = input("Silahkan Masukkan Nama Anda\t\t: ")
            umur = int(input("Silahkan Masukkan Umur Anda\t\t: "))
            alamat = input("Silahkan MAsukkan alamat Anda\t\t: ")
            username = input("Silahkan Masukkan Username Anda\t\t: ")
            password = input("Silahkan Masukkan Password Anda\t\t: ")
            akun.update({"Nama":nama})
            akun.update({"Umur":umur})                              # key
            akun.update({"Alamat":alamat})                          # value
            akun.update({"Username":username})
            akun.update({"Password":password})
            print(akun)
            enter = input("tekan enter untuk lanjut")

            print("Nama\t\t:",akun["Nama"])
            print("Umur\t\t:",akun["Umur"])
            print("Alamat\t\t:",akun["Alamat"])
            print("Username\t:",akun["Username"])
            print("Password\t:",akun["Password"])

            typingPrint("=================================================")
            time.sleep(2)
            lanjut = input("\nTekan enter untuk lanjut")
            typingPrint("=================================================\n")

        elif d1 == 2:
            print("==================================================================")
            print("=                        ASSIGNMENT 2                            =")
            print("==================================================================")
            book = {'alan':'arduino','ali':'Python'}
            while True:
                # for key in book:
                print(book)
                typingPrint("1. Tambah\n")
                typingPrint("2. Hapus\n")
                typingPrint("3. Exit\n")
                pilih = int(input("Masukkan Pilihan Anda 1/2\t: "))
                if pilih == 1:
                    name = input("Masukkan nama penuli\t: ")
                    judul = input("Masukkan judul buku\t: ")
                    book[name] = judul
                    print(book)
                elif pilih == 2:
                    print(book)
                    typingPrint("Hapus berdasarkan nama penulis\n")
                    user = input("Masukkan yang ingin dihapus \t: ")
                    del book[user]
                    print(book)
                elif pilih == 3:
                    break


    elif pilih == 11:
        print("==================================================================")
        print("=                    DICTIONARY FUNCTION                         =")
        print("==================================================================")
        print("= 1. Assignment 1                                                =")
        print("= 2. Assignment 2                                                =")
        print("==================================================================")
        while True:
            try:
                d2 = int(input("Piliha Assignment yang akan dijalankan \t: "))
            except ValueError:
                continue
            if d2 == 1:
                break
            elif d2 == 2:
                break
            else:
                print("Pilihan Anda tidak ada ..!!")
                continue
        if d2 == 1:
            print("==================================================================")
            print("=                        ASSIGNMENT 1                            =")
            print("==================================================================")
            typingPrint("Pada Assignment Dictionary Function yang ke 1 ini akan membuat 1 dictionary\n"
                        "lalu isi dalam dictionary yang memiliki value tumbuhan akan dihapus, namun\n"
                        "sebelum melakukan penghapusan dictionary dicopy terlebih dahulu\n")
            time.sleep(2)
            kamus = {'1':'Ayam','2':'Sapi','3':'Mawar','4':'Kambing','5':'Lily'}
            print("Isi Dictionary ",kamus)
            lanjut = input("\nTekan enter untuk lanjut")
            typingPrint("Sebeleum melakukan penghapusan dictionary tersebut dicopy terlebih dahulu\n"
                        "menggunakan fungsi copy()\n")
            time.sleep(2)
            typingPrint("\nHasil dari proses copy Dictionary\n")
            kamus1 = kamus.copy()
            print(kamus)
            print(kamus1)
            lanjut = input("\nTekan enter untuk lanjut")
            time.sleep(2)
            typingPrint("Proeses Penghapusan\n")
            typingPrint("\nSebelum dihapus\n")
            print(kamus)
            time.sleep(2)
            kamus.pop("3")
            kamus.pop("5")
            typingPrint("\nSetelah di hapus\n")
            print(kamus)
            time.sleep(2)
            lanjut = input("\nTekan enter untuk lanjut")
            print("=================================================")

        elif d2 == 2:
            print("==================================================================")
            print("=                        ASSIGNMENT 2                            =")
            print("==================================================================")
            typingPrint("Pada Assignment Dictionary Function yang ke 2 ini akan mengganti Value\n"
                        "Pada dictionary yang memiliki id ganjil dengan string hewan\n"
                        "di Assignment kali ini akan menggunakan fungsi key untuk mengganti\n"
                        "value dengan id ganjil dengan string hewan\n")
            time.sleep(2)
            lanjut = input("\nTekan Enter untuk lanjut")
            kamus = {'1':'Sapi','2':'Mawar','3':'Kucing','4':'Semangka','5':'Kuda'}
            typingPrint("\nSebelum di ubah : ")
            print(kamus)
            time.sleep(2)
            for key in kamus:
                if int(key) %2 != 0:
                    kamus[key] = 'hewan'
            typingPrint("\nSetelah di ubah : ")
            print(kamus)
            time.sleep(2)
            lanjut = input("\nTekan enter untuk lanjut")
            print("=================================================")
    elif pilih == 12:
        print("==================================================================")
        print("=                    DICTIONARY FUNCTION                         =")
        print("==================================================================")
        print("= 1. Project 1                                                   =")
        print("= 2. Project 2                                                   =")
        print("==================================================================")
        while True:
            try:
                pilih = int(input("Pilih Project yang akan dijalankan : "))
            except ValueError:
                continue
            if pilih == 1:
                break
            elif pilih == 2:
                break
            else:
                print("Program tidak tersedia !!!")
        if pilih == 1:
            # teks = input("Masukkan Teks : ")
            # huruf_vokal = {
            #     'a': 0,
            #     'i': 0,
            #     'u': 0,
            #     'e': 0,
            #     'o': 0
            # }
            #
            # for vokal in huruf_vokal.keys():
            #     huruf_vokal[vokal] = teks.count(vokal)
            #
            # total = sum(huruf_vokal.values())
            #
            # print(f'Total Karakter : {len(teks)}')
            # print(f'Total Huruf vokal : {total}')
            # print(f"""
            # a -> {huruf_vokal['a']}
            # i -> {huruf_vokal['i']}
            # u -> {huruf_vokal['u']}
            # e -> {huruf_vokal['e']}
            # o -> {huruf_vokal['o']}
            # """)
            #
            # pengganti = input("Masukkan huruf pengganti A : ")
            # for huruf in 'a':
            #     teks = teks.replace(huruf, pengganti)
            # print(teks)
            vokal = ["a","i","u","e","o"]
            jumlah_a = 0
            jumlah_i = 0
            jumlah_u = 0
            jumlah_e = 0
            jumlah_o = 0

            kalimat = input("Masukkan Kalimat : ")
            for huruf in kalimat.lower():
                if huruf in vokal:
                    if huruf == "a":
                        jumlah_a += 1
                    elif huruf == "i":
                        jumlah_i += 1
                    elif huruf == "u":
                        jumlah_u += 1
                    elif huruf == "e":
                        jumlah_e += 1
                    elif huruf == "o":
                        jumlah_o += 1
            print("Jumlah huruf a:", jumlah_a)
            print("Jumlah huruf i:", jumlah_i)
            print("Jumlah huruf u:", jumlah_u)
            print("Jumlah huruf e:", jumlah_e)
            print("Jumlah huruf o:", jumlah_o)

            pengganti = input("Masukkan huruf pengganti a : ")
            kalimat = kalimat.lower().replace("a", pengganti)

            print(f'Huruf yang sudah diganti : {kalimat}')

            print("=================================================")
            lanjut = input("\nTekan enter untuk lanjut")
            print("=================================================")

        elif pilih == 2:
            number = [4, 7, 6, 9, 8, 2, 3, 1, 5, 4, 6, 9, 0, 8, 7, 6, 5, 4, 8, 6, 5, 8]
            print("Sebelum di sortir")
            print(number)
            time.sleep(2)
            n = len(number)
            for i in range(n):
                for j in range(n - i - 1):
                    if number[j] > number[j + 1]:
                        number[j], number[j + 1] = number[j + 1], number[j]
            print("\nSetelah di sortir")
            print(number)
            print("=================================================")
            lanjut = input("\nTekan enter untuk lanjut")
            print("=================================================")

        else:
            print("program tidak tersedia !!!")


    elif pilih == 13:
        typingPrint("Terima kasih telah menjalankan Program ini")
        time.sleep(1)
        typingPrint("\nSemoga bermanfaat !!!")
        time.sleep(1)
        typingPrint("\nProgram ini akan di clear dalam 4..")
        time.sleep(1)
        typingPrint(" 3..")
        time.sleep(1)
        typingPrint(" 2..")
        time.sleep(1)
        typingPrint(" 1..")
        time.sleep(1)
        clearScreen()
        break
    else:
        typingPrint("Mohon Maaf pilihan anda tidak tersedia")
        time.sleep(1)
        typingPrint("\nTry Again ...\n")
        time.sleep(1)
