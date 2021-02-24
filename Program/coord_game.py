import random
import os
x = 40
y = 20
margin = 2
posisi_x = 0
posisi_y = 0
tebakan_x = 0
tebakan_y = 0
lst_akurasi = []

def setup():
    global x
    global y
    print("Daftar preset: ")
    print("Very small (ss) = 20 x 10")
    print("Small      (s) = 40 x 20")
    print("Medium     (m) = 120 x 40")
    print("Large      (l) = 200 x 50")
    print("Custom     (c) = bebas")
    tmp = input("Preset yang akan digunakan: ").casefold()
    if tmp == 'very small' or tmp == 'ss':
        x, y = 20, 10
    elif tmp == 'small' or tmp == 's':
        x, y = 40, 20
    elif tmp == 'medium' or tmp == 'm':
        x, y = 120, 40
    elif tmp == 'large' or tmp == 'l':
        x, y = 200, 50
    elif tmp == 'custom' or tmp == 'c':
        x = int(input("Ukuran horizontal: "))
        while x <= 0:
            os.system("cls")
            print("Error, ukuran horizontal harus lebih dari 0")
            x = int(input("Ukuran horizontal: "))
        
        y = int(input("Ukuran vertikal: "))
        while y <= 0:
            os.system("cls")
            print("Error, ukuran vertikal harus lebih dari 0")
            print("Ukuran horizontal: {}".format(x))
            y = int(input("Ukuran vertikal: "))
    else:
        print("Preset tidak diketahui")
    standby()

def tebak():
    global tebakan_x, tebakan_y
    print("Tebakan harus bernilai antara 0 - 100")
    tebakan_x = float(input("Masukkan tebakan x: "))
    while tebakan_x < 0 or tebakan_x > 100:
        os.system("cls")
        gambar()
        print("Error, tebakan harus bernilai antara 0 - 100")
        tebakan_x = float(input("Masukkan tebakan x: "))
    tebakan_y = float(input("Masukkan tebakan y: "))
    while tebakan_y < 0 or tebakan_y > 100:
        os.system("cls")
        gambar()
        print("Error, tebakan harus bernilai antara 0 - 100 (tanpa %)")
        print("Masukkan tebakan x: {}".format(tebakan_x))
        tebakan_y = float(input("Masukkan tebakan y: "))

def clip(p, lower, upper):
    return lower if p < lower else upper if p > upper else p

def gambar():
    tempx = -1 if tebakan_x == -1 else clip(round(x * tebakan_x / 100.0), 1, x)
    tempy = -1 if tebakan_y == -1 else clip(round(y * tebakan_y / 100.0), 1, y)
    print('+', '-'*x, '+', sep='')
    for i in range(1, y+1):
        if i != posisi_y and i != tempy:
            print('|', ' '*x, '|', sep='', end='')
        else:
            print('|', end='')
            for j in range(1, x+1):
                if j == tempx and i == tempy:
                    print('X', end='')
                elif j == posisi_x and i == posisi_y:
                    print('P', end='')
                else:
                    print(' ', end='')
            print('|', end='')
        if i == 1:
            print(" y = 0%", end='')
        elif i == y:
            print(" y = 100%", end='')
        print()
    print('+', '-'*x, '+', sep='')
    print(' x = 0%', ' '*(x-14), 'x = 100% ', sep='')

def hitung_akurasi():
    miss_x = abs(posisi_x - clip(round(x * tebakan_x / 100.0), 1, x))
    miss_y = abs(posisi_y - clip(round(y * tebakan_y / 100.0), 1, y))
    miss = (miss_x**2 + miss_y**2)**0.5
    max_miss = (x**2 + y**2)**0.5
    return 100.0 - miss/max_miss * 100.0
    
def start():
    global posisi_x, posisi_y, tebakan_x, tebakan_y
    os.system("cls")
    posisi_x = random.randint(1 + margin, x - margin)
    posisi_y = random.randint(1 + margin, y - margin)
    tebakan_x = -1
    tebakan_y = -1
    gambar()
    tebak()
    os.system("cls")
    gambar()
    akurasi = hitung_akurasi()
    lst_akurasi.append(akurasi)
    print("Akurasi: {:.2f}".format(akurasi))
    standby()

def standby():
    print("Daftar Perintah:")
    print("- 'start' atau 's' untuk mulai")
    print("- 'hasil' atau 'h' untuk melihat akurasi")
    print("- 'setup' untuk melakukan pengaturan")
    print("- 'stop' untuk menghentikan permainan")
    tmp = input(">>> ").casefold()
    if tmp == 'start' or tmp == 's':
        start()
    elif tmp == 'hasil' or tmp == 'h':
        lihat_akurasi()
    elif tmp == 'setup':
        setup()
    elif tmp == 'stop':
        os.system('cls')
    else:
        standby()

def lihat_akurasi():
    os.system('cls')
    if len(lst_akurasi) == 0:
        print("Belum ada data akurasi permainan")
    else:
        print("Akurasi rata-rata: {:.2f}".format(sum(lst_akurasi)/len(lst_akurasi)))
        print(lst_akurasi)
    standby()

standby()