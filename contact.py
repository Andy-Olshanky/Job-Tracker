import smtplib
import os
from twilio.rest import Client


def send_email(subject, body, recipient):
    ADD = os.environ.get('EMAIL_ADDRESS')
    PASS = os.environ.get('EMAIL_PASSWORD')
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(ADD, PASS)

        msg = f'Subject:{subject}\n\n{body}'

        smtp.sendmail(ADD, recipient, msg)


# def send_text(text, recipient):
#     SID = os.environ.get('TWILIO_SID')
#     TOKEN = os.environ.get('TWILIO_TOKEN')
#     PHONE = os.environ.get('TWILIO_PHONE')
#     client = Client(SID, TOKEN)
#     msg = client.messages.create(body=text, from_=PHONE, to=recipient)
#     print(msg.sid)

