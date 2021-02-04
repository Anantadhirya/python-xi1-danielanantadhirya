# Nama: D. Anantadhirya A. L.
# No. Absen: 07
# Kelas: XI MIA 1

def hasil_bagi(x, y):
    return x // y
def sisa_bagi(x, y):
    return x % y

N, M = [int(i) for i in input().split()]

print("masing-masing", hasil_bagi(N, M))
print("bersisa", sisa_bagi(N, M))