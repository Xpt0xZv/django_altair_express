import pytest
from django.template import Template, Context
import altair as alt
import json

def test_render_altair_with_chart():
    chart = alt.Chart(alt.Data(values=[{"x": 1, "y": 2}])).mark_point().encode(x='x:Q', y='y:Q')
    
    template = Template(
        "{% load altair_express %}\n"
        "{% render_altair chart %}"
    )
    context = Context({"chart": chart})
    rendered = template.render(context)
    
    assert '<div id="vis-' in rendered
    assert 'vegaEmbed(' in rendered
    assert '"point"' in rendered # Chart content

def test_render_altair_with_dict():
    chart_dict = {
        "mark": "bar",
        "data": {"values": [{"a": "A", "b": 28}]}
    }
    
    template = Template(
        "{% load altair_express %}\n"
        "{% render_altair chart %}"
    )
    context = Context({"chart": chart_dict})
    rendered = template.render(context)
    
    assert '<div id="vis-' in rendered
    assert 'vegaEmbed(' in rendered
    assert '"mark": "bar"' in rendered

def test_render_altair_with_json_string():
    chart_json = json.dumps({
        "mark": "line",
        "data": {"values": [{"a": "A", "b": 28}]}
    })
    
    template = Template(
        "{% load altair_express %}\n"
        "{% render_altair chart %}"
    )
    context = Context({"chart": chart_json})
    rendered = template.render(context)
    
    assert '<div id="vis-' in rendered
    assert 'vegaEmbed(' in rendered
    assert '"mark": "line"' in rendered

def test_render_altair_invalid_input():
    template = Template(
        "{% load altair_express %}\n"
        "{% render_altair chart %}"
    )
    context = Context({"chart": 12345}) # Invalid integer
    with pytest.raises(ValueError, match="Invalid chart object"):
        template.render(context)
