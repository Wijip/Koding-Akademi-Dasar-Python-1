pesanan = []
print("====================================")
print("=               Menu               =")
print("====================================")
menu = ["Silahkan Pilih Menu Makanan","1. Nasi Goreng","2. Mie Goreng",
        "3. Es Jeruk","4. Jus Mangga","5. Pisang Goreng"
        ]
for m in menu:
    print(m)
pilihan = input("Silahkan Ketikkan Menu yang akan dipesan = ")
pesanan.append(pilihan)
while(True):
    lagi = input("Masih Ingin Memesan Lagi? = ")
    print("")
    if lagi == 'ya':
        for m in menu:
            print(m)
        pilihan = input("Silahkan Ketikkan Menu yang akan dipesan = ")
        pesanan.append(pilihan)
    elif lagi == 'tidak':
        print("Menu Pesanan Anda : ")
        for p in pesanan:
            print(p)
        jumlah = len(pesanan)
        total = jumlah*20000
        print("Total Harga =",total)
        break