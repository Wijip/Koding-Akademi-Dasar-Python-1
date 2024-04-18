# List Multidimensi
print("Membuat List Multidimensi, dimana list Multidimensi terdapat"
      "2 buah indek yang disebut dengan index baris dan kolom")

minuman = [
    ["Kopi","Susu","Teg"],
    ["Jus Apel","Jus Melon","Jus Jeruk"],
    ["Es Kopi","Es Campur","Es Teler"]
]

print(minuman[1][1])

print("\nMenampilkan semua isi dalam index")
for list in minuman:
    for menu in list:
        print(menu)

# cara mengetahui jumlah data/panjang list
print("Mengetahui Jumlah data/Panjang dalam list menggunakan Fungsi len()")
hewan = ["Gajah","Kucing","Tikus","Anjing"]
print(len(hewan))