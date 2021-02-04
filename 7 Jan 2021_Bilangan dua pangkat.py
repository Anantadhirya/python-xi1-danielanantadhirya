# cara logaritma
import math
N = int(input())
print("ya" if N >= 0 and math.log2(N) % 1 == 0 else "bukan")

# cara loop
# N = int(input())
# while N > 1 :
#     if N % 2 == 1 :
#         print("bukan")
#         break
#     else :
#         N /= 2
# else :
#     print("ya" if N >= 1 else "bukan")

# cara rekursif
# def bdp(x) :
#     if x <= 0 : return False
#     if x == 1 : return True
#     if x % 2 == 1 : return False
#     else : return bdp(x/2)
#     
# N = int(input())
# print("ya" if bdp(N) else "bukan")
