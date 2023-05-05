import os

from flask import Flask, render_template, redirect, url_for
from flask_mail import Mail, Message

from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
# app.debug = True

app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT'))
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS', False)
app.config['MAIL_USE_SSL'] = os.getenv('MAIL_USE_SSL', False)
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')

app.config['MAIL_SUPPRESS_SEND'] = False

mail = Mail(app)


def send_mail(user_to, subject='', body=''):
    msg = Message(
        recipients=[user_to],
        body=body,
        subject=subject
    )
    mail.send(msg)


@app.route('/')
def main():
    return redirect(url_for('menu'))


@app.route('/menu')
def menu():
    return render_template('menu.html')


@app.route('/landing_pages/covid-19')
def landing_page_covid_19():
    return render_template('landing_pages/covid-19.html')


@app.route('/send_test_message')
def send_test_mail_message():
    result = 'Message sent successfully!'
    send_mail(
        'hristenko.evgeniy@yandex.ru',
        subject='Test email message.',
        body='Hello Flask'
    )
    return result


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000')

