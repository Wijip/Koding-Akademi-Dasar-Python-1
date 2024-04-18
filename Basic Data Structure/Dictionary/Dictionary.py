def dictionary():
    print("======================================================================")
    print("=                           DICTIONARY                               =")
    print("======================================================================")
    print("1. Membuat")
    print("2. Akses")
    print("3. Mengubah")
    print("4. Menghapus")
    print("5. Menambah")
    print("6. Print Jumlah")
    print("7. Assignment")
    while True:
        try:
            pilih = int(input("Pilih\t: "))
        except ValueError:
            print("\nInput Invalid")
            continue

        if pilih == 1:
            break
        elif pilih == 2:
            break
        elif pilih == 3:
            break
        elif pilih == 4:
            break
        elif pilih == 5:
            break
        elif pilih == 6:
            break
        elif pilih == 7:
            break
        else:
            print("\nInput Invalid")
            continue
    if pilih == 1:
        print("==========================")
        print("Membuat Dictionary")
        print("==========================")
        kamus1 = {
            "nama"      : "Wiji",
            "umur"      : 22,
            "Alamat"    : "pasuruan",
            "username"  : "koding",
            "password"  : 12345
        }

        print(kamus1)

    elif pilih == 2:
        print("==========================")
        print("Akses Nilai Dictionary")
        print("akses nilai dictionary dengan cara nama_dictionary[key dengan tanda kutip 2 ("")")
        print("==========================")
        kamus1 = {
            "nama": "Wiji",
            "umur": 22,
            "Alamat": "pasuruan",
            "username": "koding",
            "password": 12345
        }
        print(kamus1)
        print("\nMenagmbil Nilai dengan Kay Nama")
        ambil = kamus1["nama"]
        print(ambil)

        print("\nMenggunakan Perulangan for")
        for nama in kamus1:
            print(kamus1[nama])

    elif pilih == 3:
        print("==========================")
        print("Mengubah Nilai Dictionary")
        print("akses nilai dictionary dengan cara nama_dictionary[key dengan tanda kutip 2 ("")")
        print("==========================")
        kamus1 = {
            "nama": "Wiji",
            "umur": 22,
            "Alamat": "pasuruan",
            "username": "koding",
            "password": 12345
        }
        print(kamus1)
        print("\nMengganti nilai item dengan key username")
        kamus1["username"] = "admin"
        print(kamus1)

    elif pilih == 4:
        print("==========================")
        print("Akses Nilai Dictionary")
        print("akses nilai dictionary dengan cara nama_dictionary[key dengan tanda kutip 2 ("")")
        print("==========================")
        kamus1 = {
            "nama": "Wiji",
            "umur": 22,
            "Alamat": "pasuruan",
            "username": "koding",
            "password": 12345
        }

        print("\nUntuk mengapus nilai dalam dictionary dapat menggunakan 2 cara Yaitu:"
              "\n1. Menggunakan pop()"
              "\n2. Menggunakan del"
              "\n3. stop")
        print("\nMenggunakan pop()")
        while True:
            try:
                pilih = int(input("Pilih\t: "))
            except ValueError:
                print("Input Invalid")
                continue
            if pilih == 1:
                break
            elif pilih == 2:
                break
            elif pilih == 3:
                break
            else:
                print("Input Invalid")
                continue
        if pilih == 1:
            print(kamus1)
            print("\nMenggunakan Method pop()")
            kamus1.pop("umur")
        elif pilih == 2:
            print(kamus1)
            print("\nMenggunakan del")
            del kamus1["umur"]
        elif pilih == 3:
            exit()
        else:
            print("Input Invalid")
    elif pilih == 5:
        print("\nMenambah Nilai pada dictionary")
        akun = {
            "username":"admin"
        }
        print(akun)
        print("\nMenambah Password pada akun")
        akun.update({"password":123})
        print(akun)

    elif pilih == 6:
        print("\nJumlah item di dalam dictionary")
        kamus1 = {
            "nama": "Wiji",
            "umur": 22,
            "Alamat": "pasuruan",
            "username": "koding",
            "password": 12345
        }
        print(len(kamus1))

    elif pilih == 7:
        print("============================================")
        print("=                ASSIGNMENT                =")
        print("============================================")
        print("= 1. ASSIGNMENT 1                          =")
        print("= 2. ASSIGNMENT 2                          =")
        print("============================================")

        while True:
            try:
                pilih = int(input("Pilih\t:"))
                print("============================================")
            except ValueError:
                print("Invalid")
                continue

            if pilih == 1:
                break
            elif pilih == 2:
                break
            else:
                print("Invalud")
                continue
        if pilih == 1:
            print("============================================")
            print("=                ASSIGNMENT 1              =")
            print("============================================")
            akun = {}
            nama = input("Silahkan Masukkan Nama Anda\t\t= ")
            umur = int(input("Silahkan Masukkan Umur Anda\t\t= "))
            alamat = input("Silahkan Masukkan Alamat Anda\t= ")
            username = input("Silahkan Masukkan Username Anda\t= ")
            password = input("Silahkan Masukkan Password Anda\t= ")
            akun.update({"nama":nama})
            akun.update({"umur":umur})
            akun.update({"alamat":alamat})
            akun.update({"username":username})
            akun.update({"password":password})

            print("Nama\t\t=",akun["nama"])
            print("Umur\t\t=",akun["umur"])
            print("Alamat\t\t=",akun["alamat"])
            print("Username\t=",akun["username"])
            print("Password\t=",akun["password"])

        elif pilih == 2:
            dictionary = {'1': 'python'}
            while True:
                print("============================================")
                print("= 1. TAMBAH                                =")
                print("= 2. HAPUS                                 =")
                print("============================================")
                print("= Pilih\t:                                  ")
                print("============================================")
            ele = int(input("How many element u want? "))
            for i in range(ele):
                inn = input("Key: ")
                nam = input("Value: ")
                dictionary.update({inn: nam})

            print(dictionary)


dictionary()