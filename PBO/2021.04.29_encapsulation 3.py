class siswa:
    def __init__(self, nis, nama, kelas):
        self.__nis = nis
        self.__nama = nama
        self.__kelas = kelas
    
    # decorator
    @property
    def nis(self):
        pass

    @nis.getter
    def nis(self):
        return self.__nis
    
    @nis.setter
    def nis(self, newnis):
        self.__nis = newnis

wawan = siswa(16354, "Sopan Setiawan", "XI MIPA 1")
print(wawan.nis)
wawan.nis = 123456
print(wawan.nis)