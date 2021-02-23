"""Module untuk melakukan berbagai cipher dan decode"""
import base64

def cipher(word, key = 0):
    """Fungsi untuk melakukan caesar cipher"""
    ret = ""
    for i in word:
        if 0 <= ord(i) - ord('a') and ord(i) - ord('a') < 26:
            ret += chr((ord(i)-ord('a')+key)%26 + ord('a'))
        elif 0 <= ord(i) - ord('A') and ord(i) - ord('A') < 26:
            ret += chr((ord(i)-ord('A')+key)%26 + ord('A'))
        else:
            ret += i
    return ret

def cipher_all(word, search_word = ""):
    """Fungsi untuk mencoba semua kemungkinan dan mencari search word tertentu"""
    ret = []
    for i in range(26):
        ciphered_word = cipher(word, i)
        if search_word in ciphered_word:
            ret.append(ciphered_word)
    return ret