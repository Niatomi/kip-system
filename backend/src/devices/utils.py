from fastapi import Depends
from src.auth.oauth2 import get_current_user
from src.models import Users
from bson.objectid import ObjectId
from src.database import mongo_db


async def get_user_role(user: Users = Depends(get_current_user)):
    return user.role


async def get_mongo_object_by_id(object_id):
    return await mongo_db.device_description.find_one(
        {"_id": ObjectId(oid=object_id)})


async def get_mongo_id_by_spec(specification):

    obj = await mongo_db.device_description.find_one(
        {
            f"specifications.{specification}": {
                "$exists": "true"
            },
        }
    )
    if obj is not None:
        return str(obj['_id'])
    return None
