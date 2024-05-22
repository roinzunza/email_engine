import asyncio
import time
from datetime import datetime, timedelta

# Mock event data
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

class EmailEngine:

    _RELEVANT_EVENTS = []

    def  __init__(self, enabled_functions=[], days_before=100):
        self.enabled_functions=enabled_functions
        self.days_before = days_before

    def _send_notification(self):
        print("\t\t _send_notification ")
        print(EmailEngine._RELEVANT_EVENTS)
        
    def _birthday_helper(self, event_date):
        birthdays = []
        for customer in customers:
            if abs((customer["birthday"] - event_date).days) <= self.days_before:
                birthdays.append(customer)
                EmailEngine._RELEVANT_EVENTS.append(customer)

    async def _find_events_by_birthday(self):
        print("\t\t _find_events_by_birthday ")
        for event in events:
            print(event)
            self._birthday_helper(event['date'])

        print("\t\tdone _find_events_by_birthday ")
        # append events found


    async def _find_events_by_location(self):
        print("\t\t _find_events_by_location ")
        for event in events:
            print(event)
        # await asyncio.sleep(10)  # Use asyncio.sleep() instead of time.sleep()
        print("\t\tdone _find_events_by_location")

    async def driver(self):

        function_dict = {
        "location": self._find_events_by_location,
        "birthday": self._find_events_by_birthday
        }

        # # Run both coroutines concurrently
        # await asyncio.gather(
        #     self._find_events_by_birthday(),
        #     self._find_events_by_location()
        # )

        # Create a list to store coroutines to be executed concurrently
        coroutines = []

        # Iterate over enabled functions and append corresponding coroutines to the list
        for fnc_name in self.enabled_functions:
            print(f"calling: {fnc_name}")
            coroutines.append(function_dict[fnc_name]())

        # Execute all coroutines concurrently and wait for them to complete
        await asyncio.gather(*coroutines)
        self._send_notification()

# this function will listen
async def listener():
    count = 0
    while count < 1:

        enabled_functions = ["location","birthday"]
        this_engine = EmailEngine(enabled_functions)
        await this_engine.driver()
        count+=1

# Call the listener function
asyncio.run(listener())