from pydantic import BaseModel


class SecretCreate(BaseModel):
    key: str
    text: str
