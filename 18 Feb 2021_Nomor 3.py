def compute_hcf(x,y):
    if x == 0: return y
    return compute_hcf(y%x, x)

num1 = 54
num2 = 24
print("Nilai H.C.F dari {} dan {} adalah {}".format(num1, num2, compute_hcf(num1,num2)))