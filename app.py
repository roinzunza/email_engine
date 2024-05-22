from datetime import datetime, timedelta
import time

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

def find_events_close_to_birthday(customer, events, days_before=30):
    """
    Find events close to a customer's birthday within a specified number of days.

    Args:
        customer (dict): Customer information containing 'name' and 'birthday'.
        events (list): List of events with 'name' and 'date'.
        days_before (int): Number of days before the birthday to consider.

    Returns:
        list: List of events close to the customer's birthday.
    """
    print(f" ----------------- find_events_close_to_birthday -----------------")
    birthday = customer['birthday']
    print(f"birthday {birthday}")
    birthday_this_year = datetime(datetime.now().year, birthday.month, birthday.day)
    print(f"birthday_this_year {birthday_this_year}")
    start_date = birthday_this_year - timedelta(days=days_before)
    end_date = birthday_this_year + timedelta(days=days_before)

    relevant_events = []
    for event in events:
        print(f"event['date'] {event['date']}")
        print(f"start_date {start_date} event['date'] { event['date']} end_date{end_date}")
        if start_date <= event['date'] <= end_date:
            relevant_events.append(event['name'])
    print(f"relevant_events {relevant_events}")
    return relevant_events

def notify_customers(event, customers):
    """
    Notify customers about the given event.

    Args:
        event (dict): Event information containing 'name' and 'date'.
        customers (list): List of customers with 'name' and 'birthday'.
    """
    event_date = event['date']
    print(f" ----------------- notify_customers -----------------")
    for customer in customers:
        relevant_events = find_events_close_to_birthday(customer, [event])
        if event_date.date() == customer['birthday'].date() and event['name'] in relevant_events:
            print(f"Notifying {customer['name']} about the {event['name']} happening on {event_date}")

def event_listener(events, customers):
    """
    Listen for new events and notify relevant customers.

    Args:
        events (list): List of events with 'name' and 'date'.
        customers (list): List of customers with 'name' and 'birthday'.
    """
    # while True:
    # Mock new events arriving (for demonstration)
    new_events = [
        {"name": "Comedy Show", "date": datetime.now() + timedelta(days=5)},
        {"name": "Movie Screening", "date": datetime.now() + timedelta(days=10)},
    ]

    print(new_events)
    
    for event in new_events:
        notify_customers(event, customers)
    
    # Sleep for a while before checking for new events again
    # time.sleep(60)  # Check every minute

# Start the event listener
event_listener(events, customers)


"""
sequence

listen
 -> get new events
 -> check if any events full under current customers
    # check customers bday and event data within x days
    ## if it falls under add to notify list
-> send message to all customers to notify

## need
- customers
- events


# ask 
    how events are coming in
    what format the date is in
    how are customers are currently stored
    
"""
