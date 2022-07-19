"""Route rules for create operations"""
from fastapi import APIRouter

from src.app.models.courier import CourierSchema
from src.app.models.delivery_zone import DeliveryZoneSchema
from src.app.services.delivery_service import create_new_zone, create_new_courier

router = APIRouter()


@router.post('/add_delivery_zone',
             description='Adding info about new delivery zone')
async def add_delivery_zone(data: DeliveryZoneSchema) -> dict:
    return await create_new_zone(data.delivery_zone_id, data.coordinates)


@router.post('/add_courier', description='Adding info about new courier')
async def add_courier(data: CourierSchema) -> dict:
    return await create_new_courier(data.id_courier, data.personal_info,
                                    data.delivery_zones)
