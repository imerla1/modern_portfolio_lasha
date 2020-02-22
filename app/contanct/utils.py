from flask_mail import Message
from app import mail
from app.config import Config

cfg = Config()


def send_mail(title, sender_name, body):
    msg = Message(f'From {sender_name} title {title}', sender=cfg.MAIL_USERNAME,
                  recipients=['otbtestcase@yahoo.com'])
    msg.body = body
    mail.send(msg)
