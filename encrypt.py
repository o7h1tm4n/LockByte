import os
from core.kdf import derive_key
from core.cipher import encrypt_aes_cbc
from core.integrity import compute_hmac
from utils.file_handler import write_encrypted_file
from utils.cli import get_password

def main():
    input_file = input("Enter file to encrypt: ")
    output_file = input("Output file name: ")
    password = get_password()
    
    salt = os.urandom(16)
    iv = os.urandom(16)
    
    key = derive_key(password, salt)
    
    with open(input_file, 'rb') as f:
        plaintext = f.read()
    
    ciphertext = encrypt_aes_cbc(key, iv, plaintext)
    
    hmac_tag = compute_hmac(key, ciphertext)
    
    write_encrypted_file(output_file, salt, iv, ciphertext, hmac_tag)
    
    print("Encryption complete!")

if __name__ == "__main__":
    main()