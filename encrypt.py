from Crypto.Cipher import AES, ARC4
from Crypto.Util.Padding import pad

plaintext = b"this is the wireless security lab"
aes_padded = pad(plaintext, AES.block_size)

# Encrypt with 128-bit AES (16*8 = 128)
aes_key = b"1"*16
aes_cipher = AES.new(aes_key, AES.MODE_ECB)

print(f"AES {len(aes_key)*8}-bit:")
print(aes_cipher.encrypt(aes_padded))

# Encrypt with 40-bit RC4
rc4_key = b"1"*5
rc4_cipher = ARC4.new(rc4_key)

print(f"RC4 {len(rc4_key)*8}-bit:")
print(rc4_cipher.encrypt(plaintext))
