def jml(x):
    return x if x <= 1 else x + jml(x-1)

bil = int(input('input bilangan : '))

if bil < 0:
    print('Masukkan bilangan positif')
else:
    print('Penjumlahan dari nilai asli {} adalah {}'.format(bil, jml(bil)))