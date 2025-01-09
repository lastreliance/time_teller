import flask
from waitress import serve

from api import TimeTeller


HOST = "0.0.0.0"
PORT = 80


def main():
    app = flask.Flask(__name__)
    app.add_url_rule("/time", view_func=TimeTeller.as_view("time/seconds"))

    serve(app, host=HOST, port=PORT)


if __name__ == "__main__":
    main()
