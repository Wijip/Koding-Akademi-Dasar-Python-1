pesanan = []
print("====================================")
print("=               Menu               =")
print("====================================")
menu = ["Silahkan pilih Menu Makanan","1. Nasi Goreng","2. Mie Goreng",
        "3. Es Jeruk","4. Jus Mangga","5. Pisang Goreng"
]
while True:
    for m in menu:
        print(m)
    pilih = int(input("\nSilahkan Memilih menu yang akan di pesan 1/2/3/...= "))
    if pilih == 1:
        print("\nPesan Nasi goreng")
        porsi = int(input("Berapa Porsi : "))
        i = 0
        for p in range(porsi):
            pesanan.append("nasi goreng")
            i += 1
            if i == p:
                break
        print(pesanan)