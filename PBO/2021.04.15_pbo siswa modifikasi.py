class Siswa:
    jumlah_siswa = 0

    def __init__(self, nama, nomer, kelas):
        self.nama = nama
        self.no = nomer
        self.kelas = kelas
        self.kehadiran = {"hadir":0, "izin":0, "sakit":0}
    
    def presensi(self, keterangan):
        keterangan = keterangan.casefold()
        if keterangan not in self.kehadiran.keys():
            print("Keterangan presensi kurang jelas")
        else:
            self.kehadiran[keterangan] += 1
    
    def tampilkan_profil(self):
        print("Nama: {}".format(self.nama))
        print("Nomor: {}".format(self.no))
        print("Kelas: {}".format(self.kelas))
        print("Kehadiran:")
        for keterangan, jumlah in self.kehadiran.items():
            print("- {}: {}".format(keterangan, jumlah))

def presensi(nama, keterangan):
    for siswa in daftar_siswa:
        if siswa.nama.casefold() == nama.casefold():
            siswa.presensi(keterangan)

daftar_siswa = []
daftar_siswa.append(Siswa("Ananta", 2, "XI MIPA 1"))
daftar_siswa.append(Siswa("Abe", 1, "XI MIPA 1"))
daftar_siswa.append(Siswa("Arik", 3, "XI MIPA 1"))
daftar_siswa = sorted(daftar_siswa, key=lambda x: getattr(x, "no"))
presensi("Ananta", "Hadir")
presensi("Abe", "Hadir")
presensi("Arik", "Izin")

print("Jumlah siswa: {}".format(Siswa.jumlah_siswa))
for indeks, siswa in enumerate(daftar_siswa):
    print("{}. ".format(indeks+1))
    siswa.tampilkan_profil()
    print()