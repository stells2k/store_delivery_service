"""Module providing basic delivery service functionality"""
from typing import List
from shapely.geometry import Polygon, Point

from src.app.utils.database import delivery_collection, parse_json


async def create_new_zone(id_zone: int, coordinates: dict) -> dict:
    '''
    Function to create new delivery zone.
            Parameters:
                    id_zone (int):
                        A decimal integer
                    coordinates (dict):
                        A dictionary with zone coordinates
            Returns:
                    dict: Dictionary with full data about new zone
    '''

    data_to_save = {'id_zone': id_zone, 'coordinates': coordinates}
    delivery_zone = await delivery_collection.insert_one(data_to_save)
    inserted_id = delivery_zone.inserted_id
    new_zone = await delivery_collection.find_one({"_id": inserted_id})
    return {'data': parse_json(new_zone)}


async def create_new_courier(id_courier: int, personal_info: dict,
                             delivery_zones: List[int]) -> dict:
    '''
    Function to create new courier in database.

            Parameters:
                    id_courier (int):
                        A decimal integer
                    personal_info (dict):
                        A dictionary with personal info
                    delivery_zones (List[int]):
                        List of numbers supporting delivery zone

            Returns:
                    dict: Dictionary with full data about new courier
    '''
    data_to_save = {'id_courier': id_courier, 'personal_info': personal_info,
                    'delivery_zones': delivery_zones}
    courier = await delivery_collection.insert_one(data_to_save)
    courier = await delivery_collection.find_one({"_id": courier.inserted_id})
    return {'courier': parse_json(courier)}


def check_point(point: List[float], polygon: List[List[float]]) -> bool:
    '''
    Function to check point belongs to geo zone or not.
            Parameters:
                    point (List[int]):
                        List of point coordinates
                    polygon (List[List[float]]):
                        List of polygon coordinates
            Returns:
                    bool: True if point belongs to geo zone
    '''
    point_ = Point(point)
    poly = Polygon(polygon)
    return poly.contains(point_)


async def get_courier_for_delivery(delivery_point: List[float]) -> dict:
    '''
    Function to get courier to delivery order at provided geo point.
            Parameters:
                    delivery_point (List[int]):
                        List of point coordinates
            Returns:
                    dict: Contents a number of zone to delivery, courier info
    '''
    delivery_zones = await delivery_collection.find(
        {"_id": {"$exists": True}}).to_list(length=100)

    for zone in delivery_zones:
        if check_point(delivery_point, zone['coordinates']['polygon']):
            id_zone = zone['id_zone']
            courier = await delivery_collection.find_one(
                {"delivery_zones": id_zone})
            courier_info = parse_json(courier)["personal_info"]
            return {'id_zone': id_zone, 'courier': courier_info}
    return {'404': 'Courier not found'}
