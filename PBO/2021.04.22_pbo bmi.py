class pasien:
    jumlah_pasien = 0
    def __init__(self, nama, berat, tinggi):
        self.nama = nama
        self.berat = berat
        self.tinggi = tinggi
        pasien.jumlah_pasien += 1
    
    def bmi(self):
        bmi = self.berat/(self.tinggi**2)
        print("BMI = ", bmi)
        if bmi <= 18.5:
            print("kekurangan berat badan.")
        elif bmi > 18.5 and bmi <=24.9:
            print("berat badan ideal.")
        elif bmi > 24.9 and bmi <= 29.9:
            print("berat badan berlebih.")
        else:
            print("obesitas.")
 
    def beratIdeal(self):
        ideal = (self.tinggi*100 - 100) - (10/100 * (self.tinggi*100 - 100))
        print("BB Ideal = ", ideal)
        print("---------------------")

daftar_pasien = []
daftar_pasien.append(pasien("wawan", 110, 1.7))
daftar_pasien.append(pasien("umi", 62, 1.65))
daftar_pasien.append(pasien("andi", 70, 1.72))

for pasien in daftar_pasien:
    pasien.bmi()
    pasien.beratIdeal()
print("jumlah pasien : ", pasien.jumlah_pasien)
