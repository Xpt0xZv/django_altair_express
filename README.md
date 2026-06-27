# Django Altair Express

A Django package that provides a reusable template tag for rendering Altair charts.

## Installation

```bash
pip install django-altair-express
```
or with uv:
```bash
uv add django-altair-express
```

Add the application to your `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    # ...
    'django_altair_express',
]
```

## Requirements for Vega

For the charts to render correctly, you **must** include the exact versions of the Vega, Vega-Lite, and Vega-Embed libraries in your HTML. Please add these scripts to your base template `<head>` or before the end of the `<body>`:

```html
<!-- Exact required versions for compatibility -->
<script src="https://cdn.jsdelivr.net/npm/vega@5.30.0"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@5.21.0"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@6.26.0"></script>
```

## Usage

In your Django view, create an Altair chart and pass it to the template context:

```python
import altair as alt
from django.shortcuts import render

def my_view(request):
    chart = alt.Chart(alt.Data(values=[{"x": 1, "y": 2}])).mark_point().encode(x='x:Q', y='y:Q')
    return render(request, 'my_template.html', {'chart': chart})
```

In your template (`my_template.html`), load the template tags and use the `render_altair` tag:

```html
{% load altair_express %}

<!DOCTYPE html>
<html>
<head>
    <!-- Include Vega scripts here -->
</head>
<body>
    <h1>My Chart</h1>
    <!-- Renders the container and javascript for the chart -->
    {% render_altair chart %}
</body>
</html>
```

The `render_altair` tag accepts:
- An Altair chart object (which implements `.to_json()`)
- A Python dictionary representing the Vega-Lite JSON specification
- A JSON string representing the Vega-Lite specification
