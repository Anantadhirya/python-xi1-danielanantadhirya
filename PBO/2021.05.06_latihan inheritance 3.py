class Manusia:
    def __init__(self, nama, jk, usia):
        self.__nama = nama
        self.__jk = jk
        self.__usia = usia
    def getNama(self):
        return self.__nama
    def info(self):
        print("Nama: {}\nJenis Kelamin: {}\nUsia: {}".format(self.__nama, self.__jk, self.__usia))
        print("-" * 25)
    def makan(self):
        print("Sedang makan nasi")
        print("-" * 25)

class Pelajar(Manusia):
    def __init__(self, nama, jk, usia, nis, nilai):
        Manusia.__init__(self, nama, jk, usia)
        self.__nis = nis
        self.__nilai = nilai
    def belajar(self):
        print("{} sedang belajar".format(self.getNama()))
        print("-" * 25)
    def makan(self):
        print("{} sedang sarapan pagi dengan nasi".format(self.getNama()))
        print("-" * 25)

class Pekerja(Manusia):
    def __init__(self, nama, jk, usia, nip, gaji):
        Manusia.__init__(self, nama, jk, usia)
        self.__nip = nip
        self.__gaji = gaji
    def bekerja(self):
        print("{} sedang bekerja".format(self.getNama()))

Rudi = Pelajar("Rudianto", "Laki-Laki", 16, "15234", 90)
Wawan = Pekerja("Wawan", "Laki-Laki", 29, "1987463", 50000000)
Rudi.info()
Rudi.belajar()
Rudi.makan()
Wawan.info()
Wawan.bekerja()
Wawan.makan()