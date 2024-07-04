from geopy.distance import geodesic
import requests
import json
import sys
import statistics
import ssl
import certifi
import geopy.geocoders


# Add the UK gov fuel data links to an empty list (https://www.gov.uk/guidance/access-fuel-price-data).
fuel_data_urls = [
    "https://applegreenstores.com/fuel-prices/data.json",
    "https://storelocator.asda.com/fuel_prices_data.json",
    "https://www.bp.com/en_gb/united-kingdom/home/fuelprices/fuel_prices_data.json",
    "https://fuelprices.esso.co.uk/latestdata.json",
    "https://www.morrisons.com/fuel-prices/fuel.json",
    "https://moto-way.com/fuel-price/fuel_prices.json",
    "https://fuel.motorfuelgroup.com/fuel_prices_data.json",
    "https://www.rontec-servicestations.co.uk/fuel-prices/data/fuel_prices_data.json",
    "https://api.sainsburys.co.uk/v1/exports/latest/fuel_prices_data.json",
    "https://www.sgnretail.uk/files/data/SGN_daily_fuel_prices.json",
    "https://www.shell.co.uk/fuel-prices-data.html",
    "https://fuelprices.asconagroup.co.uk/newfuel.json",
    "https://jetlocal.co.uk/fuel_prices_data.json",
    "https://www.tesco.com/fuel_prices/fuel_prices_data.json",
]

# Set the maximum distance radius around postcode for stores to be returned
max_distance = 3


def main():
    # User enters postcode
    user_postcode = input("Postcode: ")
    user_coordinates = get_user_coordinates(user_postcode)
    stores_data = fetch_fuel_data(fuel_data_urls)
    nearby_stores = find_nearby_stores(user_coordinates, stores_data, max_distance)

    print()
    # Runs through the nearby stores and prints out key information for each store.
    if nearby_stores:
        for store in nearby_stores:
            print(f"Store: {store['name']}")
            print(f"Address: {store['address']}")
            print(f"Postcode: {store['postcode']}")
            print(f"E5 petrol: {store['E5 petrol']}")
            print(f"E10 petrol: {store['E10 petrol']}")
            print(f"B7 diesel: {store['B7 diesel']}")
            print(f"SDV diesel: {store['SDV diesel']}")
            print(f"Distance: {store['distance']} miles")
            print()

        # Calculates and prints out the average for each fuel type and the cheapest price.
        averages, cheapest = calculate_averages_and_cheapest(nearby_stores)
        print(f"Average E5 petrol: {averages['E5_petrol']}p")
        print(f"Average E10 petrol: {averages['E10_petrol']}p")
        print(f"Average B7 diesel: {averages['B7_diesel']}p")
        print(f"Average SDV diesel: {averages['SDV_diesel']}p")
        print()
        print(f"Cheapest E5 petrol: {cheapest['E5_petrol']}p")
        print(f"Cheapest E10 petrol: {cheapest['E10_petrol']}p")
        print(f"Cheapest B7 diesel: {cheapest['B7_diesel']}p")
        print(f"Cheapest SDV diesel: {cheapest['SDV_diesel']}p")

    else:
        print(f"No stores found within {max_distance} miles.")


def get_user_coordinates(postcode):
    ctx = ssl.create_default_context(cafile=certifi.where())
    geopy.geocoders.options.default_ssl_context = ctx

    # Uses the geolocator module to convert a valid postcode into a latitude and longitude coordinates,
    # otherwise program exits.
    try:
        geolocator = geopy.geocoders.Nominatim(user_agent="fuel_price_checker")
        location = geolocator.geocode(postcode)
        return location.latitude, location.longitude
    except AttributeError:
        sys.exit("Incorrect postcode")


def fetch_fuel_data(urls):
    # Initialises an empty list, in which the data from the urls is extended onto.
    all_fuel_data = []
    for url in urls:
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()
            all_fuel_data.extend(data.get("stations", []))
        # If there are exceptions or timeouts, the program passes them and continues to the next one.
        except requests.RequestException:
            pass
        except json.JSONDecodeError:
            pass
    return all_fuel_data


def find_nearby_stores(user_coordinates, stores_data, max_distance):
    nearby_stores = []
    max_stores = 10

    # Calculates the distance between the user postcode and the postcodes for each store in the list.
    for store in stores_data:
        store_coordinates = (
            store["location"]["latitude"],
            store["location"]["longitude"],
        )
        distance = round(geodesic(user_coordinates, store_coordinates).miles, 2)

        # Only appends a store's details if the distance is less than the pre-specified max distance,
        # so only nearby stores are returned.
        if distance <= max_distance:
            nearby_stores.append(
                {
                    "name": store["brand"],
                    "address": store["address"],
                    "postcode": store["postcode"],
                    "E5 petrol": store["prices"].get("E5", "N/A"),
                    "E10 petrol": store["prices"].get("E10", "N/A"),
                    "B7 diesel": store["prices"].get("B7", "N/A"),
                    "SDV diesel": store["prices"].get("SDV", "N/A"),
                    "distance": distance,
                }
            )

    # Sorts the nearby_stores list in ascending order of distance using the anonymous lambda function.
    nearby_stores = sorted(nearby_stores, key=lambda x: x["distance"])[:max_stores]
    return nearby_stores


def calculate_averages_and_cheapest(nearby_stores):
    # Initialises a dictionary for each valid fuel value to be added on.
    fuel_prices = {
        "E5_petrol": [],
        "E10_petrol": [],
        "B7_diesel": [],
        "SDV_diesel": [],
    }

    # As some stores do not provide certain fuel prices, this skips them so only real values are appended to the list.
    for store in nearby_stores:
        if store["E5 petrol"] != "N/A":
            fuel_prices["E5_petrol"].append(store["E5 petrol"])
        if store["E10 petrol"] != "N/A":
            fuel_prices["E10_petrol"].append(store["E10 petrol"])
        if store["B7 diesel"] != "N/A":
            fuel_prices["B7_diesel"].append(store["B7 diesel"])
        if store["SDV diesel"] != "N/A":
            fuel_prices["SDV_diesel"].append(store["SDV diesel"])

    # Empty dictionaries for average and cheapest are initiated.
    # The fuel prices list is then iterated through to return the values.
    fuel_averages = {}
    fuel_cheapest = {}
    for fuel_type, prices in fuel_prices.items():
        if prices:
            fuel_averages[fuel_type] = round(statistics.mean(prices), 2)
            fuel_cheapest[fuel_type] = round(min(prices), 2)
        else:
            fuel_averages[fuel_type] = 0
            fuel_cheapest[fuel_type] = 0

    return fuel_averages, fuel_cheapest


if __name__ == "__main__":
    main()
