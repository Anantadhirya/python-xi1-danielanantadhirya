import math
num = int(input("Masukkan bilangan: "))
print(num, "bilangan prima" if num > 1 and all(num % i != 0 for i in range(2, math.ceil(num**0.5)+1)) else "bukan bilangan prima")
