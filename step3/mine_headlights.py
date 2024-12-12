from bokeh.plotting import figure, show

# prepare some data
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

# create new plot
p = figure(title="Headline example")

# add line renderer with a legend
p.line(x, y, legend_label="variable", line_width=3)

# change headline location to the right
p.title_location = "right"

# change headline text
p.title.text = "Additional text example"

# style the headline
p.title.text_font_size = "17px"
p.title.align = "left"
p.title.background_fill_color = "darkgrey"
p.title.text_color = "black"

# show the results
show(p)