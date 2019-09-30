#!/usr/bin/python3
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def get_primes(count):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
              43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]

    return(primes[0:count])


with open('plain.txt', 'rb') as f:
    plaintext = f.read()

iv = ""
for i in get_primes(16):
    iv += chr(plaintext[i + 16])

print(iv)
key = b"\xba\xda\x55 HackerMan \x13\x37"  # <----- DESTROY AFTER USE

cipher = AES.new(key, AES.MODE_CBC, IV=iv.encode('utf-8'))
ciphertext_b64 = b64encode(cipher.encrypt(
    pad(plaintext, 32))).decode('utf-8')
print(ciphertext_b64)
