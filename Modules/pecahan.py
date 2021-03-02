from math import gcd

def simplify(pembilang, penyebut, keepDivisor1 = False):
    """Fungsi untuk menyederhanakan pecahan"""
    FPB = gcd(pembilang, penyebut)
    pembilang //= FPB
    penyebut //= FPB
    return "{}/{}".format(pembilang, penyebut) if keepDivisor1 or penyebut != 1 else "{}".format(pembilang)

def dtof(angka):
    """'Decimal to Fraction' -> Fungsi untuk mengubah float menjadi pecahan"""
    digit = len(str(angka).split('.')[1]) if '.' in str(angka) else 0
    a = [(round(angka*i), i, abs(round(angka*i)/i - angka)) for i in range(1, min(100, 10**digit)+1) if round(round(angka*i)/i, digit) == angka]
    a = [(simplify(i[0], i[1]), i[2]) for i in a]
    a = sorted(list(set(a)), key=lambda x: x[1])
    a = ["{} error={:.2f}%".format(i[0], 100 * i[1] / angka) for i in a]
    return a