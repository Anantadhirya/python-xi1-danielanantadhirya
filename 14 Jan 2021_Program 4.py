def print_faktor(x):
    print("Faktor dari {} adalah :".format(x))
    print(*[i for i in range(1, x + 1) if x % i == 0], sep = "\n")

print_faktor(int(input("Masukkan bilangan : ")))