from flask_mail import Mail, Message


class MailSender:
    def __init__(self, app):
        self.mail = Mail(app)

    def send_mail(self, user_to, subject='', body=''):
        msg = Message(
            recipients=[user_to],
            body=body,
            subject=subject
        )
        self.mail.send(msg)
