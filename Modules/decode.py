def cipher(word, key = 0):
    ret = ""
    for i in word:
        if 0 <= ord(i) - ord('a') and ord(i) - ord('a') < 26:
            ret += chr((ord(i)-ord('a')+key)%26 + ord('a'))
        elif 0 <= ord(i) - ord('A') and ord(i) - ord('A') < 26:
            ret += chr((ord(i)-ord('a')+key)%26 + ord('A'))
        else:
            ret += i
    return ret

def all_cipher(word, search_word = ""):
    ret = []
    for i in range(26):
        ciphered_word = cipher(word, i)
        if search_word in ciphered_word:
            ret.append(ciphered_word)
    return ret

from fp import pr
panjang = 41
pr('', panjang)
pr('=' * panjang)
pr('Daftar Perintah', panjang, 'm')
pr('- cipher(word, key)', panjang)
pr('- cipher_all(word, search_word)', panjang)
pr('=' * panjang)
pr('', panjang)