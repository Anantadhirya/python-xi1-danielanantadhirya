# Nama: D. Anantadhirya A. L.
# No. Absen: 07
# Kelas: XI MIA 1

def luas_segitiga(a, t):
    return 0.5 * a * t

A, T = [int(i) for i in input().split()]

print("{:.2f}".format(luas_segitiga(A, T), 2))