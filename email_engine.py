""" 

Sample email engine focusing on OOP design. 

- current design implementation allows for use of more email types without refactorig the current codebase

"""

from typing import List 
from datetime import datetime
# from geopy import distance

from customer import Customer
from event import Event

class EmailEngine:

    def __init__(self) -> None:
        pass

    def send_email(self, notifications: str) -> None:
        """Sends email notifications."""
        # place holder for sending api request to 3rd party Email API
        print(notifications)


    def get_notification_details(self, events_found: List[Event], customer: Customer, type= "") -> str:
        """Generates notification details based on found events."""

        notification_details = ""
        for event in events_found:
            notification_details += f"{event.name}, {event.city}, {event.date} "


        return f"Hi {customer.name} these events based on your {type} are in your area: {notification_details}"
    

    def filter_events_by_location(self, event: Event, customer: Customer):
        """Filters events based on customer's location."""
        if event.city ==  customer.city:
            return event
        

    def find_nearest_event(self, events: List[Event], customer: Customer) -> List[Event]:
        """Finds the nearest event based on customer's birthday."""
        min_days_away = float("inf")
        event_closest = None

        this_birthday = datetime.strptime(customer.birthday, "%Y-%m-%d")
        this_year_birthday = this_birthday.replace(year=datetime.now().year)

        for event in events:
            this_event_date = datetime.strptime(event.date, "%Y-%m-%d")

            days_away = abs(this_event_date -this_year_birthday)

            if  float(days_away.days)< float(min_days_away):
                min_days_away = float(days_away.days)
                event_closest = (event)

        return [event_closest]


    def filter_events_by_birthday(self, event: Event, customer: Customer) -> Event:
        """Finds the nearest event based on customer's birthday."""
        this_event_date = datetime.strptime(event.date, "%Y-%m-%d")

        this_birthday = datetime.strptime(customer.birthday, "%Y-%m-%d")
        this_year_birthday = this_birthday.replace(year=datetime.now().year)

        if this_year_birthday < this_event_date:
            return event


    def process_events(self, events: List[Event], customer: Customer, func_name, type= "") -> str:
        """Processes events based on the provided event filter."""
        events_found = []
        for event in events:
            this_event = func_name(event, customer)
            if this_event is not None:
                events_found.append(this_event)

        if type == "birthday":
            events_found  = self.find_nearest_event(events_found, customer) 
            
        notification_details = self.get_notification_details(events_found, customer, type)

        events_found.clear()
        return notification_details



def main():


    # List of mock Event objects
    events: List[Event] = [
        Event("Birthday Party", "New York", "2024-06-15", {"lat": 40.7128, "long": -74.0060}),
        Event("Conference", "San Francisco", "2024-07-20", {"lat": 40.7128, "long": -74.0060}),
        Event("Wedding", "Chicago", "2024-08-30", {"lat": 40.7128, "long": -74.0060}),
        Event("Music Festival", "Los Angeles", "2024-09-25", {"lat": 40.7128, "long": -74.0060}),
        Event("Art Exhibition", "Miami", "2024-10-10", {"lat": 40.7128, "long": -74.0060}),
        Event("Anime Exhibition", "New York", "2024-06-10", {"lat": 40.7128, "long": -74.0060})
    ]

    customer1 = Customer("John Doe", "1990-01-01", "New York")

    engine = EmailEngine(events, customer1)
    birthday_notifications = engine.process_events(events, customer1, engine.filter_events_by_birthday, type="birthday")
    engine.send_email(birthday_notifications)
    location_notifications = engine.process_events(events, customer1, engine.filter_events_by_location, type= "location")
    engine.send_email(location_notifications)


main()