import asyncio
import time
from datetime import datetime, timedelta
from typing import Union




class EmailEngine:

    def __init__(self) -> None:
        pass

    def _send_notification(self):
        pass

    def _find_by_bday(self):
        pass

    def notify_customers(self, event: dict, customers: list)-> Union[list, Exception]:


        return ["found"], None
    

def testing():
    from geopy.distance import geodesic

    # Example coordinates for two places (New York and San Francisco)
    coords1 = (40.7128, -74.0060)  # Latitude and longitude of New York City
    coords2 = (37.7749, -122.4194)  # Latitude and longitude of San Francisco

    # Calculate the distance using geopy
    distance = geodesic(coords1, coords2).kilometers

    print(f"Distance between the two places: {distance:.2f} kilometers")

def listener():

    this_engine = EmailEngine()

    while True:
        # Create a copy of the original list of events
        # Mock event data

        # got from API
        events = [
            {"name": "Music Concert", "date": datetime(2024, 6, 15)},
            {"name": "Art Exhibition", "date": datetime(2024, 7, 5)},
            {"name": "Food Festival", "date": datetime(2024, 8, 20)},
        ]

        # Mock customer data
        customers = [
            {"name": "Alice", "birthday": datetime(1990, 5, 15)},
            {"name": "Bob", "birthday": datetime(1985, 6, 25)},
            {"name": "Charlie", "birthday": datetime(1988, 7, 10)},
        ]


        events_copy = events.copy()
        for event in events:
            print(event)
            # Call notify_customers method and unpack the result
            result, err = this_engine.notify_customers(event, customers)

            # Handle the result using match-case statement
            match result:
                case "":
                    print(f"Customers notified successfully for event: {event}")
                case err:  # Matches if err is not empty (i.e., an error occurred)
                    print(f"Failed to notify customers for event: {event}. Error: {err}")
            events_copy.pop(0)  # Remove the first event from the original list

        # wait before querying again
        time.sleep(10)



listener()
