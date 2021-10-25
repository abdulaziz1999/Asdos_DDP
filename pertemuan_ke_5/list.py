# data array
datalist = ['ayam','kucing','kerbau','tikus','kecoa','penyu','hiu']

# menambahkan data di belakang list
datalist.append('laba-laba')
datalist.append('laba-laba2')

# menambahkan data dengan index tertentu
datalist.insert(0,'Kura-kura')
datalist.insert(4,'Kelinci')

# menghapus data dengan index tertentu
del datalist[1]
del datalist[2]

# potong datalist
datalist[1:5]
# print(datalist[2:5])

# looping datalist
no = 0
for hewan in datalist:
    no += 1
    index = no-1 
    print(index, hewan)

