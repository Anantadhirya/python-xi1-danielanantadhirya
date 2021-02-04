num = int(input("Masukkan bilangan: "))
print("Faktor dari", num, "adalah:")
print(*[i for i in range(1, num + 1) if num % i == 0], sep="\n")
