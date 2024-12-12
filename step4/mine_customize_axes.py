from bokeh.plotting import figure, show
from bokeh.models import NumeralTickFormatter, PrintfTickFormatter
from math import pi

# prepare some data
x = [1, 2, 3, 4, 5]
y = [4, 5, 5, 7, 2]

# create a plot
p = figure(
    y_range=(0, 15),
    title="Customized axes example",
    sizing_mode="stretch_both",
    max_width=1000,
    max_height=1000,
)

# add a renderer
p.scatter(x, y, size=10)

# format axes ticks
#   NumeralTickFormatter / PrintfTickFormatter
#   BasicTickFormatter — Default formatter for linear axes.
#   CategoricalTickFormatter — Default formatter for categorical axes.
#   DatetimeTickFormatter — Default formatter for datetime axes.
#   LogTickFormatter — Default formatter for log axes
p.yaxis[0].formatter = NumeralTickFormatter(format="$0.00")
p.xaxis[0].formatter = PrintfTickFormatter(format="%4.1e")

# change some things about the x-axis
p.xaxis.axis_label = "varaible a"
p.xaxis.axis_line_width = 2
p.xaxis.axis_line_color = "red"
p.xaxis.major_label_text_color = "orange"
p.xaxis.major_label_orientation = "horizontal"

# change some things about the y-axis
p.yaxis.axis_label = "variable b"
p.yaxis.major_label_text_color = "red"
p.xaxis.major_label_orientation = pi/4
p.yaxis.major_label_orientation = "vertical"
p.yaxis.axis_line_color = "orange"
p.yaxis.axis_line_width = 5

# change things on all axes
p.axis.minor_tick_in = -5
p.axis.minor_tick_out = 10

# show the results
show(p)