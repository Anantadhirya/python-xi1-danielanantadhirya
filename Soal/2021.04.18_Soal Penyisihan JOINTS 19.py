# Perhatikan deskripsi berikut untuk menjawab 2 soal di bawah!
# Jika didapatkan Hubungan antaran Himpunan A, B, C, D, E, F sebagai berikut:
# (1) Semua C dan F adalah B
# (2) Semua A adalah salah satu dari E atau F
# (3) Tidak ada C yang merupakan A
# (4) Tidak ada D yang merupakan F
# (5) Semua B kecuali C adalah F
# (6) Tidak ada E yang merupakan B
# 
# 19. Jika keenam pernyataan tersebut bernilai benar tentukan pernyataan yang 
# kemungkinan benar di bawah ini, kecuali ….
# a) Ada F yang merupakan C
# b) Ada D yang merupakan B
# c) Beberapa A merupakan B
# d) Tidak ada E yang merupakan C (pasti benar)
# e) Tidak ada C yang merupakan F
# 
# 20. Jika pernyataan kelima salah, manakah yang pernyataan berikut yang harus benar?
# a) Sejumlah A bukanlah F atau pun E
# b) Sejumlah C bukanlah B
# c) Sejumlah B bukanlah F dan C
# d) Sejumlah B bukanlah C atau pun F
# e) Salah satu dari “Beberapa dari F merupakan C”, atau “beberapa dari B bukanlah C 
# ataupun F” adalah benar, dan keduanya benar.

pengganti = {
    'A':'A',
    'B':'manusia',
    'C':'laki-laki',
    'D':'D',
    'E':'E',
    'F':'perempuan'
}

soal ="""(1) semua C dan F adalah B
(2) semua A adalah salah satu dari E atau F
(3) tidak ada C yang merupakan A
(4) tidak ada D yang merupakan F
(5) semua B kecuali C adalah F
(6) tidak ada E yang merupakan B
"""
no19 = """a) ada F yang merupakan C
b) ada D yang merupakan B
c) beberapa A merupakan B
d) tidak ada E yang merupakan C (pasti benar)
e) tidak ada C yang merupakan F
"""

no20 = """a) sejumlah A bukanlah F atau pun E
b) sejumlah C bukanlah B
c) sejumlah B bukanlah F dan C
d) sejumlah B bukanlah C atau pun F
e) salah satu dari “Beberapa dari F merupakan C”, atau “beberapa dari B bukanlah C
"""
print('\n'*100)
for i in "\n\n".join([soal, no19, no20]):
    if i not in "ABCDEF":
        print(i, end='')
    else:
        print(pengganti[i], end='')