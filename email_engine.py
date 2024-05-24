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

    def __init__(self, events, customer) -> None:
        self.events = events
        self.customer = customer

    def send_email(self, notifications: str) -> None:
        # place holder for sending api request to 3rd party Email API
        print(notifications)


    def get_notification_details(self, events_found: List[Event], type= "") -> str:

        notification_details = ""
        for event in events_found:
            notification_details += f"{event.name}, {event.city}, {event.date} "


        return f"Hi {self.customer.name} these events based on your {type} are in your area: {notification_details}"
    

    def process_location_based(self, event: Event, customer: Customer):

        if event.city ==  customer.city:
            return event
        

    def find_nearest(self, events: List[Event]) -> List[Event]:

        min_days_away = float("inf")
        event_closest = None

        this_birthday = datetime.strptime(self.customer.birthday, "%Y-%m-%d")
        this_year_birthday = this_birthday.replace(year=datetime.now().year)

        for event in events:
            this_event_date = datetime.strptime(event.date, "%Y-%m-%d")

            days_away = abs(this_event_date -this_year_birthday)

            if  float(days_away.days)< float(min_days_away):
                min_days_away = float(days_away.days)
                event_closest = (event)

        return [event_closest]


    def process_birthday_based(self, event: Event, customer: Customer) -> Event:

        this_event_date = datetime.strptime(event.date, "%Y-%m-%d")

        this_birthday = datetime.strptime(self.customer.birthday, "%Y-%m-%d")
        this_year_birthday = this_birthday.replace(year=datetime.now().year)

        if this_year_birthday < this_event_date:
            return event


    def process_events(self, events: List[Event], customer: Customer, func_name, type= "") -> str:
        events_found = []
        for event in events:
            this_event = func_name(event, customer)
            if this_event is not None:
                events_found.append(this_event)

        if type == "birthday":
            events_found  = self.find_nearest(events_found) 
            
        notification_details = self.get_notification_details(events_found, type)

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
    birthday_notifications = engine.process_events(events, customer1, engine.process_birthday_based, type="birthday")
    engine.send_email(birthday_notifications)
    location_notifications = engine.process_events(events, customer1, engine.process_location_based, type= "location")
    engine.send_email(location_notifications)


main()