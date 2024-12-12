from bokeh.io import curdoc
from bokeh.plotting import figure, show

# prepare some data
x = [1, 2, 3, 4, 5]
y = [4, 5, 5, 7, 2]

# apply theme to current document
curdoc().theme = "caliber" # caliber, dark_minimal, light_minimal, night_sky, and contrast

# create a plot
p = figure(
    title="Plot sizing example",
    width=950,
    height=750,
    x_axis_label="x",
    y_axis_label="y",
)

# add a renderer
p.line(x, y)

# show the results
show(p)