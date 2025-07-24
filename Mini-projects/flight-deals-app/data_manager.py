import os
import requests
from pprint import pprint
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
load_dotenv()

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_prices_endpoint = os.getenv("SHEETY_PRICES_ENDPOINT")
        self.sheety_users_endpoint = os.getenv("SHEETY_USERS_ENDPOINT")
        self.user = os.getenv("SHEETY_USERNAME")
        self.password = os.getenv("SHEETY_PASSWORD")
        self.authorization = HTTPBasicAuth(self.user, self.password)
        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        response = requests.get(self.sheety_prices_endpoint, auth=self.authorization)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for updated_row_data in self.destination_data:
            # creating a json format for each row to put into the actual sheet
            add_data = {
                "price": {
                    "iataCode": updated_row_data["iataCode"]
                }
            }
            response = requests.put(f"{self.sheety_prices_endpoint}/{updated_row_data["id"]}",
                                    json=add_data, auth=self.authorization)

    def get_customer_emails(self):
        response = requests.get(self.sheety_users_endpoint, auth=self.authorization)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
