import os
from datetime import datetime
jadwal = []
jam = []

kode = {'Upacara':'UPCR', 'Fisika':'FIS', 'Matematika Minat':'MTKP', 'Biologi':'BIO',
        'Agama':'AGM', 'PJOK':'PJOK', 'PPKn':'PPKN', 'Bahasa Inggris':'BING',
        'Bahasa Jawa':'BJW', 'Seni Budaya':'SNB', 'Sejarah Indonesia':'SJI',
        'Informatika':'INF', 'Matematika Wajib':'MTKW', 'PKWU':'PKWU', 'Kimia':'KIM',
        'Bahasa Indonesia':'BIND'}
hari = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']

def clear():
    os.system('cls')

def get_jp():
    jp = 1
    while cmp(datetime.now(), jam[datetime.now().weekday()][jp-1][1]) == -1:
        jp += 1
    return jp

def cmp(time1, time2):
    if time1.hour > time2.hour:
        return -1
    elif time1.hour < time2.hour:
        return 1
    else:
        if time1.minute > time2.minute:
            return -1
        elif time1.minute < time2.minute:
            return 1
        else:
            if time1.second > time2.second:
                return -1
            elif time1.second < time2.second:
                return 1
            else:
                return 0

def delta_time(time1, time2):
    if cmp(time1, time2) == -1: time1, time2 = time2, time1
    if time2.minute >= time1.minute:
        return (time2.hour - time1.hour, time2.minute - time1.minute)
    else:
        return (time2.hour - time1.hour - 1, time2.minute - time1.minute + 60)

def open_file():
    with open('C:/Users/Anantadhirya/Downloads/Tugas/Kelas XI/python-xi1-danielanantadhirya/Program/data_jadwal.txt', 'r') as data:
        isi = data.read().split('\n')
        for i in isi[:5]:
            tmp2 = i.split('|')
            jadwal.append([tuple(j.split(':')) for j in tmp2])
        for i in range(len(jadwal)):
            for j in range(len(jadwal[i])):
                jadwal[i][j] = (jadwal[i][j][0], int(jadwal[i][j][1]), int(jadwal[i][j][2]))
        for i in isi[6:11]:
            tmp2 = i.split('|')
            jam.append([tuple(datetime.strptime('{}:00'.format(k), '%H:%M:%S') for k in j.split('-')) for j in tmp2])

def save_file():
    with open('C:/Users/Anantadhirya/Downloads/Tugas/Kelas XI/python-xi1-danielanantadhirya/Program/data_jadwal.txt', 'w') as data:
        for baris in jadwal:
            for pelajaran in baris:
                data.write("{}:{}:{}".format(pelajaran[0], pelajaran[1], pelajaran[2]))
                if pelajaran != baris[-1]: data.write('|')
            if baris != jadwal[-1]: data.write('\n')

def print_jadwal():
    clear()
    arr = [[''], ['Senin'], ['Selasa'], ['Rabu'], ['Kamis'], ['Jumat']]
    for i in range(1, 10+1):
        arr[0].append(str(i))
    for i in range(5):
        tmp2 = 0
        for j in range(1, 10+1):
            if j > jadwal[i][-1][2]:
                arr[i+1].append('')
            else:
                while jadwal[i][tmp2][2] < j:
                    tmp2 += 1
                arr[i+1].append(kode[jadwal[i][tmp2][0]])
    max_len = 7
    for i in arr:
        max_len = max(max_len, max([len(j) for j in i]))
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j] += ' ' * (max_len - len(arr[i][j]))
    for day in arr:
        for pelajaran in day:
            print(pelajaran, end='')
            print('\t', end='')
        print()

def sekarang():
    clear()
    now = datetime.now()
    hari_ini = now.weekday()
    print('Sekarang hari {}, jam {}'.format(hari[hari_ini], now.strftime('%H:%M:%S')))
    if hari_ini >= 5:
        print("Tidak ada pelajaran hari ini")
    else:
        mulai = jam[hari_ini][0][0]
        selesai = jam[hari_ini][jadwal[hari_ini][-1][2]-1][1]
        if cmp(now, mulai) == 1:
            print("Pelajaran hari ini belum mulai")
        elif cmp(now, selesai) == -1:
            print("Pelajaran hari ini sudah selesai")
        else:
            jp = get_jp()
            jp_mulai = jam[hari_ini][jp-1][0]
            jp_selesai = jam[hari_ini][jp-1][1]
            if cmp(jp_mulai, now) >= 0 and cmp(now, jp_selesai) >= 0:
                print("Saat ini jam pelajaran ke {}".format(jp))
                i = 0
                while not(jadwal[hari_ini][i][1] <= jp and jp <= jadwal[hari_ini][i][2]):
                    i += 1
                print("Mapel: {} ({}-{})".format(jadwal[hari_ini][i][0].upper(), jam[hari_ini][jadwal[hari_ini][i][1]-1][0].strftime('%H:%M'), jam[hari_ini][jadwal[hari_ini][i][2]-1][1].strftime('%H:%M')))
            else:
                print("Saat ini istirahat ({}-{})".format(jam[hari_ini][jp-2][1].strftime('%H:%M'), jp_mulai.strftime('%H:%M')))
    print()

def pelajaran_selanjutnya():
    clear()
    now = datetime.now()
    hari_ini = now.weekday()
    print('Sekarang hari {}, jam {}'.format(hari[hari_ini], now.strftime('%H:%M:%S')))
    if hari_ini >= 5:
        print("Tidak ada pelajaran hari ini")
    else:
        selesai = jam[hari_ini][jadwal[hari_ini][-1][2]-1][1]
        if cmp(now, selesai) == -1:
            print("Pelajaran hari ini sudah selesai")
        else:
            i_next = 0
            while i_next < len(jadwal[hari_ini]) and cmp(jam[hari_ini][jadwal[hari_ini][i_next][1]-1][0], now) >= 0:
                i_next += 1
            if i_next == len(jadwal[hari_ini]):
                print("Pelajaran selanjutnya sudah habis")
                durasi_jam, durasi_menit = delta_time(now, selesai)
                print("Keterangan: {}{} menit lagi pulang".format('{} jam '.format(durasi_jam) if durasi_jam > 0 else '', durasi_menit))
            else:
                print("Pelajaran selanjutnya mapel {} ({}-{})".format(jadwal[hari_ini][i_next][0].upper(), jam[hari_ini][jadwal[hari_ini][i_next][1]-1][0].strftime('%H:%M'), jam[hari_ini][jadwal[hari_ini][i_next][2]-1][1].strftime('%H:%M')))
                jam_mulai = jam[hari_ini][jadwal[hari_ini][i_next][1]-1][0]
                durasi_jam, durasi_menit = delta_time(now, jam_mulai)
                print("Keterangan: {}{} menit lagi".format('{} jam '.format(durasi_jam) if durasi_jam > 0 else '', durasi_menit))
    print()

open_file()
while(True):
    print("Daftar Perintah:")
    print("- jadwal (j)")
    print("- next (n)")
    print("- sekarang (s)")
    print("- stop (st)")
    print("Masukkan perintah:")
    tmp = input(">>> ").casefold()
    if tmp == 'jadwal' or tmp == 'j':
        print_jadwal()
    elif tmp == 'next' or tmp == 'n':
        pelajaran_selanjutnya()
    elif tmp == 'sekarang' or tmp == 's':
        sekarang()
    else:
        clear()
        break
