class siswa:
    jumlah_siswa = 0

    def __init__(self, nama, kelas, alamat, nilai):
        self.nama = nama
        self.kelas = kelas
        self.alamat = alamat
        self.nilai = nilai
        siswa.jumlah_siswa += 1
    
    def viewSiswa(self):
        print("------------------------")
        print("Data Siswa")
        print("Nama   : {}".format(self.nama))
        print("Kelas  : {}".format(self.kelas))
        print("Alamat : {}".format(self.alamat))
        print("------------------------")
    
    def viewNilai(self):
        print("Data Nilai")
        print("Nama   : {}".format(self.nama))
        for nilai in self.nilai:
            print("Nilai  : {}".format(nilai))
        print("------------------------")
    
    def viewKeterangan(self):
        print("Keterangan")
        print("Nama       : {}".format(self.nama))
        print("Kelas      : {}".format(self.kelas))
        rata = sum(self.nilai)/len(self.nilai)
        print("Rata-rata  : {}".format(rata))
        if rata >= 75:
            keterangan = "Lulus."
        else:
            keterangan = "Tidak lulus."
        print("Keterangan : ", keterangan)
        print("------------------------")

daftar_siswa = []
daftar_siswa.append(siswa("Finda", "XII MIPA 1", "Magelang", [89,67,85,47]))
daftar_siswa.append(siswa("Umi", "XII MIPA 2", "Bantul", [89,97,85,87]))
for siswa in daftar_siswa:
    siswa.viewSiswa()
    siswa.viewNilai()
    siswa.viewKeterangan()
print("Jumlah siswa : ", siswa.jumlah_siswa)
