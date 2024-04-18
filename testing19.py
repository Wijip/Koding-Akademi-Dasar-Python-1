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

# pengganti = input("Masukkan huruf pengganti a : ")
# kalimat = kalimat.replace("a", pengganti)

for i in range(len(kalimat)):
  if kalimat[i] == "a":
    kalimat[i] = "e"

print(f'Huruf yang sudah diganti : {kalimat}')