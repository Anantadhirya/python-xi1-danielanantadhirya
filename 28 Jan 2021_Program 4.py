def f(x):
    return x if x <= 1 else f(x-1) + f(x-2)

deret = int(input('jumlah deret : '))

if deret <= 0:
    print('masukkan bilangan bulat positif')
else:
    print('deret fibonacci : ')
    print(*[f(i) for i in range(deret)], sep = '\n')
