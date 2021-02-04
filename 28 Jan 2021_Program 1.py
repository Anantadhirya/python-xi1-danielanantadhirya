def konversi(x):
    return "{}{}".format(konversi(x//2), x%2) if x > 1 else x % 2

desimal = int(input("input nilai desimal: "))
print(konversi(desimal))