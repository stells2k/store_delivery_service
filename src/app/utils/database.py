"""Module providing basic functionality to connect to mongoDB base"""
import json
import os
from typing import Any

import motor.motor_asyncio
from bson import json_util

MONGO_DETAILS = [os.getenv("MONGO_HOST", "mongodb://localhost:27017")]
COLLECTION = [os.getenv("MONGO_COLLECTION", "delivery_service")]

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.delivery_service
delivery_collection = database.get_collection(COLLECTION)


def parse_json(data: Any):
    '''
    Function to convert data from bson to json format.
            Parameters:
                    data (Any):
                        Any data to convert
            Returns:
                    data in json format
    '''
    return json.loads(json_util.dumps(data))
