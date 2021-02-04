# Nama: D. Anantadhirya A. L.
# No. Absen: 07
# Kelas: XI MIA 1

def modus(arr):
    maks_count = max(arr.count(i) for i in arr)
    return max(i for i in arr if arr.count(i) == maks_count)

N = int(input())
a = [int(i) for i in input().split()]
print(modus(a))