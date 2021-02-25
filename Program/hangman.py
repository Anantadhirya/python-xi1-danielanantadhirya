import random
import os
gagal = 0
kata = ""
menang = 0
kalah = 0
count_gagal = []
akurasi = []
daftar_kata = [
    "alphabet",
    "apel hijau",
    "atap rumah",
    "bahasa indonesia",
    "ban mobil",
    "bika ambon",
    "burung garuda",
    "cacing tanah",
    "celana training",
    "dek kartu",
    "ensiklopedia",
    "fenomena alam",
    "handphone",
    "headphone",
    "ikan lele",
    "jas hujan",
    "jendela",
    "jeruk bali",
    "kelapa sawit",
    "kertas hvs",
    "komputer",
    "kotak brankas",
    "kucing oren",
    "lemari baju",
    "matahari",
    "monitor",
    "nasi goreng",
    "obat batuk",
    "pancasila",
    "pelangi",
    "pisang",
    "pramuka",
    "programming",
    "rambutan",
    "semut merah",
    "smartphone",
    "tarian daerah",
    "tas ransel",
    "telur dadar",
    "teras rumah",
    "walkie talkie",
]

def clear():
    os.system('cls')

def setup():
    global daftar_kata
    for i in daftar_kata:
        if len(set(i)) <= 5:
            print("{} -> {}".format(i, len(set(i))))
    if daftar_kata != sorted(daftar_kata):
        print("Daftar kata tidak urut")
    daftar_kata = sorted(daftar_kata)
    max_len = max(len(i) for i in daftar_kata)
    for i in range(len(daftar_kata)):
        daftar_kata[i] = daftar_kata[i].casefold()
        daftar_kata[i] += ' ' * (max_len - len(daftar_kata[i]))

def standby():
    print("Daftar Perintah:")
    print("- 'start' atau 's' untuk mulai")
    print("- 'hasil' atau 'h' untuk melihat statistik")
    print("- 'words' atau 'w' untuk melihat daftar kata")
    print("- 'stop' untuk menghentikan permainan")
    tmp = input(">>> ")
    if tmp == 'start' or tmp == 's':
        start()
    elif tmp == 'hasil' or tmp == 'h':
        hasil()
    elif tmp == 'words' or tmp == 'w':
        word()
    elif tmp == 'stop':
        clear()
    else:
        clear()
        standby()

def word():
    clear()
    kolom = 3
    baris = (len(daftar_kata)+kolom-1)//kolom
    digit_max = len(str(len(daftar_kata) + 1))
    for i in range(baris):
        for j in range(kolom):
            if i + baris*j < len(daftar_kata):
                nomer = i + baris*j+1
                print(' '*(digit_max - len(str(nomer))), "{}. {}".format(nomer, daftar_kata[i+baris*j]), sep='', end='')
            if j == kolom - 1: print("\n", end='')
            else: print("\t", end='')
    print("Jumlah kata: {}".format(len(daftar_kata)))
    print("Panjang rata-rata tiap kata: {:.2f}".format(sum(len(i.strip()) for i in daftar_kata)/len(daftar_kata)))
    cnt = [[0, chr(i + ord('a'))] for i in range(26)]
    for i in daftar_kata:
        for j in i:
            if j.isalpha(): cnt[ord(j) - ord('a')][0] += 1
    print("Huruf paling banyak:", *[i[1].upper() for i in sorted(cnt)[:-6:-1]])
    standby()

def start():
    global kata, gagal, menang, kalah
    gagal = 0
    kata = random.choice(daftar_kata)
    daftar_kata.remove(kata)
    jawaban = [' ']
    while gagal < 11:
        clear()
        gambar()
        for i in kata:
            print('_ ' if i not in jawaban else '{} '.format(i.upper()), end='')
        print()
        print("Tebakan: ", *[i.upper() for i in jawaban[1:]], sep=' ')
        tmp = input("Masukkan tebakan: ").casefold()
        for i in tmp:
            if i in jawaban or not i.isalpha():
                continue
            jawaban.append(i)
            if i not in kata:
                gagal += 1
            if all(i in jawaban for i in kata):
                break
        if all(i in jawaban for i in kata):
            break
    akurasi.append(100.0 - 100.0*gagal/(len(jawaban)-1))
    count_gagal.append(gagal)
    if gagal < 11:
        clear()
        gambar()
        print("Jawaban:", kata.upper())
        print("Selamat anda berhasil!")
        print("Akurasi: {:.2f}%".format(akurasi[-1]))
        menang += 1
    else:
        clear()
        gambar()
        print("Jawaban benar:", kata.upper())
        print("Game Over")
        kalah += 1
    standby()

def hasil():
    clear()
    print("======== Statistik ========")
    print("Menang: {}".format(menang))
    print("Kalah: {}".format(kalah))
    if len(count_gagal) > 0:
        print("Kesalahan rata-rata: {:.2f}".format(sum(count_gagal)/len(count_gagal)))
        print("Akurasi rata-rata: {:.2f}%".format(sum(akurasi)/len(akurasi)))
    else:
        print("Kesalahan rata-rata: -")
        print("Akurasi rata-rata: -")
    print("============================")
    standby()

def gambar():
    if gagal == 0:
        print("+-----------------------+")
        print("|                       |")
        print("|                       |")
        print("|                       |")
        print("|                       |")
        print("|                       |")
        print("|                       |")
        print("|                       |")
        print("|                       |")
        print("|                       |")
        print("+-----------------------+")
    elif gagal == 1:
        print("+-----------------------+")
        print("|                       |")
        print("|                       |")
        print("|                       |")
        print("|                       |")
        print("|                       |")
        print("|                       |")
        print("|                /      |")
        print("|               /       |")
        print("|                       |")
        print("+-----------------------+")
    elif gagal == 2:
        print("+-----------------------+")
        print("|                       |")
        print("|                       |")
        print("|                       |")
        print("|                       |")
        print("|                       |")
        print("|                       |")
        print("|                / \    |")
        print("|               /   \   |")
        print("|                       |")
        print("+-----------------------+")
    elif gagal == 3:
        print("+-----------------------+")
        print("|                       |")
        print("|                 |     |")
        print("|                 |     |")
        print("|                 |     |")
        print("|                 |     |")
        print("|                 |     |")
        print("|                / \    |")
        print("|               /   \   |")
        print("|                       |")
        print("+-----------------------+")
    elif gagal == 4:
        print("+-----------------------+")
        print("|         _________     |")
        print("|                 |     |")
        print("|                 |     |")
        print("|                 |     |")
        print("|                 |     |")
        print("|                 |     |")
        print("|                / \    |")
        print("|               /   \   |")
        print("|                       |")
        print("+-----------------------+")
    elif gagal == 5:
        print("+-----------------------+")
        print("|         _________     |")
        print("|         |       |     |")
        print("|         |       |     |")
        print("|                 |     |")
        print("|                 |     |")
        print("|                 |     |")
        print("|                / \    |")
        print("|               /   \   |")
        print("|                       |")
        print("+-----------------------+")
    elif gagal == 6:
        print("+-----------------------+")
        print("|         _________     |")
        print("|         |       |     |")
        print("|        O|       |     |")
        print("|                 |     |")
        print("|                 |     |")
        print("|                 |     |")
        print("|                / \    |")
        print("|               /   \   |")
        print("|                       |")
        print("+-----------------------+")
    elif gagal == 7:
        print("+-----------------------+")
        print("|         _________     |")
        print("|         |       |     |")
        print("|        O|       |     |")
        print("|        |        |     |")
        print("|        |        |     |")
        print("|                 |     |")
        print("|                / \    |")
        print("|               /   \   |")
        print("|                       |")
        print("+-----------------------+")
    elif gagal == 8:
        print("+-----------------------+")
        print("|         _________     |")
        print("|         |       |     |")
        print("|        O|       |     |")
        print("|       /|        |     |")
        print("|        |        |     |")
        print("|                 |     |")
        print("|                / \    |")
        print("|               /   \   |")
        print("|                       |")
        print("+-----------------------+")
    elif gagal == 9:
        print("+-----------------------+")
        print("|         _________     |")
        print("|         |       |     |")
        print("|        O|       |     |")
        print("|       /|\       |     |")
        print("|        |        |     |")
        print("|                 |     |")
        print("|                / \    |")
        print("|               /   \   |")
        print("|                       |")
        print("+-----------------------+")
    elif gagal == 10:
        print("+-----------------------+")
        print("|         _________     |")
        print("|         |       |     |")
        print("|        O|       |     |")
        print("|       /|\       |     |")
        print("|        |        |     |")
        print("|       /         |     |")
        print("|                / \    |")
        print("|               /   \   |")
        print("|                       |")
        print("+-----------------------+")
    elif gagal == 11:
        print("+-----------------------+")
        print("|         _________     |")
        print("|         |       |     |")
        print("|        O|       |     |")
        print("|       /|\       |     |")
        print("|        |        |     |")
        print("|       / \       |     |")
        print("|                / \    |")
        print("|               /   \   |")
        print("|                       |")
        print("+-----------------------+")

setup()
standby()
