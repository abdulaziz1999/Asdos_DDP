name1 = "Ahmad"
agama1 = "Islam"
pay1 = 4000000
child1 = 2


tunjab1 = pay1 * 20 / 100


if(child1 <= 2):
    tunke1 = pay1 * 10 / 100
elif(child1 > 2):
    tunke1 = pay1 * 20 / 100
else:
    tunke1 = 0

gako1 = pay1 + tunjab1 + tunke1

#Zakat profesi hanya untuk pegawai muslim dan memiliki gaji kotornya lebih dari Rp. 6.000.000.
#Zakat profesi sebesar 2,5% dari total gaji kotor.
zapro1 = (0, 0.025)[agama1 == "Islam" and gako1 >= 6000000] * gako1

gaber1 = gako1 - zapro1

print("SLIP GAJI PT. XYZ\n")
print("------------------\n")
print("Nama Pegawai \t\t: ",name1)