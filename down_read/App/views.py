"""
Routes and views for the flask application.
"""
import threading
import json
from flask import render_template, url_for, redirect
from down_read.App import app
from down_read.DB.classes import StateRecord
from down_read.DB import session

REMOTE_HOST = "https://pyecharts.github.io/assets/js"


def get_data():
    jsonData = {}
    x = []
    y = []
    data_flag = False
    while not data_flag:

        try:
            states = session.query(StateRecord).filter().all()
        except Exception:
            print('get data failed')
            session.close()
        else:
            data_flag = True
    session.close()
    for state in states[-50:-1]:
        x.append(str(state.datetime))
        y.append(state.light)
    jsonData['datetime'] = x
    jsonData['values'] = y
    _json = json.dumps(jsonData)
    return _json


class DataThread(threading.Thread):
    result = None

    def __init__(self, func, args=()):
        super(DataThread, self).__init__()
        self.func = func
        self.args = args

    def run(self):
        self.result = self.func()

    def get_result(self):
        return self.result


@app.route('/')
def hello():
    return render_template('my_template.html')


@app.route('/test', methods=['GET'])
def return_data():
    thread = DataThread(func=get_data)
    # thread.setDaemon(True)
    thread.start()
    thread.join()
    back = thread.get_result()
    if back is not None:
        return thread.get_result()
    else:
        return redirect(url_for('return_data'))


@app.route('/a')
def a():
    return '1'
