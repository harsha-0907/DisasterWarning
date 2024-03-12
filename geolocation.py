# Get the coordinates and convert to a city name
import requests


def convertCoordinatesToCity(lat, lng):
    apikey = "bdc_43e7339ecac34660a139e16f7073a6ce"  # bigdata-api
    base_url = r"https://api-bdc.net/data/reverse-geocode"
    params = {'latitude': lat, 'longitude': lng, 'localityLanguage': 'en', 'key': apikey}

    resp = requests.get(base_url, params=params)
    status_code = resp.status_code
    # print(status_code)
    if status_code == 200:
        data = resp.json()
        city = data['city']
    elif status_code == 401:
        raise Exception("AP Error - BigData API")
        # Write in a log
    else:
        raise Exception("Unknown")
    print(city)
    return city


def convertCityToCoordinates(cityname):
    # print(cityname)
    apikey = "pk.02b5994cb8a776ef80fd220a5ebd8be4"  # Api key for location iq
    base_url = r"https://us1.locationiq.com/v1/search"
    params = {'key': apikey, 'q': cityname, 'format': 'json'}
    resp = requests.get(base_url, params=params)
    print(resp.url)
    data = resp.json()
    status_code = resp.status_code
    if status_code == 200:
        # API KEY is still valid
        coordinates = (float(data[0]["lat"]), float(data[0]["lon"]))
        # print(coordinates)
    elif status_code == 401:
        raise Exception("API Error - (LocationIQ")
        # Write in a log
    else:
        # Write in a log
        print(f"Error - {status_code}")
        raise Exception("Unknown Error")
    return coordinates


# city = convertCoordinatesToCity(17.680, 83.08)
# print(convertCityToCoordinates(city))