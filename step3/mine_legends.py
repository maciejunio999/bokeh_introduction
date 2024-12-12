from bokeh.plotting import figure, show

# prepare some data
x = [1, 2, 3, 4, 5]
y1 = [3.5, 5.25, 5, 6.75, 2]
y2 = [3, 6, 4.5, 7, 1]

# create a new plot
p = figure(title="Legend example")

# add circle renderer with legend_label arguments
line = p.line(x, y1, legend_label="variable", line_color="black", line_width=5)
circle = p.scatter(
    x,
    y2,
    marker="circle",
    size=60,
    legend_label="Objects",
    fill_color="green",
    fill_alpha=0.2,
    line_color="black",
)

# display legend in top left corner (default is top right corner)
p.legend.location = "top_left"

# add a title to your legend
p.legend.title = "Some info"

# change appearance of legend text
p.legend.label_text_font = "times"
p.legend.label_text_font_style = "italic"
p.legend.label_text_color = "navy"

# change border and background of legend
p.legend.border_line_width = 3
p.legend.border_line_color = "navy"
p.legend.border_line_alpha = 0.8
p.legend.background_fill_color = "navy"
p.legend.background_fill_alpha = 0.2

# show the results
show(p)