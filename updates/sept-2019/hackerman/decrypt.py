#!/usr/bin/python3
from base64 import b64decode
from Crypto.Cipher import AES

ciphertext_b64 = "/lb0WZDpaIDJVJwy+Q04LCqERqVj7AUItWGREJuXJeWtZN77yP6grehn1gRif31hjTEjLNFyxESweea81/QluWUyhZV9vmabm8NYkkSc6JJWuylGJKQJzA/wC2cM2ScrQQ8gV7GcnVyBCh7eq/N0jUm/L4xrX6IUIDi5CAkVZ9xSS5Tb4o01onOTbGWLd1EZwzZOMlq88wsTPZ6zY7dqj+LKq3Pj6SKlZfaR9eo6PXrRUOARCe9sQVtWVKc5DJfI"
key = b"\xba\xda\x55 HackerMan \x13\x37"

ciphertext = b64decode(ciphertext_b64)
iv = ciphertext[:16]

cipher = AES.new(key, AES.MODE_CBC, IV=iv)

plaintext = cipher.decrypt(ciphertext[AES.block_size:]).decode('utf-8')

print(plaintext)
