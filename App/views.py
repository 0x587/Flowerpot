"""
Routes and views for the flask application.
"""
from flask import render_template, request
from pyecharts_javascripthon.api import TRANSLATOR
from pyecharts import Bar
from App import app
from jinja2 import Environment, PackageLoader
from DB.classes import StateRecord
from DB import session

REMOTE_HOST = "https://pyecharts.github.io/assets/js"


def bar_chart():
    bar = Bar("我的第一个图表", "这里是副标题")
    bar.add(
        "服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90]
    )
    return bar


@app.route('/data_post', methods=['POST', 'GET'])
def data_post():
    state = StateRecord(light=request.json['light'])
    session.add(state)
    session.commit()
    print('write')
    return 'OK'


@app.route('/', methods=['POST', 'GET'])
def home():
    # return render_template('Home.html')
    a = request.json
    print(a)
    print(type(a))
    return 'Welcome!'


@app.route('/rev', methods=['PUT'])
def receiver():
    print('Get rev')
    temp_record = StateRecord()
    session.add(temp_record)
    session.commit()
    return '200'  # 200:request is approved 300:request is rejected



def main():
    bar = bar_chart()
    jinja_env = Environment(loader=PackageLoader('App', 'templates'))

    javascript_snippet = TRANSLATOR.translate(bar.options)
    chart_temp_env = jinja_env.get_template('chart_block.html')
    chart = chart_temp_env.render(
        width='100%',
        height='600px',
        chart_id=bar.chart_id,
        renderer=bar.renderer,
        custom_function=javascript_snippet.function_snippet,
        options=javascript_snippet.option_snippet,
    )
    return render_template(
        'Home.html',
        host=REMOTE_HOST,
        script_list=bar.get_js_dependencies(),
        my_chart=chart,
    )
    # return chart1
