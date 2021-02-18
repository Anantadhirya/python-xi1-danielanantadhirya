import itertools, random

deck = list(itertools.product(range(1,14),["kriting", "hati", "wajik", "sekop"]))

random.shuffle(deck)
print("kamu mendapat: ")
for i in deck[:5]:
    print("{} dari {}".format(i[0], i[1]))