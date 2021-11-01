nama = input("Masukan Nama Anda : ")
umur = int(input("Masukan umur anda : "))
if(umur >= 25):
    print(nama,"Kamu Tua")
elif(umur <= 17):
    print(nama,"Kamu Bocil")
else:
    print(nama,"Kamu Remaja")