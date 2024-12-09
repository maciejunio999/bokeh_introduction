from bokeh.plotting import figure, show

# prepare some data
x = [0, 5, 10, 15, 20, 25]
y1 = [1, 2, 3, 4, 5, 6]
y2 = [7, 6, 5, 4, 3, 2]
y3 = [8, 10, 9, 11, 12, 10]

# create a new plot with a title and axis labels
p = figure(title="Mine lines example", x_axis_label="x", y_axis_label="y")

# add multiple renderers
p.line(x, y1, legend_label="Line #1", color="blue", line_width=1)
p.line(x, y2, legend_label="Line #2", color="red", line_width=2)
p.line(x, y3, legend_label="Line #3", color="green", line_width=3)

# show the results
show(p)