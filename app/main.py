from datetime import datetime

from fastapi import FastAPI, Form, HTTPException

from app.config import get_config
from app.db.config import secrets
from app.db.hash import hash_secret_key, is_valid_secret_key
from app.schemas import PyObjectId, SecretCreate, SecretRetrive

app = FastAPI(title=get_config().app_name)


@app.post("/generate")
async def create_secret(schema: SecretCreate):
    """
    Create a secret in database.

    :param schema: SecretCreate is a parameter that take a SecretCreate instance
    :type schema: SecretCreate
    :return: ID of the inserted document.
    """
    secret: dict = schema.dict()
    secret["key"] = await hash_secret_key(secret.pop("key"))
    secret["created"] = datetime.now()
    result = await secrets.insert_one(secret)
    return str(result.inserted_id)


@app.post("/secret/{_id}", response_model=SecretRetrive)
async def get_secret(_id: PyObjectId, key: str = Form(...)):
    """
    Get a secret by its id. If key is valid the return secret.

    :param _id: PyObjectId
    :type _id: PyObjectId
    :param key: Secret key that will be used to decrypt the secret
    :type key: str
    :return: Secret instance.
    """
    secret = await secrets.find_one({"_id": _id})
    if secret is None:
        raise HTTPException(status_code=404, detail=f"There isn't any secrets with id({_id})")
    is_valid_key = await is_valid_secret_key(key, secret.get("key"))
    if not is_valid_key:
        raise HTTPException(status_code=400, detail="Invalid secret key")
    await secrets.delete_one({"_id": _id})
    return secret
