my_str = "kasur ini rusak"

my_str = my_str.casefold()

print("kalimat ini {} palindrome".format("adalah" if my_str == my_str[::-1] else "bukan"))