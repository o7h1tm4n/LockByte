from core.kdf import derive_key
from core.cipher import decrypt_aes_cbc
from core.integrity import verify_hmac
from utils.file_handler import read_encrypted_file
from utils.cli import get_password

def main():
    input_file = input("Enter encrypted file: ")
    output_file = input("Output file name: ")
    password = get_password()
    
    salt, iv, ciphertext, stored_hmac = read_encrypted_file(input_file)
    
    key = derive_key(password, salt)
    
    if not verify_hmac(key, ciphertext, stored_hmac):
        print("Error: Wrong password or corrupted file!")
        return
    
    plaintext = decrypt_aes_cbc(key, iv, ciphertext)
    
    with open(output_file, 'wb') as f:
        f.write(plaintext)
    
    print("Decryption complete!")

if __name__ == "__main__":
    main()