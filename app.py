"""
Email notification engine for
- events close to someones birthday
- events within someones location

customers List [Dict{}]
events  List [Dict[]]
"""
import time
from datetime import datetime, timedelta
from geopy.distance import geodesic
from typing import Tuple, Optional

class EmailEngine:

    def __init__(self) -> None:
        self._events_near_customer = {}
        self._events_within_birthday = {}


    @staticmethod
    def _send_notification(notify_list):
        print(" ------------ _send_notification ------------")
        for customer, events in notify_list.items():
            # assume api request
            try:
                print(f"sending {customer} email for events: {events}")
            except Exception as e:
                print(repr(e))


    def _event_close_to_birthday(self, event: dict, customer: dict) -> None:
        # would append to _EVENTS_WITHIN_BIRTHDAY
        pass


    @staticmethod
    def _calculate_distance(event_coord: Tuple[float, float], customer_coord: Tuple[float, float]) -> Optional[float]:
        """
        Calculate the distance between two coordinates using geodesic distance.

        Args:
            event_coord (Tuple[float, float]): The coordinates (latitude, longitude) of the event.
            customer_coord (Tuple[float, float]): The coordinates (latitude, longitude) of the customer.

        Returns:
            Optional[float]: The distance between the two coordinates in miles, or None if any coordinate is missing.
        """

        if None in event_coord or None in customer_coord:
            return
        
        try:
            return geodesic(event_coord, customer_coord).miles
        except Exception as e:
            print(repr(e))
            return None


    def _event_near_customer(self, event: dict, customer: dict) -> None:
        print(" ------------ _event_near_customer ------------")

        this_event_location = event.get('location')
        this_customer_location = customer.get('location')

        # skip on those without location data
        if this_event_location is None or this_customer_location is None:
            return None
        
        this_event_coord = (this_event_location.get('lat'), this_event_location.get('long'))

        this_customer_coord = (this_customer_location.get('lat'),this_customer_location.get('long'))
        this_distance = EmailEngine._calculate_distance(this_event_coord, this_customer_coord)

        if this_distance is not None and this_distance <= customer.get("threshold", float('inf')):
            if customer['name'] not in self._events_near_customer:
                self._events_near_customer[customer['name']] = [event]
            else:
                self._events_near_customer[customer['name']].append(event)


    def driver(self, event: dict, customers: list) -> None:
        for customer in customers:
            self._event_near_customer(event, customer)
            self._event_close_to_birthday(event, customer)

        notify_customers_near = self._events_near_customer.copy()
        EmailEngine._send_notification(notify_customers_near)
        self._events_near_customer.clear()

        notify_customers_birthday = self._events_within_birthday.copy()
        EmailEngine._send_notification(notify_customers_birthday)
        self._events_within_birthday.clear()


def listener():

    this_email_engine = EmailEngine()

    while True:
        # mock event data
        events = [
            {"name": "Music Concert", "date": datetime(2024, 6, 15), "location": {"lat": 40.7128, "long": -74.0060}},  # New York, NY
            {"name": "Art Exhibition", "date": datetime(2024, 7, 5), "location": {"lat": 34.0522, "long": -118.2437}},  # Los Angeles, CA
            {"name": "Food Festival", "date": datetime(2024, 8, 20), "location": {"lat": 41.8781, "long": -87.6298}},  # Chicago, IL
            {"name": "Gaming experience", "date": datetime(2024, 6, 15), "location": {"lat": 40.7128, "long": -74.0060}},  # New York, NY
        ]

        # Mock customer data from API
        customers = [
            {"name": "Alice", "birthday": datetime(1990, 5, 15), "location": {"lat": 40.7128, "long": -74.0060}, "threshold": 300},  # New York, NY
            {"name": "Bob", "birthday": datetime(1985, 6, 25), "location": {"lat": 51.5074, "long": -0.1278}, "threshold": 10000},  # London, UK
            {"name": "Charlie", "birthday": datetime(1988, 7, 10), "location": {"lat": 48.8566, "long": 2.3522}, "threshold": 100},  # Paris, France
        ]

        for event in events:
            this_email_engine.driver(event, customers)

        time.sleep(10)


listener()


