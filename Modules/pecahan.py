from math import gcd
max_digit = 4
max_cari = 20

def simplify(pembilang, penyebut, keepDivisor1 = False):
    """Fungsi untuk menyederhanakan pecahan"""
    FPB = gcd(pembilang, penyebut)
    pembilang //= FPB
    penyebut //= FPB
    return "{}/{}".format(pembilang, penyebut) if keepDivisor1 or penyebut != 1 else "{}".format(pembilang)

def dtof(angka):
    """'Decimal to Fraction' -> Fungsi untuk mengubah float menjadi pecahan"""
    digit = min(max_digit, len(str(angka).split('.')[1]) if '.' in str(angka) else 0)
    a = []
    for i in range(1, 10**digit+1):
        if round(round(angka*i)/i, digit) == round(angka, digit):
            a.append((simplify(round(angka*i), i), abs(round(angka*i)/i - angka)))
    a = sorted(list(set(a)), key=lambda x: x[1])[:max_cari]
    a = ["{} error={:.1e}".format(i[0], i[1]) for i in a]
    return a