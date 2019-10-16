#!/usr/bin/python3
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import sys

ciphertext_b64 = "/lb0WZDpaIDJVJwy+Q04LCqERqVj7AUItWGREJuXJeWtZN77yP6grehn1gRif31hjTEjLNFyxESweea81/QluWUyhZV9vmabm8NYkkSc6JJWuylGJKQJzA/wC2cM2ScrQQ8gV7GcnVyBCh7eq/N0jUm/L4xrX6IUIDi5CAkVZ9xSS5Tb4o01onOTbGWLd1EZwzZOMlq88wsTPZ6zY7dqj+LKq3Pj6SKlZfaR9eo6PXrRUOARCe9sQVtWVKc5DJfI"
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
