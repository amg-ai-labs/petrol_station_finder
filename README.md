# ⛽ Petrol Station Finder

**Petrol Station Finder** is a Python-based command line tool that helps UK residents locate nearby fuel stations and compare fuel prices by postcode. Built for the CS50P final project, it uses government APIs, geocoding, and distance calculations to offer both convenience and insight for drivers.

---

## 💡 Project Overview

Fuel prices vary significantly between nearby stations — this tool helps users quickly compare prices and choose the most cost-effective or convenient option.

The script uses UK government fuel price data and geolocation to:
- Fetch stations within a 3-mile radius of a given UK postcode
- Display current prices for key fuel types
- Calculate the average and cheapest prices per fuel type

---

## ✅ Features

- 🔍 Accepts a UK postcode and searches nearby stations (within 3 miles)
- 📍 Retrieves fuel station data from UK government APIs
- ⛽ Displays fuel prices for:
  - E10 petrol (unleaded)
  - E5 petrol (super unleaded)
  - B7 diesel (standard)
  - SDV diesel (super grade)
- 📊 Calculates average prices and identifies the cheapest for each fuel type
- 🧪 Includes basic unit tests for key functions

---

## 🛠️ Technologies Used

- Python
- geopy
- requests
- JSON parsing
- Unit testing with `pytest`

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x  
- Install dependencies:
```bash
pip install geopy requests certifi
```


### ▶️ Usage

1. Clone the repository:
  ```bash
  git clone https://github.com/amg-ai-labs/petrol_station_finder.git  
  cd petrol_station_finder
  ```

2. Run the script:
  ```bash
    python main.py
  ```

3. Enter a valid UK postcode when prompted.

---

### 🧪 Testing

Basic unit tests are included in `test_main.py`.  
To run tests:
```bash
    pytest test_main.py
```

---

### 🗂️ Code Overview

### `main.py`

- Main driver script  
- Includes functions to:
  - Convert postcode to coordinates (`get_user_coordinates`)
  - Fetch and aggregate fuel data (`fetch_fuel_data`)
  - Find nearby stations (`find_nearby_stores`)
  - Calculate average and cheapest prices (`calculate_averages_and_cheapest`)

### `test_main.py`

- Unit tests for:
  - Coordinate conversion
  - Nearby station filtering
  - Price calculations

---

### 📊 Example Output

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

### Data Sources

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
