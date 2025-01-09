import time
import flask.views


class TimeTeller(flask.views.MethodView):
    @staticmethod
    def get():
        return str(round(time.time())), 200
