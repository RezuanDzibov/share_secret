import os
from pathlib import Path

from dotenv import load_dotenv
from motor import motor_asyncio
from pymongo.collection import Collection

BASE_DIR = Path(__file__).parent.parent
load_dotenv(dotenv_path=BASE_DIR / ".env")

client = motor_asyncio.AsyncIOMotorClient(os.getenv("MONGO_URL"))
db = client.database
secrets: Collection = db.secrets
secrets.create_index("created", expireAfterSeconds=86400)  # By default delete a document after 1 day
