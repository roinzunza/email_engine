from itertools import product
from datetime import datetime, timedelta
from geopy import distance
from typing import Tuple, Optional

class EmailNotificationEngine:
    def __init__(self, events: list, subscribers: list):
        self.events = events
        self.subscribers = subscribers
        self.notify_list = {}

    def _send_notification(self, event_name: str):
        # send notification to notify list
        for sub, events in self.notify_list.items():
            print(f"notifying: {sub} for {event_name} events: {events}")

    def validate_birthday(self, event: dict, subscriber: dict):
        within_days = 10
        # Check if the event falls within the subscriber's birthday range
        this_event_date = event.get('date')
        this_birthday = subscriber.get('birthday')
        this_year_birthday = this_birthday.replace(year=datetime.now().year)

        if this_year_birthday <= this_event_date <= this_year_birthday + timedelta(days=within_days):

            if subscriber.get("name") not in self.notify_list:
                self.notify_list[ subscriber.get("name")] = [event]
            else:
                self.notify_list[ subscriber.get("name")].append(event)


    def validate_distance(self, event: dict, subscriber: dict):
        distance_threshold = 400
        # Check if the event is within a certain distance for the subscriber
        this_event_location = event.get('location')
        this_subscriber_location = subscriber.get('location')

        this_event_coord = (this_event_location.get('lat'), this_event_location.get('long'))
        this_subscriber_coord = (this_subscriber_location.get('lat'), this_subscriber_location.get('long'))

        this_event_distance = distance.distance(this_event_coord, this_subscriber_coord).miles

        if this_event_distance < distance_threshold:

            if subscriber.get("name") not in self.notify_list:
                self.notify_list[ subscriber.get("name")] = [event]
            else:
                self.notify_list[ subscriber.get("name")].append(event)

    def process_events(self, validation_func , event_name):
        for event, subscriber in product(self.events, self.subscribers):
            validation_func(event, subscriber)

        self._send_notification(event_name)
        self.notify_list.clear()

# mock event data
events = [
    {"name": "Music Concert", "date": datetime(2024, 6, 15), "location": {"lat": 40.7128, "long": -74.0060}},  # New York, NY
    {"name": "Art Exhibition", "date": datetime(2024, 7, 5), "location": {"lat": 34.0522, "long": -118.2437}},  # Los Angeles, CA
    {"name": "history Exhibition", "date": datetime(2024, 7, 4), "location": {"lat": 34.0522, "long": -118.2437}},  # Los Angeles, CA
    {"name": "Food Festival", "date": datetime(2024, 8, 20), "location": {"lat": 41.8781, "long": -87.6298}},  # Chicago, IL
    {"name": "Gaming experience", "date": datetime(2024, 6, 15), "location": {"lat": 40.7128, "long": -74.0060}},  # New York, NY
]

# Mock customer data from API
subscribers = [
    {"name": "Alice", "birthday": datetime(1990, 5, 15), "location": {"lat": 40.7128, "long": -74.0060}, "threshold": 300},  # New York, NY
    {"name": "Bob", "birthday": datetime(1985, 6, 25), "location": {"lat": 34.0522, "long": -118.2437}, "threshold": 10000},  # Los Angeles, CA
    {"name": "Charlie", "birthday": datetime(1988, 7, 10), "location": {"lat": 48.8566, "long": 2.3522}, "threshold": 100},  # Paris, France
]

engine = EmailNotificationEngine(events, subscribers)
engine.process_events(engine.validate_distance, "nearest")
engine.process_events(engine.validate_birthday, "close to birthday")