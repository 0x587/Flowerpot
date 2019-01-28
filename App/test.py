import cProfile
from pyecharts_javascripthon.api import TRANSLATOR
from pyecharts import Bar
from jinja2 import Environment, PackageLoader
import pstats


def bar_chart():
    bar = Bar("我的第一个图表", "这里是副标题")
    bar.add(
        "服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90]
    )
    return bar


_bar = bar_chart()
javascript_snippet = TRANSLATOR.translate(_bar.options)

env = Environment(loader=PackageLoader('App', 'templates'))


def test():
    for i in range(10000):
        print(i)
        temp = env.get_template('chart_block.html')
        temp.render(
            width='100%',
            height='600px',
            chart_id=_bar.chart_id,
            renderer=_bar.renderer,
            custom_function=javascript_snippet.function_snippet,
            options=javascript_snippet.option_snippet,
        )


if __name__ == '__main__':
    cProfile.run('test()', filename="result.out")
    p = pstats.Stats("result.out")
    p.strip_dirs().sort_stats("cumulative").print_stats(5)
