import flask
from waitress import serve

from api import TimeTeller, Homepage


HOST = "0.0.0.0"
PORT = 80


def main():
    app = flask.Flask(__name__)
    app.add_url_rule("/time", view_func=TimeTeller.as_view("time/seconds"))
    app.add_url_rule("/", view_func=Homepage.as_view("homepage"))

    print(f"SERVER RUNNING ON PORT {PORT}")

    serve(app, host=HOST, port=PORT)


if __name__ == "__main__":
    main()
