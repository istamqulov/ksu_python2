
import flask
from currencies.main import *
from datetime import datetime

app = flask.Flask(__name__)
currencies_service = Currencies()


@app.route("/")
def index():
    currencies_data = currencies_service.load_currencies()

    current_time = datetime.now()
    print(currencies_data.items())

    return flask.render_template(
        "index.html",
        current_time=current_time,
        currencies=currencies_data.items()
    )

@app.route("/info")
def info():
    return flask.render_template(
        "info.html"
    )


@app.route('/currencies/<code>')
def currency_page(code):
    return code

app.run(
    port=8000,
    debug=True
)