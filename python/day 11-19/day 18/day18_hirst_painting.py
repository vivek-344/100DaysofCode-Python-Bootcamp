import random
import turtle
import turtle as t
import colorgram as cg


colorgram = cg.extract("day18_hirst_painting.png", 88)
colors = []
for color in colorgram:
    colors.append((color.rgb.r, color.rgb.g, color.rgb.b))

# remove shades of white
for _ in range(0, 3):
    colors.pop(0)


t = t.Turtle()
turtle.colormode(255)

t.home()
t.pensize(20)
t.shape("circle")
t.penup()
t.speed("fastest")
for i in range(-5, 5):
    t.sety(i * 50)
    for j in range(-5, 5):
        t.setx(j*50)
        color = random.choice(colors)
        t.color(color)
        t.stamp()
        t.penup()


turtle.exitonclick()
