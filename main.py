import flask

from api import TimeTeller


def main():
    app = flask.Flask(__name__)
    app.add_url_rule("/time", view_func=TimeTeller.as_view("time/seconds"))
    app.run(host="0.0.0.0", port=80)


if __name__ == "__main__":
    main()
