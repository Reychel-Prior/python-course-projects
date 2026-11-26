import colorgram

colors = colorgram.extract('image.jpg', 10)
colors_list = []

for current_color in range(10):
    r = colors[current_color].rgb.r
    g = colors[current_color].rgb.g
    b = colors[current_color].rgb.b

    color_tuple = (r, g, b)
    colors_list.append(color_tuple)

print(colors_list)