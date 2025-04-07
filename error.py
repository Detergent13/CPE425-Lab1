from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

plaintext = b"This is my untainted plaintext. It surely will not be modified by any malicious force."
plaintext = pad(plaintext, AES.block_size)

KEY = b"sixteen byte key"
MODE = AES.MODE_CTR
IV = b"1234567890123456"

# ECB/CTR doesn't use an IV.
# CBC needs different ciphersuites for encryption and decryption, since the operations mutate state.
cipher_enc = AES.new(KEY, MODE, IV) if (MODE != AES.MODE_CTR and MODE != AES.MODE_ECB) else AES.new(KEY, MODE)
cipher_dec = AES.new(KEY, MODE, IV) if (MODE != AES.MODE_CTR and MODE != AES.MODE_ECB) else AES.new(KEY, MODE)

ciphertext = cipher_enc.encrypt(plaintext)

print(f"\nOriginal ciphertext:")
print(ciphertext)

# Flip the first bit of the ciphertext (w/ XOR)
tainted = bytearray(ciphertext)
tainted[0] ^= 0b10000000
tainted = bytes(tainted)

print(f"\nTainted ciphertext:")
print(tainted)

print(f"\nDecrypted tainted ciphertext:")
print(cipher_dec.decrypt(tainted))
