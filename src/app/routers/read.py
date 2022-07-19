"""Route rules for read operations"""
from typing import List

from fastapi import APIRouter

from src.app.services.delivery_service import get_courier_for_delivery
from src.app.utils.database import delivery_collection, parse_json

router = APIRouter()


@router.get('/retrieve_delivery_zones',
            description='Get information about all available delivery zones')
async def retrieve_delivery_zones():
    delivery_zones = []
    async for delivery_zone in delivery_collection.find():
        delivery_zones.append(delivery_zone)
    return {'result': parse_json(delivery_zones)}


@router.post('/get_courier_for_delivery',
             description='Get information about courier for provided '
                         'delivery point')
async def get_courier(delivery_point: List[float]):
    return await get_courier_for_delivery(delivery_point)
