teks = input("Tuliskan Teks : ")
huruf_vokal = {
    'a':0,
    'i':0,
    'u':0,
    'e':0,
    'o':0
}

for vokal in huruf_vokal.keys():
    huruf_vokal[vokal] = teks.count(vokal)

total = sum(huruf_vokal.values())

print(f'Total karakter : {len(teks)}')
print(f'Total huruf vokal : {total}')
print(f"""
a -> {huruf_vokal['a']}
i -> {huruf_vokal['i']}
u -> {huruf_vokal['u']}
e -> {huruf_vokal['e']}
o -> {huruf_vokal['o']}
""")

pengganti = input("Masukkan huruf pengganti : ")

for huruf in 'a':
    teks = teks.replace(huruf,pengganti)
print(teks)