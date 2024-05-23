from email_notification_engine import EmailNotificationEngine
from datetime import datetime, timedelta
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/email_engine', methods=['POST'])
def email_engine():
    # Check if request contains JSON data
    if not request.is_json:
        return jsonify({'message': 'Request must contain JSON data'}), 400
    

    data = request.get_json()
    events = data.get('events')
    subscribers = data.get('subscribers')

    # mock event data
    events = [
        {"name": "Music Concert", "date": datetime(2024, 6, 15), "location": {"lat": 40.7128, "long": -74.0060}},  # New York, NY
        {"name": "Art Exhibition", "date": datetime(2024, 7, 5), "location": {"lat": 34.0522, "long": -118.2437}},  # Los Angeles, CA
        {"name": "Food Festival", "date": datetime(2024, 8, 20), "location": {"lat": 41.8781, "long": -87.6298}},  # Chicago, IL
        {"name": "Gaming experience", "date": datetime(2024, 6, 15), "location": {"lat": 40.7128, "long": -74.0060}},  # New York, NY
    ]

    # Mock customer data from API
    subscribers = [
        {"name": "Alice", "birthday": datetime(1990, 5, 15), "location": {"lat": 40.7128, "long": -74.0060}, "threshold": 300},  # New York, NY
        {"name": "Bob", "birthday": datetime(1985, 6, 25), "location": {"lat": 51.5074, "long": -0.1278}, "threshold": 10000},  # London, UK
        {"name": "Charlie", "birthday": datetime(1988, 7, 10), "location": {"lat": 48.8566, "long": 2.3522}, "threshold": 100},  # Paris, France
    ]


    if events is None or not events:
        return jsonify({'message': 'no events'}), 400
    
    if subscribers is None or not subscribers:
        return jsonify({'message': 'no subscribers'}), 400
    
    engine = EmailNotificationEngine(events, subscribers)
    engine.process_events(engine.validate_distance, "nearest")
    engine.process_events(engine.validate_birthday, "close to birthday")

    return jsonify({'message': 'success'}), 200

    
if __name__ == '__main__':
    app.run(debug=True)

