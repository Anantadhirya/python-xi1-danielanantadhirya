def pangkat(a, b):
    return 1 if b == 0 else a * pangkat(a, b-1)

x = int(input())
y = int(input())
print(pangkat(x, y))