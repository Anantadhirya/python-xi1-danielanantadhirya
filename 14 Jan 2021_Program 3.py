def hitung_FPB(x, y) :
    if x == 0 : return y
    return hitung_FPB(y % x, x)

num1 = 106
num2 = 24

print("FPB dari {} dan {} = {}".format(num1, num2, hitung_FPB(num1, num2)))