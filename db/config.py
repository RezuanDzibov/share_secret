from motor import motor_asyncio

client = motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
db = client.test_database
secrets = db.secrets
