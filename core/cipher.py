from Crypto.Cipher import AES

def encrypt_aes_cbc(key: bytes, iv: bytes, plaintext: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pad_len = AES.block_size - (len(plaintext) % AES.block_size)
    plaintext = plaintext + bytes([pad_len]) * pad_len
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

def decrypt_aes_cbc(key: bytes, iv: bytes, ciphertext: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)
    pad_len = plaintext[-1]
    return plaintext[:-pad_len]