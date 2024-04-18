# # Assignment 1
# kamus = {'1': 'Ayam', '2': 'Sapi', '3': 'Mawar', '4': 'Kambing', '5': 'Lily'}
# kamus1 = kamus.copy()
#
# print(kamus)
# print(kamus1)
#
# kamus.pop("3")
# kamus.pop("5")
# print(kamus)
# print(kamus1)
# #
# # # Assignment 2
# print("\nAssignment 2")
# dic = {'1':'Sapi','2':'Mawar','3':'Kucing','4':'Semangka','5':'Kuda'}
# print(dic)
# for key in dic:
#    if int(key) %2 != 0:
#        dic[key] = 'hewan'
#
# print(dic)

##project

print("project 1\n")
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


print("\nProject 2\n")
sorter =[10,20,30,5,6,7,5,8,9,3,2,12,10]
print(sorter)
n = len(sorter)
for i in range(n):
    for j in range(n - i - 1):
        if sorter[j] > sorter[j+1]:
            sorter[j], sorter[j+1] = sorter[j+1],sorter[j]
print("hasil")
print(sorter)