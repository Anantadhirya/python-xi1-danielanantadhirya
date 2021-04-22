import math
max_digit = 4
digit = 0
max_cari = 20
max_pangkat = 2
max_akar = 100
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
    "-": "⁻", "=": "⁼", "(": "⁽", ")": "⁾"
    }
sub = {
    "0": "₀", "1": "₁", "2": "₂", "3": "₃", "4": "₄", "5": "₅", "6": "₆",
    "7": "₇", "8": "₈", "9": "₉", "a": "ₐ", "b": "b", "c": "c", "d": "d",
    "e": "ₑ", "f": "f", "g": "g", "h": "ₕ", "i": "ᵢ", "j": "ⱼ", "k": "ₖ",
    "l": "ₗ", "m": "ₘ", "n": "ₙ", "o": "ₒ", "p": "ₚ", "q": "q", "r": "ᵣ",
    "s": "ₛ", "t": "ₜ", "u": "ᵤ", "v": "ᵥ", "w": "w", "x": "ₓ", "y": "y",
    "z": "z", "+": "₊", "-": "₋", "=": "₌", "(": "₍", ")": "₎"
}
konstanta = {
    "π": [math.pi, 3.14, 22/7], "g": [9.807, 9.8,  10], "R (J/mol.K)": [8.3144621, 8.314, 8.31],
    "R (liter.atm/mol.K)": [0.08205746, 0.082], "k": [1.38064852e-23, 1.38e-23]
}

def akar_pangkat(pangkat):
    """Fungsi untuk mengeluarkan string berupa akar pangkat"""
    if type(pangkat) != str:
        pangkat = str(pangkat)
    if pangkat == '2': pangkat = ''
    else: pangkat = ''.join(sup[i] for i in pangkat)
    return "{}√".format(pangkat)

def simplify(pembilang, penyebut, keepDivisor1 = False):
    """Fungsi untuk menyederhanakan pecahan"""
    FPB = math.gcd(pembilang, penyebut)
    pembilang //= FPB
    penyebut //= FPB
    return "{}/{}".format(pembilang, penyebut) if keepDivisor1 or penyebut != 1 else "{}".format(pembilang)

def simplify2(a, b, c, C, keep01 = False):
    """Fungsi untuk menyederhanakan bentuk (a + b.C)/c"""
    # Keterangan:
    # a, b, c ∈ ℤ
    # C ∈ ℝ
    FPB = math.gcd(a, b, c)
    a //= FPB
    b //= FPB
    c //= FPB
    ret = ""
    if keep01:
        ret = "({} + {}{})/{}".format(a, b, C, c)
    else:
        ret = "{}".format(C)
        # ret = C
        if b != 1:
            ret = "{}{}".format(b, ret)
        # ret = b.C
        if a != 0:
            ret = "{} + {}".format(a, ret)
        # ret = a + b.C
        if c != 1:
            ret = "({})/{}".format(ret, c)
        # ret = (a + b.C)/c
    return ret

def fp(angka, asString = True):
    """Fungsi untuk menuliskan faktorisasi prima dari suatu angka"""
    ret = {}
    faktor = 2
    while angka > 1:
        if angka % faktor == 0:
            if faktor in ret.keys():
                ret[faktor] += 1
            else:
                ret[faktor] = 1
            angka //= faktor
        else:
            faktor += 1
    if asString:
        ret = " . ".join(["{}{}".format(i, sup[str(j)]) for i,j in ret.items()])
    return ret

def sama(float1, float2):
    return round(float1, digit) == round(float2, digit)

def konsto(angka, kons, nama_kons):
    """Fungsi untuk menuliskan angka dinyatakan dalam suatu konstanta"""
    # Keterangan:
    # a, b, c ∈ ℤ
    # C ∈ ℝ
    ret = []
    max_abc = 10**digit+1
    # Bentuk (a + b.C)/c = angka
    for c in range(1, max_abc):
        for b in range(1, max_abc):
            if sama((b*kons)%1, (c*angka)%1):
                a = round(c*angka - b*kons)
                ret.append((simplify2(a, b, c, nama_kons), abs(a + b*kons - c*angka)))
    ret = sorted(list(set(ret)), key=lambda x: x[1])[:max_cari]
    return ret

def dtof(angka):
    """'Decimal to Fraction' -> Fungsi untuk mengubah float menjadi pecahan"""
    ret = []
    for i in range(1, 10**digit+1):
        if sama(round(angka*i)/i, angka):
            ret.append((simplify(round(angka*i), i), abs(round(angka*i)/i - angka)))
    ret = sorted(list(set(ret)), key=lambda x: x[1])[:max_cari]
    return ret

def dtor(angka):
    """'Decimal to Root' -> Fungsi untuk mengubah float menjadi bentuk akar (√)"""
    ret = []
    for pangkat in range(2, max_pangkat+1):
        for i in range(2, max_akar):
            akar = i**(1/pangkat)
            ret += konsto(angka, akar, "{}{}".format(akar_pangkat(pangkat), i))
    ret = sorted(list(set(ret)), key=lambda x: x[1])[:max_cari]
    return ret
        

def uncalc(angka):
    """Fungsi untuk mengubah angka pembulatan kalkulator menjadi angka sebelum pembulatan"""
    global digit
    digit = min(max_digit, len(str(angka).split('.')[1]) if '.' in str(angka) else 0)
    ret = []
    if type(angka) == int: ret += (fp(angka), 0)
    ret += dtof(angka)
    ret += dtor(angka)
    
    max_len = max(len(str(i[0])) for i in ret)
    ret = sorted(list(set([(str(i[0]) + ' '*(max_len-len(str(i[0]))), i[1]) for i in ret])), key=lambda x:x[1])[:max_cari]
    print(*["{}\t error={:.1e}".format(i[0], i[1]) for i in ret], sep='\n')
    return