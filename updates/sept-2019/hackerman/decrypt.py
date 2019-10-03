#!/usr/bin/python3
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import sys


def xor(data, key1):
    b = key1
    if type(key1) is str:
        b = bytes(key1, encoding='utf8')

    iData = int.from_bytes(data, sys.byteorder)
    iKey = int.from_bytes(b, sys.byteorder)
    xored = iData ^ iKey
    xored = xored.to_bytes(len(data), sys.byteorder)
    return xored


ciphertext_b64 = "/lb0WZDpaIDJVJwy+Q04LCqERqVj7AUItWGREJuXJeWtZN77yP6grehn1gRif31hjTEjLNFyxESweea81/QluWUyhZV9vmabm8NYkkSc6JJWuylGJKQJzA/wC2cM2ScrQQ8gV7GcnVyBCh7eq/N0jUm/L4xrX6IUIDi5CAkVZ9xSS5Tb4o01onOTbGWLd1EZwzZOMlq88wsTPZ6zY7dqj+LKq3Pj6SKlZfaR9eo6PXrRUOARCe9sQVtWVKc5DJfI"
# ciphertext_b64 = "J5Q9oFJ/O77jdhhNMJbkfd+FkCKqYSlOt/fTYT/1HaPdIIDxo4NmeHofnW4NhWEL8t6ehBc+ZKYZp7pBWFEva0mZhBjbZoMW56c4VwqWPo+i07g2TJIhPGcdLkyTpKnrZyNe6oy8QO5PVK8WQylpXgLJbUCrcecI2laJ4spN/keAMeSN02FsQrDPsmcL45q5zVZBBDisTJxpaHFVenG/5BiM+XU2YU+Xbsixtdzh1gaWEekuaeBCUEbthSDumfUR"
# ciphertext_b64 = "vfpCERjMFBAwlm4EudaOBF5weTn2ydwGzrd9wojpZGKVzSzkbbVfOotF6hfYR9WhBneTwzJ/X8DE9RemQeTvHvAK3leczdZ4OYxzgw+IGDaFCGWazBN0EoJNXQB4UGsJHN258m5TL0LMwB889nSQ0UjknHjpWGgbNkb0919DCY/DOUn5LEz8Vneomw9s2K1G7DxZsxYf15AFLGY1GDrebrFpRHbzXUANKmzlUugG4nchIwb5pwelgGEfgPaPAcS+"
# ciphertext_b64 = "vfpCERjMFBAwlm4EudaOBF5weTn2ydwGzrd9wojpZGKVzSzkbbVfOotF6hfYR9WhBneTwzJ/X8DE9RemQeTvHvAK3leczdZ4OYxzgw+IGDaFCGWazBN0EoJNXQB4UGsJHN258m5TL0LMwB889nSQ0UjknHjpWGgbNkb0919DCY/DOUn5LEz8Vneomw9s2K1G7DxZsxYf15AFLGY1GDreblYK2b3MKmZVKjaRPlFFQp9kti7xSDZTF4BmgTVR+Ti0"
# ciphertext_b64 = "3RAfI2MrcDI6R48Xgl1hcDmNOoH6QJSwOi5dpIbEwpDEtNW5LHCKcmXRTEqMpriw8+/1cezKCZvfTCR7H0NW9JDGWIJ149lQXny64H9FUSlk+pU78wGG9AVrYrNyNUahA+HU8SvfoCT8ITxwzBPCajEyGwmVBuZd0XLG6O28aJ9BrAIT4qk6d3c8osgViKPL58NT1D4P2YaZJ5LweeDkTDOFHYPVMNgDW+3gudCzwWjayc43sLUFc0wa4EfsJw/8"
# ciphertext_b64 = "0yFImXU3oKrDdRmyfnQA1kfBBjIP25Rwo8iTd+A4Eg9mUsb9UfaAdRcYSXTJglNIpd7t/9fRcZiEPdRx7xeo6FH7/yip2GgDUUP58gxP4+jplv292NJu10GdQkFe96LoDVFP8z7RaShUANSsZwezXV6QmEKKNZb3JHf2MLZuOiQjIRPyhZ0ibEdTyPfuJDz5/vkDSlxfinFduDnn/O9bSZia9llBykkGQ4mijTjlPHsJDI97y5uEwaSh0783pD7yZkBH/AKmi5dCeTXovYijdQ=="
key = b"\xba\xda\x55 HackerMan \x13\x37"
iv = b"\x00"*16

ciphertext = b64decode(ciphertext_b64)

# 1. Ser alt etter 'erer! Du...'. Mangler alt foran. Minst 'Gratul' men det blir ikke 16 byte block
# 2. Padder plain.txt (var 'Gratulerer! Du kl...'). Endret til: 'xxxxxxxxxxGratul'
# 3. Får da IV 'er uate!k,mngn i' i encrypt.py
# 4. Bruker ny IV her
#iv = b"er uate!k,mngn i"
cipher = AES.new(key, AES.MODE_CBC, IV=iv)

plaintext = cipher.decrypt(ciphertext)

print(plaintext)
