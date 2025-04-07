import binascii
import time
from itertools import product

from Crypto.Cipher import AES, ARC4
from Crypto.Util.Padding import pad
from string import ascii_lowercase, digits

MODE = "aes"
ALPHABET = ascii_lowercase + digits
plaintext = b"this is the wireless security lab"

# From encrypt.py
aes_ciphertext = b';[\xb5\x90\xb3\x93\x91F\xf6gF)\x11\x0e\xce\xa3\x1a\xb3\x9c\xae~\xb8O3\x9d\x875\x9eV\xe1\xa1\x05p\x8a\x0e|L`\xb7]\xacf|b-\x87\xeao'
rc4_ciphertext = b'\x14r\xab\x1e\xb7.\x99R\x00Tx\x9d=\x0e\xd2\x91:\x949nO\\\x17P\x13\xca\xca\x9f\xdc\x1ce\xd2^'

key_len = 16 if MODE == "aes" else 5

encrypted = binascii.hexlify(aes_ciphertext).decode() if MODE == "aes" else binascii.hexlify(rc4_ciphertext).decode()

print(f"Encrypted: {encrypted}")

count = 0
stime = time.time()
# Brute force the key
for key in product(ALPHABET, repeat=key_len):
    key = ''.join(key).encode()
    count += 1
    if count % 1000000 == 0:
        print(f"Progress: {count} keys tried. Current key: {key.decode()}")

    if MODE == "aes":
        aes_cipher = AES.new(key, AES.MODE_ECB)
        aes_padded = pad(plaintext, AES.block_size)
        if aes_cipher.encrypt(aes_padded) == aes_ciphertext:
            print(f"AES key found: {key}")
            break
    elif MODE == "rc4":
        rc4_cipher = ARC4.new(key)
        if rc4_cipher.encrypt(plaintext) == rc4_ciphertext:
            print(f"RC4 key found: {key}, ")
            break

etime = time.time()
print(f"Time taken: {etime - stime} seconds")
