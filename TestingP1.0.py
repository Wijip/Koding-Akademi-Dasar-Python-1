import tkinter as tk

# Definisikan variabel
pesanan = []
menu = ["Silahkan pilih Menu Makanan","1. Nasi Goreng","2. Mie Goreng",
        "3. Es Jeruk","4. Jus Mangga","5. Pisang Goreng"
        ]
# Buat objek jendela
# Fungsi untuk menambah pesanan
def tambah_pesanan():
    # Ambil pilihan menu dari listbox
    pilihan = listbox_menu.get(listbox_menu.curselection()[0])

    # Ambil jumlah pesanan dari entry
    jumlah = int(entry_jumlah.get())

    # Tambahkan pesanan ke list
    for i in range(jumlah):
        pesanan.append(pilihan)

# Fungsi untuk menampilkan pesanan
def tampilkan_pesanan():
    # Tampilkan pesanan
    print("Menu pesanan Anda : ")
    for p in pesanan:
        print(p)
root = tk.Tk()

# Buat label judul
label_judul = tk.Label(root, text="Menu Makanan")
label_judul.pack()

# Buat listbox untuk menampilkan menu
listbox_menu = tk.Listbox(root, width=30)
for m in menu:
    listbox_menu.insert(tk.END, m)
listbox_menu.pack()

# Buat label untuk menampilkan jumlah pesanan
label_jumlah = tk.Label(root, text="Jumlah Pesanan")
label_jumlah.pack()

# Buat entry untuk memasukkan jumlah pesanan
entry_jumlah = tk.Entry(root)
entry_jumlah.pack()

# Buat tombol untuk menambah pesanan
tombol_tambah = tk.Button(root, text="Tambah Pesanan", command=tambah_pesanan)
tombol_tambah.pack()

# Buat tombol untuk menampilkan pesanan
tombol_pesanan = tk.Button(root, text="Tampilkan Pesanan", command=tampilkan_pesanan)
tombol_pesanan.pack()

# Buat tombol untuk keluar
tombol_keluar = tk.Button(root, text="Keluar", command=root.quit)
tombol_keluar.pack()



# Jalankan program
root.mainloop()
