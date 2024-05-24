

# Email Engine
- showcase OOP design (Modular Design:, Encapsulation, Reusability)

## dependencies
[Geopy Distance Documentation](https://geopy.readthedocs.io/en/stable/#module-geopy.distance)



```python

class EmailNotificationEngine:
    """
    Represents an engine for email notifications.

    Attributes:
        events (list): List of events to be processed.
        subscribers (list): List of subscribers to receive notifications.
        notify_list (dict): Dictionary to store events to notify subscribers.
    """

    def __init__(self, events: list, subscribers: list):
        """
        Initializes the EmailNotificationEngine instance.

        Parameters:
            events (list): List of events to be processed.
            subscribers (list): List of subscribers to receive notifications.
        """
        self.events = events
        self.subscribers = subscribers
        self.notify_list = {}

    def _send_notification(self, event_name: str):
        """
        Sends notification to subscribers.

        Parameters:
            event_name (str): The name of the event being processed.
        """

    def validate_birthday(self, event: dict, subscriber: dict):
        """
        Validates if the event falls within the subscriber's birthday range.

        Parameters:
            event (dict): The event to be validated.
            subscriber (dict): The subscriber whose birthday is being validated.
        """


    def validate_distance(self, event: dict, subscriber: dict):
        """
        Validates if the event is within a certain distance for the subscriber.

        Parameters:
            event (dict): The event to be validated.
            subscriber (dict): The subscriber whose distance from the event is being validated.
        """

    def process_events(self, validation_func, event_name):
        """
        Processes events using the specified validation function and sends notifications.

        Parameters:
            validation_func (Callable[[dict, dict], None]): The validation function to be applied to each event-subscriber combination.
            event_name (str): The name of the event being processed.
        """

```
