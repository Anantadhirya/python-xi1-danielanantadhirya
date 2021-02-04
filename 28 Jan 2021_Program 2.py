def f(x):
    return x * f(x-1) if x > 0 else 1

bil = int(input('input bilangan : '))

if bil < 0:
    print('faktorial hanya untuk nilai positif')
else:
  print('faktorial dari {} adalah {}'.format(bil, f(bil)))
