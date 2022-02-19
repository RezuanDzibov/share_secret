from fastapi import FastAPI, Form, HTTPException

from db.config import secrets
from db.hash import hash_secret_key, is_valid_secret_key
from schemas import PyObjectId, SecretCreate, SecretRetrive

app = FastAPI()


@app.post("/secret")
async def create_secret(schema: SecretCreate):
    """
    Create a secret.
    
    :param schema: SecretCreate is a parameter that takes in a SecretCreate object
    :type schema: SecretCreate
    :return: The ID of the inserted secret.
    """
    secret: dict = schema.dict()
    secret["key"] = await hash_secret_key(secret.pop("key"))
    result = await secrets.insert_one(secret)
    return str(result.inserted_id)


@app.post("/secret/{_id}", response_model=SecretRetrive)
async def get_secret(_id: PyObjectId, key: str = Form(...)):
    """
    Get secret from the database and check if the secret key is valid.
    
    :param _id: PyObjectId
    :type _id: PyObjectId
    :param key: str = Form(...)
    :type key: str
    :return: The secret is being returned.
    """
    secret = await secrets.find_one({"_id": _id})
    if secret is None:
        raise HTTPException(status_code=404, detail=f"There isn't any secrets with id({_id})")
    is_valid_key = await is_valid_secret_key(key, secret.get("key"))
    if not is_valid_key:
        raise HTTPException(status_code=400, detail="Invalid secret key")
    await secrets.delete_one({"_id": _id})
    return secret
