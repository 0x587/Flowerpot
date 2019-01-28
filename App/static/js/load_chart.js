


//< div id = "{{ chart_id }}" style = "width:{{ my_width }};height:{{ my_height }}px;" > < /div>
function load_chart(chart_id, renderer, option) {
    window.onload = function () 
    {
        setTimeout(function () 
        {
            var This_chart_id = echarts.init(document.getElementById(chart_id), null, {renderer:renderer});
            {{ custom_function }}
            This_chart_id.setOption(option);
            window.onresize = function () 
            {
                This_chart_id.resize();
            };
        }, 1000);
    }
}

    