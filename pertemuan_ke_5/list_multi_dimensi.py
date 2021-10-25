list_makanan = [
   ["Bakwan","Combro","Misro"],
   ["Sop Iga","Sop Buntut","Sop Kaki"],
   ["Nasi Uduk","Nasi Goreng","Nasi Rames"]
]

print('-------- Cetak List Pertama ------------')
print(list_makanan[0][0])
print(list_makanan[0][1])
print(list_makanan[0][2])

print('\n')
print('-------- Cetak List Kedua ------------')
print(list_makanan[1][0])
print(list_makanan[1][1])
print(list_makanan[1][2])

print('\n')
print('-------- Cetak List Ketiga ------------')
print(list_makanan[2][0])
print(list_makanan[2][1])
print(list_makanan[2][2])

print('\n')
print('-------- Cetak All Makanan ------------')
# menampilkan semua makanan
for menu in list_makanan:
    for makanan in menu:
        print(makanan)