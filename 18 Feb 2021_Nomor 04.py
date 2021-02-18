vowels = "aiueo"
ip_str = "Halo nama saya sopan setiawan, saya sedang belajar python"
ip_str = ip_str.casefold()
count = {}.fromkeys(vowels, 0)

for i in ip_str:
    if i in count:
        count[i] += 1

print(count)