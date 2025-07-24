import time
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

my_city_IATA = "HYD"

# ==================== Update the Airport Codes in Google Sheet ====================

for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        time.sleep(2)

data_manager.destination_data = sheet_data
data_manager.update_destination_codes()

# ==================== Retrieve your customer emails ====================

customer_data = data_manager.get_customer_emails()
customer_email_list = [row["whatIsYourEmail?"] for row in customer_data]

# ==================== Search for Flights and Send Notifications ====================

tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
one_month_from_today = (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")

for destination in sheet_data:
    print(f"Getting flights for {destination}")
    stopover_flights = flight_search.check_flights(my_city_IATA, destination["iataCode"], from_time=tomorrow,
                                                to_time=one_month_from_today, is_direct="false")
    cheapest_flight = find_cheapest_flight(stopover_flights)
    print(f"{destination['city']}: INR {cheapest_flight.price}")
    # Slowing down requests to avoid rate limit
    time.sleep(2)

    # ==================== Search for indirect flight if N/A ====================

    if cheapest_flight.price == "N/A":
        print(f"No direct flight to {destination['city']}. Looking for indirect flights...")
        stopover_flights = flight_search.check_flights(
            my_city_IATA,
            destination["iataCode"],
            from_time=tomorrow,
            to_time=one_month_from_today,
            is_direct=False
        )
        cheapest_flight = find_cheapest_flight(stopover_flights)
        print(f"Cheapest indirect flight price is: INR {cheapest_flight.price}")
    else:
        print(f"Direct flight found! the price is: INR {cheapest_flight.price}")

    # ==================== Send Notifications and Emails  ====================

    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        # Customise the message depending on the number of stops
        if cheapest_flight.stops == 0:
            message = f"Low price alert! Only INR {cheapest_flight.price} to fly direct " \
                    f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, " \
                    f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        else:
            message = f"Low price alert! Only INR {cheapest_flight.price} to fly " \
                    f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, " \
                    f"with {cheapest_flight.stops} stop(s) " \
                    f"departing on {cheapest_flight.out_date} and returning on {cheapest_flight.return_date}."

        print(f"Check your email. Lower price flight found to {destination['city']}!")

        # notification_manager.send_sms(message_body=message)
        # SMS not working? Try whatsapp instead.
        notification_manager.send_whatsapp(message_body=message)

        # Send emails to everyone on the list
        notification_manager.send_emails(email_list=customer_email_list, email_body=message)

