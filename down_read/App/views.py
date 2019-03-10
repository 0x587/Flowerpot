"""
Routes and views for the flask application.
"""
import threading
import json
import time
from flask import render_template, url_for, redirect
from down_read.App import app
from down_read.DB.classes import StateRecord
from down_read.DB import session
from down_read.LocalCacheDB import session as LCsession
from down_read.LocalCacheDB.classes import StateRecord as LCStateRecord

REMOTE_HOST = "https://pyecharts.github.io/assets/js"
cacheDBlock = threading.Lock()
DBlen = 0


def cache_data():
    global timer, DBlen
    nt = time.time()
    print('start loading')

    # download data
    down_data = session.query(StateRecord).filter().all()
    DBlen = len(down_data)
    print('download data spend %s s' % str(time.time() - nt))
    nt = time.time()
    cacheDBlock.acquire()

    # empty data
    LCsession.query(LCStateRecord).filter().delete()
    LCsession.commit()
    print('empty data spend %s s' % str(time.time() - nt))
    # write data
    nt = time.time()
    for data_index in range(len(down_data)):
        down_data[data_index] = LCStateRecord(down_data[data_index].light, down_data[data_index].datetime)
    LCsession.bulk_save_objects(down_data)
    LCsession.commit()
    print('write data spend %s s' % str(time.time() - nt))
    LCsession.close()
    cacheDBlock.release()
    timer = threading.Timer(10, cache_data)
    timer.start()


cache_data()


def get_data():
    global DBlen
    jsonData = {}
    x = []
    y = []
    get_data_flag = False
    states = []
    cacheDBlock.acquire()
    while not get_data_flag:
        try:
            t = time.time()
            states = LCsession.query(LCStateRecord).filter(LCStateRecord.record_id >= DBlen - 1000).all()
        except Exception:
            print('get data failed')
            LCsession.close()
        else:
            get_data_flag = True
            LCsession.close()
            print('get data spend %s' % str((time.time() - t)*1000)+'ms')
    for state in states:
        x.append(str(state.datetime))
        y.append(state.light)
    jsonData['datetime'] = x
    jsonData['values'] = y
    _json = json.dumps(jsonData)
    cacheDBlock.release()
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
