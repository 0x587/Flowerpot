"""
Routes and views for the flask application.
"""
from flask import render_template, request, jsonify
from pyecharts_javascripthon.api import TRANSLATOR
from pyecharts import Bar
from App import app
from DB.classes import StateRecord
from DB import session
import json

REMOTE_HOST = "https://pyecharts.github.io/assets/js"


@app.route('/data_post', methods=['POST', 'GET'])
def data_post():
    try:
        state = StateRecord(light=request.json['light'])
        session.add(state)
        session.commit()
        session.close()
    finally:
        pass
    return 'OK'


@app.route('/')
def hello():
    return render_template('my_template.html')


@app.route('/test', methods=['POST'])
def my_echart():
    # 转换成JSON数据格式
    jsonData = {}
    x = []
    y = []
    states = session.query(StateRecord).filter().all()
    session.close()
    for state in states:
        x.append(str(state.datetime))
        y.append(state.light)
    jsonData['xdays'] = x
    jsonData['yvalues'] = y
    j = json.dumps(jsonData)

    # 在浏览器上渲染my_template.html模板（为了查看输出的数据）
    return (j)


@app.route('/home')
def receiver():
    chart_list, script_list = render_charts([bar_chart(), bar_chart()])
    return render_template(
        'Home.html',
        host=REMOTE_HOST,
        chart1=chart_list[0],
        chart2=chart_list[1],
        script_list=script_list,
    )


@app.route("/chart")
def chart():
    _bar = bar_chart()
    javascript_snippet = TRANSLATOR.translate(_bar.options)
    return render_template(
        "chart_block.html",
        renderer=_bar.renderer,
        custom_function=javascript_snippet.function_snippet,
        options=javascript_snippet.option_snippet,
        script_list=_bar.get_js_dependencies(),
    )


def bar_chart():
    bar = Bar("我的第一个图表", "这里是副标题")
    bar.add(
        "服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [10, 20, 36, 10, 75, 90]
    )
    return bar


def render_charts(charts):
    chart_htmls = []
    script_list = []
    for _chart in charts:
        javascript_snippet = TRANSLATOR.translate(_chart.options)
        chart_html = render_template(
            'chart_block.html',
            chart_id=_chart.chart_id,
            host=REMOTE_HOST,
            renderer=_chart.renderer,
            custom_function=javascript_snippet.function_snippet,
            options=javascript_snippet.option_snippet, )
        script_list.append(_chart.get_js_dependencies())
        chart_htmls.append(chart_html)
    return chart_htmls, script_list[0]
