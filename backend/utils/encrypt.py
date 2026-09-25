import bcrypt


def hash_password(password: str) -> str:

    bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)

    return hash

def check_passwork(user_password: str, password: str) -> bool:

    user_bytes = user_password.encode("utf-8")
    user_salt = bcrypt.gensalt()
    user_hash = bcrypt.hashpw(user_bytes, user_salt)

    bytes = password.encode("utf-8")
    
    result = bcrypt.checkpw(user_hash, bytes)

    return result