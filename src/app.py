from sender import send_message
from weather_data import fetch_weather

email_sender = 'svetlana.automation2023@gmail.com'
email_password = 'akxglecarsafeded'
email_receiver = 'svetlanazemskova@gmail.com'
subject = 'Current Weather in Berlin and Jakarta'
api_key = '508fff3d42115d0a06add2db1afe3607'
cities = ["Berlin", "Jakarta"]

period_ms = 1000

def main():
    body = fetch_weather(api_key, cities)
    send_message(email_sender, email_password, email_receiver, subject, body)


if __name__ == "__main__":
    main()
