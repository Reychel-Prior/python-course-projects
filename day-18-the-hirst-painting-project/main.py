import colorgram
import turtle as t
import random

colors = colorgram.extract('image.jpg', 10)
colors_list = []

for current_color in range(10):
    r = colors[current_color].rgb.r
    g = colors[current_color].rgb.g
    b = colors[current_color].rgb.b

    color_tuple = (r, g, b)
    colors_list.append(color_tuple)

def random_color():
    return random.choice(colors_list)
# 10 x 10 dots
# spaced 50
# dot size 20

tilin = t.Turtle()
t.colormode(255)
tilin.penup()

# Initial coordinates
tilin.goto(-250,-250)

def draw_row(no_rows):
    for i in range(no_rows):
        tilin.color(random_color())
        tilin.dot(20)
        tilin.forward(50)


def next_row(no_rows):
    tilin.left(90)
    tilin.forward(50)
    tilin.left(90)
    tilin.forward(no_rows * 50)
    tilin.setheading(0)


for i in range(10):
    draw_row(10)
    next_row(10)

screen = t.Screen()
screen.exitonclick()