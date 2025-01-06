import time
import flask.views


class TimeTeller(flask.views.MethodView):
    @staticmethod
    def get():
        return round(time.time()), 200
