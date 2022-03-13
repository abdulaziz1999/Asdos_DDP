# barang = {'Kipas Angin':1000000, 'TV':2000000, 'Mesin Cuci':3000000, 'Ac':4000000, 'Kulkas':5000000}
barang = [
    ["Kipas Angin", "TV", "Mesin Cuci", "Ac", "Kulkas", "Cencel"],
    [1000000, 2000000, 3000000, 4000000, 5000000],
    [5,10,20]
]
bagi = 100

print("\n====Selamat Datang di Produk Elektronik====")
nama = input("\nNama Pelanggan : ")

print("\n================Menu Barang================")
bar = barang[0]
for nabar in bar:
    no = bar.index(nabar)+1
    print(no,"%s" %(nabar))
print("===========================================")

#Nuzurwan Patri Arja
#0110221230
selectmenu = int(input("Silahkan pilih menu: "))

#Kipas Angin
if selectmenu == 1:
    print(
        "\nNama barang \t:",barang[0][0],
        "\nHarga barang \t:",barang[1][0],
        "\nDiskon barang \t:",barang[2][0],"%"
    )
    jumbar = int(input("Berapa jumlah barang yg di inginkan : "))
    konfir = input("Konfirmasi: apakah anda ingin melanjutkan transaksi? y/n ")

    if konfir == "y":
        harko = jumbar * barang[1][0]
        disc = harko * barang[2][0] / bagi
        ppn = (harko - disc) * barang[2][1] / bagi
        haber = (harko - disc) + ppn

        print("\n===========================================") 
        print(
            "\nNama Pelanggan \t:",nama,
            "\nNama Produk \t:",barang[0][0],
            "\nHarga Produk \t:",barang[1][0],
            "\nJumlah Beli \t:",jumbar,
            "\nHarga Kotor \t:",float(harko),
            "\nDiskon \t\t:",barang[2][0],"%"
            "\nPPN 10% \t:",ppn,
            "\nHarga Bersih \t:",float(haber)
        )
        print("===========================================")
    elif konfir == "n":
        print("\n===========================================")
        print("Terimkasih telah melihat-melihat Toko kami")
        print("===========================================")
        exit()
    else:
        print("Error, enter only the letter y or n")
        exit()
#TV
elif selectmenu == 2:
    print(
        "\nNama barang \t:",barang[0][1],
        "\nHarga barang \t:",barang[1][1],
        "\nDiskon barang \t:",barang[2][0],"%"
    )
    jumbar = int(input("Berapa jumlah barang yg di inginkan : "))
    konfir = input("Konfirmasi: apakah anda ingin melanjutkan transaksi? y/n ")

    if konfir == "y":
        harko = jumbar * barang[1][1]
        disc = harko * barang[2][0] / bagi
        ppn = (harko - disc) * barang[2][1] / bagi
        haber = (harko - disc) + ppn

        print("\n===========================================") 
        print(
            "Nama Pelanggan \t:",nama,
            "\nNama Produk \t:",barang[0][1],
            "\nHarga Produk \t:",barang[1][1],
            "\nJumlah Beli \t:",jumbar,
            "\nHarga Kotor \t:",float(harko),
            "\nDiskon \t\t:",barang[2][0],"%"
            "\nPPN 10% \t:",ppn,
            "\nHarga Bersih \t:",float(haber)
        )
        print("===========================================")
    elif konfir == "n":
        print("\n===========================================")
        print("Terimkasih telah melihat-melihat Toko kami")
        print("===========================================")
        exit()
    else:
        print("Error, enter only the letter y or n")
        exit()
#Mesin Cuci
elif selectmenu == 3:
    print(
        "\nNama barang \t:",barang[0][2],
        "\nHarga barang \t:",barang[1][2],
        "\nDiskon barang \t:",barang[2][0],"%"
    )
    jumbar = int(input("Berapa jumlah barang yg di inginkan : "))
    konfir = input("Konfirmasi: apakah anda ingin melanjutkan transaksi? y/n ")

    if konfir == "y":
        harko = jumbar * barang[1][2]
        disc = harko * barang[2][0] / bagi
        ppn = (harko - disc) * barang[2][1] / bagi
        haber = (harko - disc) + ppn

        print("\n===========================================") 
        print(
            "Nama Pelanggan \t:",nama,
            "\nNama Produk \t:",barang[0][2],
            "\nHarga Produk \t:",barang[1][2],
            "\nJumlah Beli \t:",jumbar,
            "\nHarga Kotor \t:",float(harko),
            "\nDiskon \t\t:",barang[2][0],"%"
            "\nPPN 10% \t:",ppn,
            "\nHarga Bersih \t:",float(haber)
        )
        print("===========================================")
    elif konfir == "n":
        print("\n===========================================")
        print("Terimkasih telah melihat-melihat Toko kami")
        print("===========================================")
        exit()
    else:
        print("Error, enter only the letter y or n")
        exit()
#Ac
elif selectmenu == 4:
    print(
        "\nNama barang \t:",barang[0][3],
        "\nHarga barang \t:",barang[1][3],
        "\nDiskon barang \t:",barang[2][0],"%"
        "\nNote: mendapatkan diskon",barang[2][2],"% jika jumlah beli 5 atau lebih"
    )
    jumbar = int(input("Berapa jumlah barang yg di inginkan : "))
    konfir = input("Konfirmasi: apakah anda ingin melanjutkan transaksi? y/n ")

    if konfir == "y":
        if jumbar >= 5:
            harko = jumbar * barang[1][3]
            disc = harko * barang[2][2] / bagi
            ppn = (harko - disc) * barang[2][1] / bagi
            haber = (harko - disc) + ppn

            print("\n===========================================") 
            print(
                "Nama Pelanggan \t:",nama,
                "\nNama Produk \t:",barang[0][3],
                "\nHarga Produk \t:",barang[1][3],
                "\nJumlah Beli \t:",jumbar,
                "\nHarga Kotor \t:",float(harko),
                "\nDiskon \t\t:",barang[2][2],"%"
                "\nPPN 10% \t:",ppn,
                "\nHarga Bersih \t:",float(haber)
            )
            print("===========================================")
        else:
            harko = jumbar * barang[1][3]
            disc = harko * barang[2][0] / bagi
            ppn = (harko - disc) * barang[2][1] / bagi
            haber = (harko - disc) + ppn

            print("\n===========================================") 
            print(
                "Nama Pelanggan \t:",nama,
                "\nNama Produk \t:",barang[0][3],
                "\nHarga Produk \t:",barang[1][3],
                "\nJumlah Beli \t:",jumbar,
                "\nHarga Kotor \t:",float(harko),
                "\nDiskon \t\t:",barang[2][0],"%"
                "\nPPN 10% \t:",ppn,
                "\nHarga Bersih \t:",float(haber)
            )
            print("===========================================") 
    elif konfir == "n":
        print("\n===========================================")
        print("Terimkasih telah melihat-melihat Toko kami")
        print("===========================================")
        exit()
    else:
        print("Error, enter only the letter y or n")
        exit()
#kulkas
elif selectmenu == 5:
    print(
        "\nNama barang \t:",barang[0][4],
        "\nHarga barang \t:",barang[1][4],
        "\nDiskon barang \t:",barang[2][0],"%"
        "\nNote: mendapatkan diskon",barang[2][1],"% jika jumlah beli 3 atau lebih"
    )
    jumbar = int(input("Berapa jumlah barang yg di inginkan : "))
    konfir = input("Konfirmasi: apakah anda ingin melanjutkan transaksi? y/n ")

    if konfir == "y":
        if jumbar >= 3:
            harko = jumbar * barang[1][4]
            disc = harko * barang[2][1] / bagi
            ppn = (harko - disc) * barang[2][1] / bagi
            haber = (harko - disc) + ppn

            print("\n===========================================") 
            print(
                "Nama Pelanggan \t:",nama,
                "\nNama Produk \t:",barang[0][4],
                "\nHarga Produk \t:",barang[1][4],
                "\nJumlah Beli \t:",jumbar,
                "\nHarga Kotor \t:",float(harko),
                "\nDiskon \t\t:",barang[2][1],"%"
                "\nPPN 10% \t:",ppn,
                "\nHarga Bersih \t:",float(haber)
            )
            print("===========================================")
        else:
            harko = jumbar * barang[1][4]
            disc = harko * barang[2][0] / bagi
            ppn = (harko - disc) * barang[2][1] / bagi
            haber = (harko - disc) + ppn

            print("\n===========================================") 
            print(
                "Nama Pelanggan \t:",nama,
                "\nNama Produk \t:",barang[0][4],
                "\nHarga Produk \t:",barang[1][4],
                "\nJumlah Beli \t:",jumbar,
                "\nHarga Kotor \t:",float(harko),
                "\nDiskon \t\t:",barang[2][0],"%"
                "\nPPN 10% \t:",ppn,
                "\nHarga Bersih \t:",float(haber)
            )
            print("===========================================") 
    elif konfir == "n":
        print("\n===========================================")
        print("Terimkasih telah melihat-melihat Toko kami")
        print("===========================================")
        exit()
    else:
        print("Error, enter only the letter y or n")
        exit()
# keluar
elif selectmenu == 6:
    print("\n===========================================")
    print("Terimkasih telah melihat Toko kami")
    print("===========================================")
    exit()
else:
    print('tes')
