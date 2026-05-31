def write_encrypted_file(filename: str, salt: bytes, iv: bytes, ciphertext: bytes, hmac_tag: bytes) -> None:
    with open(filename, 'wb') as f:
        f.write(salt)
        f.write(iv)
        f.write(ciphertext)
        f.write(hmac_tag)

def read_encrypted_file(filename: str):
    with open(filename, 'rb') as f:
        salt = f.read(16)
        iv = f.read(16)
        rest = f.read()
        ciphertext = rest[:-32]
        hmac_tag = rest[-32:]
    return salt, iv, ciphertext, hmac_tag