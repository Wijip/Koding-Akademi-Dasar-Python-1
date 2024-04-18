print("Silahkan Pilih Menu Makanan")

Makanan = ["1. Nasi Goreng", "2. Mie Goreng", "3. Es Jeruk", "4. Jus Mangga", "5. Pisang Goreng"]
for menu in Makanan:
    print(menu)

order = []

pesan = input("Silahkan Ketikan Menu Yang Akan Dipesan =")
order.append(pesan)
while(True):
    pesan_lagi = input("Masih Ingin Memesan? =")
    if pesan_lagi == "Ya":
        pesan = input("Silahkan Ketikan Menu Yang Akan Dipesan =")
        order.append(pesan)
    elif pesan_lagi == "Tidak":
        for o in order:
            print(o)
        Sum = len(order)
        total = Sum * 20000
        print("Total Harga =", total)
        break
