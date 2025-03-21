# Petrol Station Finder

Welcome to the Petrol Station Finder! This Python program helps you locate the nearest petrol stations and their fuel prices within a 3-mile radius of a given UK postcode. It uses fuel price data from the UK government website and provides an average of the prices as well as the cheapest price. This was created as part of the final project for the CS50P course.


## Features

* Input a UK postcode to find nearby petrol stations.
* Retrieve the nearest 10 petrol stations within a 3-mile radius.
* Display the fuel prices for E5 petrol (super-unleaded), E10 petrol (unleaded), B7 diesel (standard grade), and SDV diesel (supergrade).
* Calculate and display the average prices and the cheapest prices for each fuel type.


## Prerequisites

Before you begin, ensure you have the following installed:

* Python 3.x
* Required Python packages: geopy, requests, json, statistics, ssl, certifi

You can install the necessary packages using pip:

`pip install geopy requests certifi`


## Usage

1. Clone this repository to your local machine.
2. Navigate to the directory containing the script.
3. Run the script using Python:

`python main.py`

4. Enter a valid UK postcode when prompted.


## Code Overview

### Main Function
The `main` function drives the program. It takes the user's postcode, fetches fuel data from various sources, finds nearby stores, and calculates and displays the relevant information.

### Get User Coordinates
The `get_user_coordinates` function converts a postcode into latitude and longitude coordinates using the Geopy library.

### Fetch Fuel Data
The `fetch_fuel_data` function fetches fuel price data from multiple URLs and combines it into a single list.

### Find Nearby Stores
The `find_nearby_stores` function calculates the distance between the user's location and each petrol station, returning those within a 3-mile radius.

### Calculate Averages and Cheapest Prices
The `calculate_averages_and_cheapest` function calculates the average prices and the cheapest prices for each fuel type.


## Example Output

```
Postcode: SW1A 1AA

Store: BP
Address: 123 Example Street
Postcode: SW1A 2BB
E5 petrol: 142.9
E10 petrol: 139.9
B7 diesel: 145.9
SDV diesel: 150.9
Distance: 1.25 miles

Average E5 petrol: 142.9p
Average E10 petrol: 139.9p
Average B7 diesel: 145.9p
Average SDV diesel: 150.9p

Cheapest E5 petrol: 142.9p
Cheapest E10 petrol: 139.9p
Cheapest B7 diesel: 145.9p
Cheapest SDV diesel: 150.9p
```

## Data Sources

The fuel price data is sourced from various UK fuel retailers, as listed below:

* Applegreen
* Asda
* BP
* Esso
* Morrisons
* Moto
* Motor Fuel Group
* Rontec
* Sainsbury's
* SGN
* Shell
* Ascona
* Jet
* Tesco
