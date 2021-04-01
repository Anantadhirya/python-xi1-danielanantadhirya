import os
from datetime import datetime
jadwal = []
list_jam = []
jam_aktif = 0
jam = []

class day:
    jam = datetime.now()
    hari = datetime.now().weekday()
    jp = 0
    jpid = 0
    mapel = []
    jadwal = []
    mulai = 0
    selesai = 0
    status = ""

today = day()

kode = {'Upacara':'UPCR', 'Fisika':'FIS', 'Matematika Minat':'MTKP', 'Biologi':'BIO',
        'Agama':'AGM', 'PJOK':'PJOK', 'PPKn':'PPKN', 'Bahasa Inggris':'BING',
        'Bahasa Jawa':'BJW', 'Seni Budaya':'SNB', 'Sejarah Indonesia':'SJI',
        'Informatika':'INF', 'Matematika Wajib':'MTKW', 'PKWU':'PKWU', 'Kimia':'KIM',
        'Bahasa Indonesia':'BIND'}
kode_hari = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']

def open_file():
    global jam_aktif, jam
    with open('C:/Users/Anantadhirya/Downloads/Tugas/Kelas XI/python-xi1-danielanantadhirya/Program/data_jadwal.txt', 'r') as data:
        isi = data.read().split('\n\n')
        for i in isi[0].split('\n'):
            tmp2 = i.split('|')
            jadwal.append([tuple(j.split(':')) for j in tmp2])
        for i in range(len(jadwal)):
            for j in range(len(jadwal[i])):
                jadwal[i][j] = (jadwal[i][j][0], int(jadwal[i][j][1]), int(jadwal[i][j][2]))
        
        jam_aktif = int(isi[1])

        for i in isi[2:]:
            list_jam.append([])
            for j in i.split('\n'):
                tmp2 = j.split('|')
                list_jam[-1].append([tuple(datetime.strptime('{}:00'.format(l), '%H:%M:%S') for l in k.split('-')) for k in tmp2])
        jam = list_jam[jam_aktif]

def save_file():
    with open('C:/Users/Anantadhirya/Downloads/Tugas/Kelas XI/python-xi1-danielanantadhirya/Program/data_jadwal.txt', 'w') as data:
        for baris in jadwal:
            for idx, pelajaran in enumerate(baris):
                data.write("{}:{}:{}".format(pelajaran[0], pelajaran[1], pelajaran[2]))
                if idx != len(baris) - 1: data.write('|')
            data.write('\n')
        data.write('\n')
        for idx2, baris in enumerate(jam):
            for idx, tjp in enumerate(baris):
                data.write("{}:{}-{}:{}".format(tjp[0].hour, tjp[0].minute, tjp[1].hour, tjp[1].minute))
                if idx != len(baris)-1: data.write('|')
            if idx2 != len(jam)-1: data.write('\n')

def clear():
    os.system('cls')
    # print("\n"*100)

def update():
    global today, jam
    jam = list_jam[jam_aktif]
    today.jam = datetime.now()
    today.hari = datetime.now().weekday()
    today.jp = 0
    today.jpid = -1
    today.mapel = jadwal[today.hari]
    today.jadwal = jam[today.hari]
    today.mulai = today.jadwal[0][0]
    today.selesai = today.jadwal[today.mapel[-1][2] - 1][1]
    if today.hari >= 5:
        today.status = "libur"
    elif cmp(today.jam, today.mulai) == 1:
        today.status = "belum mulai"
    elif cmp(today.jam, today.selesai) == -1:
        today.status = "sudah pulang"
    else:
        today.status = "pelajaran"
        today.jp = 1
        while cmp(today.jam, today.jadwal[today.jp-1][1]) == -1:
            today.jp += 1
        today.jpid = 0
        while today.jp > today.mapel[today.jpid][2]:
            today.jpid += 1
        if not (cmp(today.jam, today.jadwal[today.jp-1][0]) <= 0 and cmp(today.jam, today.jadwal[today.jp-1][1]) >= 0):
            today.status = "istirahat"
    return

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

def center_str(string, length = 0):
    return ' ' * max(0, (length-len(string))//2) + string + ' ' * max(0, (length-len(string)+1)//2)

def print_jadwal():
    nomer = 10
    max_len = 7
    for hari in kode_hari[:5]:
        max_len = max(max_len, len(hari))
    for hari in kode.values():
        max_len = max(max_len, max([len(mapel) for mapel in hari]))
    max_len += 2
    final_len = max_len*(nomer+1) + (nomer+2)
    
    print('/' + '-' * (final_len-2) + '\\')
    temp = '|' + ' ' * max_len + '|'
    for i in range(1, nomer+1):
        temp += center_str(str(i), max_len) + '|'
    print(temp)
    for idx, hari in enumerate(jadwal):
        print('|' + '-' * (final_len-2) + '|')
        temp = '|' + center_str(str(kode_hari[idx]), max_len) + '|'
        for mapel in hari:
            temp += center_str(kode[mapel[0]], (max_len+1) * (mapel[2]-mapel[1]+1) - 1) + '|'
        while(len(temp) < final_len):
            temp += ' '*(final_len-len(temp)-1) + '|'
        print(temp)
    print('\\' + '-' * (final_len-2) + '/')

def sekarang():
    print('Sekarang hari {}, jam {}'.format(kode_hari[today.hari], today.jam.strftime('%H:%M:%S')))
    if today.status == "libur":
        print("Tidak ada pelajaran hari ini")
    elif today.status == "belum mulai":
        print("Pelajaran hari ini belum mulai")
    elif today.status == "sudah pulang":
        print("Pelajaran hari ini sudah selesai")
    elif today.status == "istirahat":
        print("Saat ini istirahat ({}-{})".format(today.jadwal[today.jp-2][1].strftime('%H:%M'), today.jadwal[today.jp-1][0].strftime('%H:%M')))
    elif today.status == "pelajaran":
        print("Saat ini jam pelajaran ke {}".format(today.jp))
        print("Mapel: {} ({}-{})".format(today.mapel[today.jpid][0].upper(), today.jadwal[today.mapel[today.jpid][1]-1][0].strftime('%H:%M'), today.jadwal[today.mapel[today.jpid][2]-1][1].strftime('%H:%M')))
        durasi_jam, durasi_menit = delta_time(today.jam, today.jadwal[today.mapel[today.jpid][2]-1][1])
        print("Keterangan: {}{} menit lagi selesai".format('{} jam '.format(durasi_jam) if durasi_jam > 0 else '', durasi_menit))
    print()

def pelajaran_selanjutnya():
    print('Sekarang hari {}, jam {}'.format(kode_hari[today.hari], today.jam.strftime('%H:%M:%S')))
    if today.status == "libur":
        print("Tidak ada pelajaran hari ini")
    elif today.status == "sudah pulang":
        print("Pelajaran hari ini sudah selesai")
    else:
        if today.jpid == len(today.mapel) - 1:
            print("Pelajaran selanjutnya sudah habis")
            durasi_jam, durasi_menit = delta_time(today.jam, today.selesai)
            print("Keterangan: {}{} menit lagi pulang".format('{} jam '.format(durasi_jam) if durasi_jam > 0 else '', durasi_menit))
        else:
            print("Pelajaran selanjutnya mapel {} ({}-{})".format(today.mapel[today.jpid+1][0].upper(), today.jadwal[today.mapel[today.jpid+1][1]-1][0].strftime('%H:%M'), today.jadwal[today.mapel[today.jpid+1][2]-1][1].strftime('%H:%M')))
            durasi_jam, durasi_menit = delta_time(today.jam, today.jadwal[today.mapel[today.jpid+1][1]-1][0])
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
    clear()
    update()
    if tmp == 'jadwal' or tmp == 'j':
        print_jadwal()
    elif tmp == 'next' or tmp == 'n':
        pelajaran_selanjutnya()
    elif tmp == 'sekarang' or tmp == 's':
        sekarang()
    else:
        break
