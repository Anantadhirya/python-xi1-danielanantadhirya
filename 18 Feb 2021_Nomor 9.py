def compute_lcm(x, y):
    greater = max(x, y)
    while(1):
        if greater % x == 0 and greater % y == 0:
            lcm = greater
            break
        greater += 1
    return lcm

num1 = 12
num2 = 20

print("nilai KPK adalah ", compute_lcm(num1, num2))