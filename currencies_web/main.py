from flask import Flask, render_template, request

from currencies.main import *
from datetime import datetime

from db import session, Currency

app = Flask(__name__)
currencies_service = Currencies()


@app.route("/")
def index():

    currencies = session.query(Currency).all()
    current_time = datetime.now()

    return render_template(
        "index.html",
        current_time=current_time,
        currencies=currencies
    )


@app.route("/info")
def info():
    return render_template(
        "info.html"
    )


@app.route('/currencies/<code>')
def currency_page(code):
    current_time = datetime.now()

    current_date = current_time.strftime("%Y-%m-%d")
    date = request.args.get('date', )

    rates = currencies_service.get_currencies_for(code, date or "latest")

    return render_template(
        "currency_page.html",
        currency_code=code,
        rates=rates,
        current_date=current_date,
        date=date or current_date
    )


app.run(
    port=8000,
    debug=True
)