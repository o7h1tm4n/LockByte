import hashlib
import hmac

def compute_hmac(key: bytes, data: bytes) -> bytes:
    cipher_hmac = hmac.new(key, data, hashlib.sha256)
    return cipher_hmac.digest()

def verify_hmac(key: bytes, data: bytes, tag: bytes) -> bool:
    expected = compute_hmac(key, data)
    return hmac.compare_digest(expected, tag)