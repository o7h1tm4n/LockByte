import hashlib                                 

def derive_key(password: str, salt: bytes, iterations: int = 10000) -> bytes:

    key = password.encode()                    
    key = key + salt                           
    for i in range(iterations):                
        key = hashlib.sha256(key).digest()    
    
    return key                                