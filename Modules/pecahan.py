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
    "-": "⁻", "=": "⁼", "(": "⁽", ")": "⁾"
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

def simplify2(a, b, c, C, keep1 = False):
    """Fungsi untuk menyederhanakan bentuk (a + b.C)/c"""
    # Keterangan:
    # a, b, c ∈ ℤ
    # C ∈ ℝ
    FPB = math.gcd(a, b, c)
    a //= FPB
    b //= FPB
    c //= FPB
    ret = ""
    if keep1:
        ret = "({} + {}.{})/{}".format(a, b, C, c)
    else:
        ret = "{}".format(C)
        # ret = C
        if b != 1:
            ret = "{}.{}".format(b, ret)
        # ret = b.C
        if a != 0:
            ret = "{} + {}".format(a, ret)
        # ret = a + b.C
        if c != 1:
            ret = "({})/{}".format(ret, c)
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
        ret = " ‧ ".join(["{}{}".format(i, sup[str(j)]) for i,j in ret.items()])
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
    
    # Bentuk C = angka
    if sama(kons, angka):
        ret.append(("{}".format(nama_kons), abs(kons-angka)))
    
    # Bentuk a + C = angka
    if sama(kons % 1, angka % 1):
        a = round(angka - kons)
        if a != 0: ret.append(("{} + {}".format(a, nama_kons), abs(a + kons - angka)))
    
    # Bentuk a.C = angka
    a = round(angka/kons)
    if sama(a * kons, angka):
        if a != 1: ret.append(("{}{}".format(a, nama_kons), abs(a*kons - angka)))
    
    # Bentuk a + b.C = angka
    for b in range(2, max_abc):
        if sama((b * kons)%1, angka%1):
            a = round(angka - b*kons)
            if a != 0: ret.append(("{} + {}{}".format(a, b, nama_kons), abs(a + b*kons - angka)))
    
    # Bentuk C/a = angka
    a = round(kons/angka)
    if a != 0 and sama(kons/a, angka):
        if a != 1: ret.append(("{}/{}".format(nama_kons, a), abs(kons/a - angka)))
    
    # Bentuk (a + b.C)/c = angka
    for c in range(2, max_abc):
        for b in range(2, max_abc):
            if sama((b*kons)%1, (c*angka)%1):
                a = round(c*angka - b*kons)
                # belum selesai
            
    
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
        for i in range(2, 10**digit+1):
            akar = i**(1/pangkat)
            ret += konsto(angka, akar, "{}{}".format(akar_pangkat(pangkat), i))
    ret = sorted(list(set(ret)), key=lambda x: x[1])[:max_cari]
    return ret
        

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