import bcrypt


async def hash_secret_key(key: str) -> bytes:
    """
    Hash secret key.
    
    :param key: The secret key to hash
    :type key: str
    :return: Hashed secret key.
    """
    key = bytes(key, "utf-8")
    hashed_key = bcrypt.hashpw(key, bcrypt.gensalt())
    return hashed_key


async def is_valid_secret_key(raw_key: str, hashed_key) -> bool:
    """
    Checks if raw key is the same as hashed key.
    
    :param raw_key: Secret key that you want to check against hashed key
    :type raw_key: str
    :param hashed_key: Hashed secret key that you want to check against
    :return: Boolean value.
    """
    raw_key = bytes(raw_key, "utf-8")
    return bcrypt.checkpw(raw_key, hashed_key)
