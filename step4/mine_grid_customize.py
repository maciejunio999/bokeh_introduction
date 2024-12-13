from bokeh.plotting import figure, show
import random
from datetime import datetime, timedelta

from bokeh.models import DatetimeTickFormatter, NumeralTickFormatter

# generate list of dates (today's date in subsequent weeks)
x = [(datetime.now() + timedelta(day * 7)) for day in range(0, 26)] # dates

# generate 25 random data points
y = random.sample(range(0, 100), 26)

# create a plot
p = figure(
    title="Customized grid lines example",
    sizing_mode="stretch_width",
    max_width=900,
    height=750,
)

# add renderers
p.scatter(x, y, size=8)
p.line(x, y, color="navy", line_width=1)

# format axes ticks
p.yaxis[0].formatter = NumeralTickFormatter(format="$0.00")
p.xaxis[0].formatter = DatetimeTickFormatter(months="%b %Y")

# add a renderer
p.line(x, y, line_color="green", line_width=2)

# add bands to the y-grid
p.ygrid.band_fill_color = "olive"
p.ygrid.band_fill_alpha = 0.1

# define vertical bonds
p.xgrid.bounds = (2, 4)

# change things only on the x-grid
p.xgrid.grid_line_color = "red"

# change things only on the y-grid
p.ygrid.grid_line_alpha = 0.8
p.ygrid.grid_line_dash = [6, 4]

# change the fill colors
p.background_fill_color = (204, 255, 255)
p.border_fill_color = (102, 204, 255)
p.outline_line_color = (0, 0, 255)

p.toolbar_location = "below"
p.toolbar.logo = None

# show the results
show(p)