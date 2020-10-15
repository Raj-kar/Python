def encrypt(msg, shift):
    res = ""
    for letter in msg:
        res += chr(ord(letter) + shift)
    print(res)


encrypt("raj@+%", 5)


def decrypt(msg, shift):
    res = ""
    for letter in msg:
        res += chr(ord(letter) - shift)
    print(res)


decrypt("wfoE0*", 5)