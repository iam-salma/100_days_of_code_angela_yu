import os
import smtplib
from dotenv import load_dotenv
from twilio.rest import Client
load_dotenv()

class NotificationManager:
    def __init__(self):
        self.email = os.getenv("SMTP_EMAIL")
        self.password = os.getenv("SMTP_PASSWORD")
        self.twilio_virtual_number = os.getenv("TWILIO_VIRTUAL_NUMBER")
        self.twilio_verified_number = os.getenv("TWILIO_VERIFIED_NUMBER")
        self.client = Client(os.getenv("TWILIO_SID"), os.getenv("TWILIO_AUTH_TOKEN"))

    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_=self.twilio_virtual_number,
            body=message_body,
            to=self.twilio_verified_number
        )
        print(message.sid)

    def send_emails(self, email_list, email_body):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=self.email, password=self.password)
            for email in email_list:
                connection.sendmail(
                    from_addr=self.email,
                    to_addrs=email,
                    msg=email_body
                )


