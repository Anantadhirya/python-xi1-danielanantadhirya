import cmath

# ax^2 + bx + c
a = 1
b = 5
c = 6

d = (b**2) - 4*a*c

sol1 = -b-cmath.sqrt(d)/(2*a)
sol2 = -b+cmath.sqrt(d)/(2*a)

print("akar dari {}x^2 + {}x + {} adalah {} dan {}".format(a, b, c, sol1, sol2))