"""
Routes and views for the flask application.
"""
from flask import render_template
from pyecharts_javascripthon.api import TRANSLATOR
from App import app
from pyecharts import Bar
from jinja2 import Environment, PackageLoader

REMOTE_HOST = "https://pyecharts.github.io/assets/js"


def bar_chart():
    bar = Bar("我的第一个图表", "这里是副标题")
    bar.add(
        "服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90]
    )
    return bar


@app.route('/')
@app.route('/home')
def home():
    return render_template('Home.html')


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
