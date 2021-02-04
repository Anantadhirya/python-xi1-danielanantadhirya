def penjumlahan(*angka) :
    print("Jumlahnya adalah: {}".format(sum(i for i in angka)))

def rata(*angka) :
    print("Rata-ratanya adalah: {}".format(sum(i for i in angka)/len(angka)))

penjumlahan(10, 30, 50, 70)
rata(10, 30, 50, 70)