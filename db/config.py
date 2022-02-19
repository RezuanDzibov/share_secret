from motor import motor_asyncio
from pymongo.collection import Collection

client = motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
db = client.test_database
secrets: Collection = db.secrets
secrets.create_index("created", expireAfterSeconds=5)  # By default delete a document after 1 day
