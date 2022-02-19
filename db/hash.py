import bcrypt


async def hash_secret_key(key: str) -> str:
    key = bytes(key, "utf-8")
    hashed_key = bcrypt.hashpw(key, bcrypt.gensalt())
    return str(hashed_key)


async def is_valid_secret_key(raw_key: str, hashed_key) -> bool:
    raw_key = bytes(raw_key, "utf-8")
    hashed_key = bytes(hashed_key, "utf-8")
    return bcrypt.checkpw(raw_key, hashed_key)
