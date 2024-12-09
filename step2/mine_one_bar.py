from bokeh.plotting import figure, show

# prepare some data
x = [0, 5, 10, 15, 20, 25]
y1 = [1, 2, 3, 4, 5, 6]

# create a new plot with a title and axis labels
p = figure(title="Mine lines example", x_axis_label="x", y_axis_label="y")

# add multiple renderers
p.vbar(x=x, top=y1, legend_label="Rate #1", color="blue", width=0.5, bottom=0)

# show the results
show(p)