# # # # list1 = ['data1', 'data2', 'data3', 'barang1', 'data4', 'data5', 'data6', 'data7']  # contoh list
# # # # # list2 = ['barang1','barang2','barang3','barang4']
# # # # # print(list[3])
# # # # # for n in list:
# # # # #     print(n)
# # # #
# # # # # print("Sebelum")
# # # # # print(list)
# # # # # list[2] = 'barang1'
# # # # # print("Sesudah")
# # # # # print(list)
# # # #
# # # # """
# # # # menambah append() dan insert()
# # # # append => di bagian paling belakang
# # # # insert => list.insert(3,"data")
# # # # """
# # # #
# # # # # list1.append("data8")
# # # # # print(list1)
# # # # #
# # # # # list1.insert(3,"data10")
# # # # # print(list1)
# # # # #
# # # # # """
# # # # # menghapus del & remove()
# # # # # del => menghapus berdasarkan index listnya
# # # # # """
# # # # # del list1[6]
# # # # # print(list1)
# # # # #
# # # # # list1.remove("data2")
# # # # # print(list1)
# # # #
# # # # # gabung = list1 + list2
# # # # # print(gabung)
# # # # #
# # # # # perkalian = list2 * 3
# # # # # print(perkalian)
# # # #
# # # # # list multidimensi
# # # # multi = [
# # # #     ["data1", "data2", "data3"],
# # # #     ["data4", "data5", "data6"],
# # # #     ["data7", "data8", "data9"]
# # # # ]
# # # # # print(multi[0][1])
# # # # # print(multi[1][1])
# # # #
# # # # # for list in multi:
# # # # #     print(list)
# # # # #     for list1 in list:
# # # # #         print(list1)
# # # #
# # # # """
# # # # fungsi len()
# # # # """
# # # # # print(len(list1))
# # # # print(len(multi[1]))
# # # #
# # # # # Assignment
# # # #
# # # # print("==================================================================")
# # # # print("=                           LIST                                 =")
# # # # print("==================================================================")
# # # # pesanan = []
# # # # print("====================================")
# # # # print("=               Menu               =")
# # # # print("====================================")
# # # # menu = ["Silahkan pilih Menu Makanan", "1. Nasi Goreng", "2. Mie Goreng",
# # # #         "3. Es Jeruk", "4. Jus Mangga", "5. Pisang Goreng"
# # # #         ]
# # # # for m in menu:
# # # #     print(m)
# # # # pilihan = input("Silahkan ketikkan menu yang akan dipesan = ")
# # # # pesanan.append(pilihan)
# # # # while True:
# # # #     lagi = input("Masih ingin memesan lagi? = ")
# # # #     print("")
# # # #     if lagi == 'ya' or lagi == 'iya':
# # # #         for m in menu:
# # # #             print(m)
# # # #         pilihan = input("Silahkan ketikkan menu yang akan dipesan = ")
# # # #         pesanan.append(pilihan)
# # # #
# # # #
# # # #
# # # # sorter =[10,20,5,30,6,7,70,45,5,8,9,3,2,12,10]
# # # # print("Sebelum")
# # # # print(sorter)
# # # # n = len(sorter)
# # # # for i in range(n):
# # # #     print(i)
# # # #     for j in range(n - i - 1):
# # # #         if sorter[j] > sorter[j + 1]:
# # # #             sorter[j], sorter[j+1] = sorter[j+1], sorter[j]
# # # #
# # # # input("Tekan enter")
# # # # print("Sesudah")
# # # # print(sorter)
# # # #
# # # # # print("\nFungsi sort")
# # # # # i = sorted(sorter)
# # # # # print(i)
# # #
# # #
# # kamus = {'1': 'Ayam', '2': 'Sapi', '3': 'Mawar', '4': 'Kambing', '5': 'Lily'}
# #
# # i = kamus.items()
# # print(i)
# # l = kamus.keys()
# # print(l)
# # p = kamus.values()
# # print(p)
# # # # mengakses data dictionary
# # # print(kamus['1'])
# # # print(kamus['2'])
# # # # [], (), {}
# # #
# # # # mengganti value pada dictionary
# # # kamus['4'] = 'Data1'
# # # print(kamus)
# # #
# # # # pop() del()
# # # # del kamus['5']
# # # # kamus.pop('4')
# # #
# # #
# # # # update()
# # # kamus.update({"key1": "data1"})
# # # print(kamus)
# # #
# # # # jumlah data menggunakan fungsi len()
# # # print(len(kamus))
# # #
# #
# # nama_hewan = {'Sapi', 'Ayam', 'Kambing'}
# #
# # hewan = dict.fromkeys(nama_hewan, 'Hewan')
# # print("Hewan: ", hewan)
#
# # number = [4, 7, 6, 9, 8, 2, 3, 1, 5, 4, 6, 9, 0, 8, 7, 6, 5, 4, 8, 6, 5, 8]
# #
# # n = len(number)
# # print(n)
#
#
# a1 = {
#     1:{
#         'Nama':"Honda",
#         "Jenis":"Mobilio"
#     },
# }
#
# print(a1)

_variabel = 1
