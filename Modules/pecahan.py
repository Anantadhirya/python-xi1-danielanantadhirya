import math
max_digit = 4
digit = 0
max_cari = 20
max_pangkat = 3
sup = {
    "0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵", "6": "⁶",
    "7": "⁷", "8": "⁸", "9": "⁹", "a": "ᵃ", "b": "ᵇ", "c": "ᶜ", "d": "ᵈ",
    "e": "ᵉ", "f": "ᶠ", "g": "ᵍ", "h": "ʰ", "i": "ᶦ", "j": "ʲ", "k": "ᵏ",
    "l": "ˡ", "m": "ᵐ", "n": "ⁿ", "o": "ᵒ", "p": "ᵖ", "q": "۹", "r": "ʳ",
    "s": "ˢ", "t": "ᵗ", "u": "ᵘ", "v": "ᵛ", "w": "ʷ", "x": "ˣ", "y": "ʸ",
    "z": "ᶻ", "A": "ᴬ", "B": "ᴮ", "C": "ᶜ", "D": "ᴰ", "E": "ᴱ", "F": "ᶠ",
    "G": "ᴳ", "H": "ᴴ", "I": "ᴵ", "J": "ᴶ", "K": "ᴷ", "L": "ᴸ", "M": "ᴹ",
    "N": "ᴺ", "O": "ᴼ", "P": "ᴾ", "Q": "Q", "R": "ᴿ", "S": "ˢ", "T": "ᵀ",
    "U": "ᵁ", "V": "ⱽ", "W": "ᵂ", "X": "ˣ", "Y": "ʸ", "Z": "ᶻ", "+": "⁺",
    "-": "⁻", "=": "⁼", "(": "⁽", ")": "⁾"}

def akar_pangkat(pangkat):
    """Fungsi untuk mengeluarkan string berupa akar pangkat"""
    if type(pangkat) != str:
        pangkat = str(pangkat)
    pangkat = ''.join(sup[i] for i in pangkat)
    return "{}√".format(pangkat)

def simplify(pembilang, penyebut, keepDivisor1 = False):
    """Fungsi untuk menyederhanakan pecahan"""
    FPB = math.gcd(pembilang, penyebut)
    pembilang //= FPB
    penyebut //= FPB
    return "{}/{}".format(pembilang, penyebut) if keepDivisor1 or penyebut != 1 else "{}".format(pembilang)

def dtof(angka):
    """'Decimal to Fraction' -> Fungsi untuk mengubah float menjadi pecahan"""
    a = []
    for i in range(1, 10**digit+1):
        if round(round(angka*i)/i, digit) == round(angka, digit):
            a.append((simplify(round(angka*i), i), abs(round(angka*i)/i - angka)))
    a = sorted(list(set(a)), key=lambda x: x[1])[:max_cari]
    return a

def dtor(angka):
    """'Decimal to Root' -> Fungsi untuk mengubah float menjadi bentuk akar (√)"""
    a = []
    for pangkat in range(2, max_pangkat+1):
        for i in range(2, 10**digit+1):
            akar = i**(1/pangkat)
            # bentuk ᵇ√a = angka
            if round(akar, digit) == round(angka, digit):
                a.append(("{}{}".format(akar_pangkat(pangkat), i), abs(akar-angka)))
            # bentuk c + ᵇ√a = angka
            elif round(abs(round(angka, digit) - round(akar, digit)) % 1) == 0:
                a.append(("{} + {}{}".format(round(round(angka,digit)-round(akar,digit)), akar_pangkat(pangkat), i), abs(akar-angka)%1))
    a = sorted(list(set(a)), key=lambda x: x[1])[:max_cari]
    return a
        

def uncalc(angka):
    """Fungsi untuk mengubah angka pembulatan kalkulator menjadi angka sebelum pembulatan"""
    global digit
    digit = min(max_digit, len(str(angka).split('.')[1]) if '.' in str(angka) else 0)
    ret = []
    ret += dtof(angka)
    ret += dtor(angka)
    
    max_len = max(len(str(i[0])) for i in ret)
    ret = sorted(list(set([(str(i[0]) + ' '*(max_len-len(str(i[0]))), i[1]) for i in ret])), key=lambda x:x[1])[:max_cari]
    print(*["{}\t error={:.1e}".format(i[0], i[1]) for i in ret], sep='\n')
    return