# Banyaknya faktor positif dari 2^4.3^4.7^4 yang lebih dari 2^2.3^2.7^2 adalah …
# a) 62
# b) 63
# c) 64
# d) 65
# e) 66

# 2^a . 3^b . 4^c
def hitung(a,b,c):
    return 2**a * 3**b * 7**c

import itertools
jawaban = []
cnt = 0
for a,b,c in itertools.product(range(4+1), repeat=3):
    if hitung(a,b,c) > hitung(2,2,2):
        cnt += 1
        jawaban.append((a,b,c))

print(cnt)
print(*jawaban, sep='\n')