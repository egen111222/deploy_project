from flask_mail import Mail
from flask_mail import Message
from dotenv import load_dotenv
import os

mail = Mail()
load_dotenv()

def send_mail(result_source,
              title="",
              body=""):
    message = Message(title,
                      sender=os.environ["MAIL_USERNAME"],
                      recipients=[result_source],
                      body=body)
    mail.send(message)
