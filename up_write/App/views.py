"""
Routes and views for the flask application.
"""
from flask import request
from up_write.App import app
from up_write.DB.classes import StateRecord
from up_write.DB import session


@app.route('/', methods=['POST', 'GET'])
def data_post():
    state = StateRecord(light=request.json['light'])
    session.add(state)
    session.commit()
    session.close()
    return 'OK'
