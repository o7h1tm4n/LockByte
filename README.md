# LockByte

LockByte is a command-line encryption tool that secures any file using a user-provided password. It implements AES-256-CBC for data confidentiality, HMAC-SHA256 for integrity verification, and SHA-256 key stretching with 10,000 iterations for secure key derivation. Decryption is only possible with the correct password.


## Installation Req

pip install pycryptodome

## Usage

## Usage

**Encrypt:**
1. Run `python encrypt.py`
2. Enter file to encrypt
3. Enter output name
4. Enter password

**Decrypt:**
1. Run `python decrypt.py`
2. Enter encrypted file
3. Enter output name
4. Enter password


   
## License

GPL-3.0


o7
