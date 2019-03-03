"""
Routes and views for the flask application.
"""
import threading
import queue
from flask import request, render_template
from up_write.App import app
from up_write.DB.classes import StateRecord
from up_write.DB import session

REMOTE_HOST = "https://pyecharts.github.io/assets/js"


@app.route('/data_post', methods=['POST', 'GET'])
def data_post():
    state = StateRecord(light=request.json['light'])
    session.add(state)
    session.commit()
    session.close()
    return 'OK'


@app.route('/')
def hello():
    return render_template('my_template.html')
