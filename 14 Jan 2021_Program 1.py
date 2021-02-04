def ceknilai(nilai):
    return nilai + 2 if nilai % 2 == 0 else nilai * 2

print("hasilnya adalah {}".format(ceknilai(int(input("masukkan nilai = ")))))