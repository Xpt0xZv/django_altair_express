import json
import uuid

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def render_altair(chart):
    """
    Renders an Altair chart or its JSON specification into an HTML container.
    """
    if hasattr(chart, "to_json"):
        spec_json = chart.to_json()
    elif isinstance(chart, str):
        # Assume it's a JSON string
        spec_json = chart
    elif isinstance(chart, dict):
        spec_json = json.dumps(chart)
    else:
        raise ValueError(
            "Invalid chart object provided to render_altair tag. Must be an Altair chart, dict, or JSON string.")

    # Generate a unique ID for the chart container
    vis_id = f"vis-{uuid.uuid4().hex[:12]}"

    html = f"""
<div id="{vis_id}"></div>
<script type="text/javascript">
  (function() {{
    var spec = {spec_json};
    vegaEmbed('#{vis_id}', spec).then(function(result) {{
      // Access the Vega view instance as result.view
    }}).catch(console.error);
  }})();
</script>
"""
    return mark_safe(html)
