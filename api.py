import time
import flask.views


class Homepage(flask.views.MethodView):
    @staticmethod
    def get():
        return flask.render_template("homepage.html")


class TimeTeller(flask.views.MethodView):
    @staticmethod
    def get():
        return str(round(time.time())), 200
