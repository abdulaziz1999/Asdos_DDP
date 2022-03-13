print("----------banyak input----------")
nama = input("Nama:")
gender = str(input("Jenis kelamin:"))
umur = int(input("Umur:"))
beratBadan = float(input("Berat badan:"))

print("Nama\t\t: %s"
      "\nJenis kelamin\t: %s"
      "\nUmur\t\t: %i Tahun"
      "\nBerat badan\t: %.2f Kg" % (nama, gender, umur, beratBadan)
      )