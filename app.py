from email_engine import EmailEngine
from datetime import datetime, timedelta
from flask import Flask, request, jsonify
from customer import Customer
from event import Event
from typing import List

app = Flask(__name__)


@app.route('/email_engine', methods=['POST'])
def email_engine():
    # Check if request contains JSON data
    if not request.is_json:
        return jsonify({'message': 'Request must contain JSON data'}), 400
    

    data = request.get_json()
    events = data.get('events')
    customer = data.get('customer')

    # List of mock Event objects
    events: List[Event] = [
        Event("Birthday Party", "New York", "2024-06-15", {"lat": 40.7128, "long": -74.0060}),
        Event("Conference", "San Francisco", "2024-07-20", {"lat": 40.7128, "long": -74.0060}),
        Event("Wedding", "Chicago", "2024-08-30", {"lat": 40.7128, "long": -74.0060}),
        Event("Music Festival", "Los Angeles", "2024-09-25", {"lat": 40.7128, "long": -74.0060}),
        Event("Art Exhibition", "Miami", "2024-10-10", {"lat": 40.7128, "long": -74.0060}),
        Event("Anime Exhibition", "New York", "2024-06-10", {"lat": 40.7128, "long": -74.0060})
    ]

    customer = Customer("John Doe", "1990-01-01", "New York")

    if events is None or not events:
        return jsonify({'message': 'no events'}), 400
    
    if customer is None or not customer:
        return jsonify({'message': 'no subscribers'}), 400
    
    engine = EmailEngine(events, customer)
    birthday_notifications = engine.process_events(events, customer, engine.process_birthday_based, type="birthday")
    engine.send_email(birthday_notifications)
    location_notifications = engine.process_events(events, customer, engine.process_location_based, type= "location")
    engine.send_email(location_notifications)

    return jsonify({'message': 'success'}), 200

    
if __name__ == '__main__':
    app.run(debug=True)

