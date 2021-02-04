# Nama: D. Anantadhirya A. L.
# No. Absen: 07
# Kelas: XI MIA 1

# Definisi fungsi
def penjumlahan( *vartuple ):
    print("Jumlahnya adalah: ")
    jumlah = 0;
    for var in vartuple:
        jumlah += var
    print(jumlah)

def rata(*vartuple):
    print("Rata-ratanya adalah: ")
    rerata = 0
    tot = 0
    for var in vartuple:
        tot += var
    rerata = tot / len(vartuple)
    print(rerata)

# Empat argumen
penjumlahan( 10, 30, 50, 70 )
rata( 10, 30, 50, 70 )