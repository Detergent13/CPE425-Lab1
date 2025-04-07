from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

plaintext = b"repeat repeat repeat repeat repeat repeat repeat repeat repeat repeat repeat repeat repeat repeat repeat repeat repeat repeat repeat repeat repeat repeat repeat repeat repeat repeat repeat repeat repeat repeat repeat repeat repeat repeat repeat repeat repeat repeat repeat repeat repeat repeat repeat repeat repeat repeat repeat repeat repeat repeat"
plaintext = pad(plaintext, AES.block_size)

# Change mode here
cipher = AES.new(b"1"*16, AES.MODE_ECB)

ciphertext = cipher.encrypt(plaintext)

print(f"AES {len(b'1'*16)*8}-bit:")
print(ciphertext)