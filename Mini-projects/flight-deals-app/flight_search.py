import os
import requests
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

IATA_endpoint = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
flight_endpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers"
token_endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"

class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def __init__(self):
        self.api_key = os.environ["AMADEUS_API_KEY"]
        self.api_secret = os.environ["AMADEUS_SECRET"]
        # Getting a new token every time program is run. Could reuse unexpired tokens as an extension.
        self.token = self.get_new_token()

    def get_destination_code(self, city):
        print(f"Using this token to get destination {self.token}")
        headers = {"Authorization": f"Bearer {self.token}"}
        params = {
            "keyword": city,
            "max": 2,
            "include": "AIRPORTS"
        }
        response = requests.get(IATA_endpoint, params=params, headers=headers)
        try:
            code = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city}.")
            return "Not Found"
        return code


    def get_new_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self.api_key,
            'client_secret': self.api_secret
        }
        response = requests.post(url=token_endpoint, headers=header, data=body)

        # New bearer token. Typically expires in 1799 seconds (30min)
        print(f"Your token is {response.json()['access_token']}")
        print(f"Your token expires in {response.json()['expires_in']} seconds")

        return response.json()['access_token']


    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time, is_direct=True):
        headers = {
            "Authorization": f"Bearer {self.token}",
        }
        params = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time,
            "returnDate": to_time,
            "adults": 1,
            "nonStop": "true" if is_direct else "false",
            "currencyCode": "INR",
            "max": "10"
        }

        response = requests.get(flight_endpoint, params=params, headers=headers)

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation:\n"
                  "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                  "-reference")
            print("Response body:", response.text)
            return None

        return response.json()
