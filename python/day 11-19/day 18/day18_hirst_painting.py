import random
import turtle
import turtle as t


"""
import colorgram as cg


colorgram = cg.extract("day18_hirst_painting.png", 88)

colors = []

for color in colorgram:
    if color.rgb.r > 220 and color.rgb.g > 220 and color.rgb.g > 220:
        pass
    else:
        colors.append((color.rgb.r, color.rgb.g, color.rgb.b))

print(colors)
"""


colors = [(213, 13, 9), (198, 12, 35), (197, 69, 20), (33, 90, 188), (43, 212, 71), (234, 148, 40), (33, 30, 152),
          (16, 22, 55), (66, 9, 49), (244, 39, 149), (65, 202, 229), (14, 205, 222), (63, 21, 10), (224, 19, 111),
          (229, 165, 8), (15, 154, 22), (245, 58, 16), (98, 75, 9), (248, 11, 9), (222, 140, 203), (68, 240, 161),
          (10, 97, 62), (5, 38, 33), (68, 219, 155), (238, 157, 212), (86, 77, 208), (86, 225, 235), (250, 8, 14),
          (242, 166, 157), (177, 180, 224), (36, 243, 159), (6, 81, 115), (11, 55, 248)]


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
