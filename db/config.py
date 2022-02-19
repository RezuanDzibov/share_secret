from motor import motor_asyncio

client = motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
db = client.test_database
db = client["test_database"]
collection = db.test_collection
collection = db["test_collection"]
