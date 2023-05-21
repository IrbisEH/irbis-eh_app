import os
from flask import Flask, render_template, redirect, url_for, request, jsonify
from utils.MailSender import MailSender
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.debug = True

app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT'))
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS', False)
app.config['MAIL_USE_SSL'] = os.getenv('MAIL_USE_SSL', False)
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')

app.config['MAIL_SUPPRESS_SEND'] = False

MailSender = MailSender(app)

# app.add_('../landing_page_covid-19')

@app.route('/')
def main():
    return redirect(url_for('menu'))


@app.route('/menu')
def menu():
    return render_template('menu.html')

# /Users/evgenijhristenko/irbis-eh_app/irbis-eh_app/templates/landing_pages/landing_page_covid-19/covid-19.html
@app.route('/landing_pages/covid-19')
def landing_pages_covid_19():
    return render_template('landing_pages/landing_page_covid-19/covid-19.html')


@app.route('/games/conwaysGame')
def games_conways_game():
    return render_template('games/conwaysGame.html')


@app.route('/send_test_message')
def send_test_mail_message():
    result = 'Message sent successfully!'
    MailSender.send_mail(
        'hristenko.evgeniy@yandex.ru',
        subject='Test email message.',
        body='Hello Flask'
    )
    return result


@app.route('/send_covid_email', methods=['POST'])
def send_covid_email():
    email = request.json.get('email')
    MailSender.send_mail(
        email,
        subject='COVID-19 landing page',
        body='Thank you for visiting the COVID-19 page.\nMore projects can be seen on irbis-eh.space'
    )
    return jsonify({"message": "Email отправлен: {}".format(email)})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='3000')

