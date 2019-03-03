"""
Routes and views for the flask application.
"""
from flask import render_template, request
from down_read.App import app
from down_read.DB.classes import StateRecord
from down_read.DB import session
import json

REMOTE_HOST = "https://pyecharts.github.io/assets/js"


@app.route('/')
def hello():
    return render_template('my_template.html')


@app.route('/test', methods=['POST'])
def get_data():
    jsonData = {}
    x = []
    y = []
    states = session.query(StateRecord).filter().all()
    session.close()
    for state in states:
        x.append(str(state.datetime))
        y.append(state.light)
    jsonData['datetime'] = x
    jsonData['values'] = y
    _json = json.dumps(jsonData)

    return _json
