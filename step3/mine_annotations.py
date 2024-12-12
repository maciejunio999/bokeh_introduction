import random

from bokeh.models import BoxAnnotation
from bokeh.plotting import figure, show

# generate some data (1-50 for x, random values for y)
x = list(range(0, 51))
y = random.sample(range(0, 100), 51)

# create new plot
p = figure(title="Box annotation example")

# add line renderer
line = p.line(x, y, line_color="#a8a7a7", line_width=5)

# add box annotations
lower_box = BoxAnnotation(top=20, fill_alpha=0.2, fill_color="#615256")
low_box = BoxAnnotation(bottom=20, top=40, fill_alpha=0.35, fill_color="#f7f48b")
mid_box = BoxAnnotation(bottom=40, top=60, fill_alpha=0.8, fill_color="#f2496d")
high_box = BoxAnnotation(bottom=60, top=80, fill_alpha=0.35, fill_color="#f7f48b")
higher_box = BoxAnnotation(bottom=80, fill_alpha=0.2, fill_color="#615256")

# add boxes to existing figure
p.add_layout(lower_box)
p.add_layout(low_box)
p.add_layout(mid_box)
p.add_layout(high_box)
p.add_layout(higher_box)

# show the results
show(p)