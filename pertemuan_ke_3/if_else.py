nama = input("Masukan Nama Anda : ")
umur = int(input("Masukan umur anda : "))
hobi = input("Masukan Hobi :")
if(umur >= 25):
    print(nama,"Kamu Berumur Tua")
elif(umur <= 17):
    print(nama,"Kamu Bocil")
else:
    print(nama,"Kamu Remaja")
    
if(hobi == 'renang' or hobi == 'Renang'):
    print("Selamat Hobi kamu",hobi)
elif(hobi == 'takraw'):
    print("Selamat Hobi kamu",hobi)
else:
    print("hobi kamu selain renang dan takraw")
