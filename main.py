from fastapi import FastAPI, Form, HTTPException

from db.config import secrets
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
    result = await secrets.insert_one(secret)
    return str(result.inserted_id)


@app.post("/secret/{_id}", response_model=SecretRetrive)
async def get_secret(_id: PyObjectId, key: str = Form(...)):
    """
    Retrive a secret from the database
    
    :param _id: PyObjectId
    :type _id: PyObjectId
    :param key: str = Form(...)
    :type key: str
    :return: The secret is being returned.
    """
    secret = await secrets.find_one({"_id": _id, "key": key})
    if secret is None:
        raise HTTPException(status_code=404, detail=f"There isn't any secrets with id({_id}) and key({key}).")
    await secrets.delete_one({"_id": _id})
    return secret
