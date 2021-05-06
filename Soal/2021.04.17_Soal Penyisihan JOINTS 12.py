#    A B C D
#    A B C D
# ----------- +
#  D E F G H
# 
# Setiap huruf merepresentasikan 1 bilangan bulat antara 0-9 (inklusif), nilai E < H dan 
# tidak ada 2 huruf berbeda yang merepresentasikan angka yang sama.Nilai dari A x B x C x D = . . .
# a) 84
# b) 90
# c) 105
# d) 160
# e) 175

import itertools
# nilai D hanya antara 0-1
nomer = 1
def prn(ABCD, DEFGH):
    global nomer
    str1 = "      " + " ".join(ABCD)
    str2 = "   ----------- +"
    str3 = "    " + " ".join(DEFGH)
    print(str(nomer) + ".")
    nomer += 1
    print(str1)
    print(str1)
    print(str2)
    print(str3)
    print()

jawaban = []
for abcd in itertools.product(range(10), range(10), range(10), range(2)):
    ABCD = int("".join([str(i) for i in abcd]))
    DEFGH = 2 * ABCD
    ABCD = "{:04d}".format(ABCD)
    DEFGH = "{:05d}".format(DEFGH)
    cnt = {}.fromkeys(range(10), 0)
    for i in ABCD + DEFGH[1:]:
        cnt[int(i)] += 1
    # kalau beda semua dan E < H
    if max(cnt.values()) <= 1 and int(DEFGH[1]) < int(DEFGH[4]):
        prn(ABCD, DEFGH)
        jawaban.append(int(ABCD[0]) * int(ABCD[1]) * int(ABCD[2]) * int(ABCD[3]))

for jawab in jawaban:
    print(jawab)