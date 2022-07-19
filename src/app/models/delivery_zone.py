"""Models for delivery service data"""
from typing import Optional, List

from pydantic import BaseModel, Field


class DeliveryZoneSchema(BaseModel):
    delivery_zone_id: int = Field(..., description="Number of delivery zone")
    coordinates: dict = Field(..., description="Coordinates of delivery zone")

    class Config:
        '''Class for store example of schema'''
        schema_extra = {
            "example": {
                "delivery_zone_id": 1,
                "coordinates": {"polygon": [[1, 1], [1, 8], [6, 8], [6, 1]], },
            }
        }


class DeliveryZoneModel(BaseModel):
    delivery_zone_id_: Optional[int]
    coordinates: Optional[List[List[float]]]

    class Config:
        '''Class for store example of schema'''
        schema_extra = {
            "example": {
                "delivery_zone_id_": 1,
                "coordinates": {"polygon": [[1, 1], [1, 8], [6, 8], [6, 1]], },
            }
        }
