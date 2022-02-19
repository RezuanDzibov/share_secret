from motor import motor_asyncio
from pymongo.collection import Collection

client = motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
db = client.test_database
secrets: Collection = db.secrets
