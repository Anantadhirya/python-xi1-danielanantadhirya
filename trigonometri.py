from math import *
print("menentukan nilai sin, cos, dan tan dari 0 - 360 derajat")
print ("sudut\tsin\tcos\ttan")
selisih = 30
sudut = [radians(i) for i in range(0, 360+1, selisih)]
print(*["{:.0f}\t{:.2f}\t{:.2f}\t{:.2f}".format(degrees(x), sin(x), cos(x), tan(x)) for x in sudut], sep="\n")
