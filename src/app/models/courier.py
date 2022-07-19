"""Model for courier"""
from typing import List

from pydantic import BaseModel


class CourierSchema(BaseModel):
    '''Class to store courier data schema'''
    personal_info: dict
    delivery_zones: List[int]
    id_courier: int

    class Config:
        '''Class for store example of schema'''
        schema_extra = {
            "example": {
                "personal_info": {"name": "Alex", "phone": "79789879687"},
                "delivery_zones": [1, 2, 7],
                "id_courier": 50
            }
        }


class UpdateCourierModel(BaseModel):
    '''Class to store courier update data schema'''
    personal_info: dict
    delivery_zones: List[int]
    id_courier: int

    class Config:
        '''Class for store example of schema'''
        schema_extra = {
            "example": {
                "personal_info": {"name": "Alex", "phone": "79789879687"},
                "delivery_zones": [1, 2, 7],
                "id_courier": 50
            }
        }
