from flask import Flask, render_template, redirect , url_for


app = Flask(__name__)


@app.route('/')
def main():
    return redirect(url_for('menu'))


@app.route('/menu')
def menu():
    return render_template('menu.html')


@app.route('/landing_pages/covid-19')
def landing_page_covid_19():
    return render_template('landing_pages/covid-19.html')


if __name__ == '__main__':
    app.run()
