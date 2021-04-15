class Karyawan:
    jumlah_karyawan = 0

    def __init__(self, nama, gaji, usia):
        self.nama = nama
        self.gaji = gaji
        self.usia = usia
        Karyawan.jumlah_karyawan += 1
    
    def tampilkan_jumlah():
        print("Total karyawan: {}".format(Karyawan.jumlah_karyawan))
    
    def tampilkan_profil(self):
        print("Nama: {}".format(self.nama))
        print("Usia: {}".format(self.usia))
        print("Gaji: {}".format(self.gaji))

daftar_karyawan = []
daftar_karyawan.append(Karyawan("Sarah", 1000000, 23))
daftar_karyawan.append(Karyawan("Budi", 2000000, 26))
daftar_karyawan.append(Karyawan("Andi", 1500000, 21))

for karyawan in daftar_karyawan:
    karyawan.tampilkan_profil()
Karyawan.tampilkan_jumlah()
print()

# Diurutkan berdasarkan usia
print("Daftar karyawan diurutkan berdasarkan usia:")
daftar_karyawan = sorted(daftar_karyawan, key=lambda x: getattr(x, "usia"))
for karyawan in daftar_karyawan:
    karyawan.tampilkan_profil()
Karyawan.tampilkan_jumlah()
print()