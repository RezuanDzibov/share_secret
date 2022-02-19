from fastapi import FastAPI

from db.config import secrets
from schemas import SecretCreate, SecretRetrive, PyObjectId

app = FastAPI()


@app.post("/secret")
async def create_secret(schema: SecretCreate):
    secret: dict = schema.dict()
    result = await secrets.insert_one(secret)
    return str(result.inserted_id)


@app.get("/secret/{_id}", response_model=SecretRetrive)
async def get_secret(_id: PyObjectId):
    secret = await secrets.find_one({"_id": _id})
    return secret
