from motor import motor_asyncio
from pymongo.collection import Collection

from app.config import get_config

client = motor_asyncio.AsyncIOMotorClient(get_config().db_path)
db = client.database
secrets: Collection = db.secrets
secrets.create_index("created", expireAfterSeconds=86400)  # By default delete a document after 1 day
