# Membuat List
print("Membuat List")
hewan = ["Sapi","Ayam","Kambing","Kuda"]
item_list = ["Book",23,1984,True,"Pencil"]

# menampilkan item lis menggunakan For
print("Menamplkan item dalam List menggunakan For")
for h in hewan:
    print(h)
for item in item_list:
    print(item)

# Mengambil Nilai dari List
print("\nMengambil nilai tertentu yang terdapat pada list")

print("\nData pertama")
print(hewan[0])

print("\nData Kedua")
print(hewan[1])

# Mengganti nilai list
print("\nMengganti nilai list menggunakan index")
print("Sebelum diubah")
print(hewan[0])
hewan[0] = "Kanguru"
print("Setelah diubah ")
print(hewan[0])

# menambahkan nilai kedalam list
print("\nmenambahkan nilai dari belakang menggunakan fungsi append(item)")
colors = ["Red","Blue","Green"]
print("Sebeleum Di tambah")
print(colors)
colors.append("Brown")
print("Setelah ditambah")
print(colors)

# menghapus nilai pada list
print("\nMenghapus Nilai pada list menggunakan fungsi remove()")
colors.remove("Blue")

# Operasi Pada List
print("\nOperasi Penggabungan List")
hewan1 = ["gajah","Kucing","Tikus","Anjing"]
tumbuhan = ["Putri Malu","Lidah Buaya","Mangga"]
mahluk_hidup = hewan1 + tumbuhan