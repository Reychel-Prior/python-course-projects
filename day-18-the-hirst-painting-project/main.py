import colorgram
import turtle as t

colors = colorgram.extract('image.jpg', 10)
colors_list = []

for current_color in range(10):
    r = colors[current_color].rgb.r
    g = colors[current_color].rgb.g
    b = colors[current_color].rgb.b

    color_tuple = (r, g, b)
    colors_list.append(color_tuple)

# 10 x 10 dots
# spaced 50
# dot size 20

tilin = t.Turtle()




screen = t.Screen()
screen.exitonclick()