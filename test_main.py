from main import (
    get_user_coordinates,
    find_nearby_stores,
    calculate_averages_and_cheapest,
    max_distance,
)
import pytest


# Test postcode-to-coordinate conversion with valid and invalid inputs
def test_get_user_coordinates():
    assert get_user_coordinates("CH43 7NJ") == (53.39666, -3.07945)
    assert get_user_coordinates("WA8 0BG") == (53.37323, -2.70749)
    with pytest.raises(SystemExit):
        get_user_coordinates("ljakssld")
    with pytest.raises(SystemExit):
        get_user_coordinates("98992398")


# Test store filtering logic and distance calculation
def test_find_nearby_stores():
    user_coordinates = (51.509865, -0.118092)
    stores_data = [
        {
            "brand": "Station 1",
            "location": {"latitude": 51.509865, "longitude": -0.118092},
            "address": "123 Example St",
            "postcode": "EC1A 1BB",
            "prices": {"E5": 130.0, "E10": 125.0, "B7": 140.0, "SDV": 145.0},
        }
    ]
    nearby_stores = find_nearby_stores(user_coordinates, stores_data, max_distance)
    assert nearby_stores[0]["name"] == "Station 1"
    assert nearby_stores[0]["E5 petrol"] == 130.0
    assert nearby_stores[0]["E10 petrol"] == 125.0
    assert nearby_stores[0]["B7 diesel"] == 140.0
    assert nearby_stores[0]["SDV diesel"] == 145.0


# Test average and cheapest price calculations across multiple stores
def test_calculate_averages_and_cheapest():
    nearby_stores = [
        {
            "name": "Station 1",
            "address": "123 Example St",
            "postcode": "EC1A 1BB",
            "E5 petrol": 130.0,
            "E10 petrol": 125.0,
            "B7 diesel": 140.0,
            "SDV diesel": 145.0,
            "distance": 1.0,
        },
        {
            "name": "Station 2",
            "address": "456 Another St",
            "postcode": "EC1A 2BB",
            "E5 petrol": 135.0,
            "E10 petrol": 128.0,
            "B7 diesel": 138.0,
            "SDV diesel": 147.0,
            "distance": 2.0,
        },
    ]

    averages, cheapest = calculate_averages_and_cheapest(nearby_stores)
    assert averages["E5_petrol"] == 132.5
    assert cheapest["E5_petrol"] == 130.0
