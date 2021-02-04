def fpb(a, b):
    return b if a == 0 else fpb(b%a, a)

x, y = [int(i) for i in input().split()]
print(fpb(x, y))