class NotificationManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(NotificationManager, cls).__new__(cls)
        return cls._instance

    def send_notification(self, message, strategy):
        strategy.send(message)

# Strategy Pattern
class NotificationStrategy:
    def send(self, message):
        pass

class EmailNotificationStrategy(NotificationStrategy):
    def send(self, message):
        print(f"Sending Email Notification: {message}")

class SMSNotificationStrategy(NotificationStrategy):
    def send(self, message):
        print(f"Sending SMS Notification: {message}")

class PushNotificationStrategy(NotificationStrategy):
    def send(self, message):
        print(f"Sending Push Notification: {message}")

def main():
    # Singleton Pattern
    notification_manager = NotificationManager()

    # Strategy Pattern
    email_strategy = EmailNotificationStrategy()
    sms_strategy = SMSNotificationStrategy()
    push_strategy = PushNotificationStrategy()


    notification_manager.send_notification("important news!", email_strategy)
    notification_manager.send_notification("planned meeting reminder!", sms_strategy)
    notification_manager.send_notification("new notification!", push_strategy)

if __name__ == "__main__":
    main()
