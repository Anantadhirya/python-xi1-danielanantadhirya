"""Module untuk melakukan print dengan mudah"""

def pl(lst):
    """Fungsi untuk melakukan print sebuah list"""
    print(*lst, sep="\n")

def pr(kalimat, panjang = 0, perataan = 'l', pengisi = ' '):
    """Fungsi untuk melakukan print sebuah kalimat dengan mengatur perataannya"""
    if perataan == 'l' or perataan == 'left' or perataan == 'kiri':
        print(kalimat, pengisi * max(0, panjang - len(kalimat)))
    elif perataan == 'm' or perataan == 'middle' or perataan == 'tengah':
        print(pengisi * max(0, (panjang - len(kalimat) + 1)//2), kalimat, pengisi * max(0, (panjang - len(kalimat))//2))
    elif perataan == 'r' or perataan == 'right' or perataan == 'kanan':
        print(pengisi * max(0, panjang - len(kalimat)), kalimat)