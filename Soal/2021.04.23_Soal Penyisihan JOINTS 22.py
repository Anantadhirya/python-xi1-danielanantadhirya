# Diberikan barisan a1, a2, … yang memenuhi
# an+3 = an+2 + 2*an+1 + an
# di mana a1=2, a2=3, a3=5. Nilai dari a2021 mod 7 adalah …
# a) 2
# b) 3
# c) 4
# d) 5
# e) 6

T = [[0,1,0], [0,0,1], [1,2,1]]
F = [2, 3, 5]

def printm(matriks):
    for baris in matriks:
        for kolom in baris:
            print(kolom, end=' ')
        print()

def kali(m1, m2):
    baris1 = len(m1)
    kolom1 = len(m1[0])
    baris2 = len(m2)
    kolom2 = len(m2[0])
    ret = [[0 for kolom in range(kolom2)] for baris in range(baris1)]
    if kolom1 != baris2: return "Error"
    for baris in range(baris1):
        for kolom in range(kolom2):
            for k in range(kolom1):
                ret[baris][kolom] += m1[baris][k] * m2[k][kolom]
    return ret

def modm(matriks, mod):
    return [[kolom % mod for kolom in baris] for baris in matriks]

t = [T]
for i in range(1, 12):
    t.append(kali(t[i-1], t[i-1]))

T_print = t[5]
printm(T_print)
print()
printm(modm(T_print, 7))