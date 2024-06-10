import random
import turtle
from turtle import Turtle, Screen

t = Turtle()
turtle.colormode(255)


"""Challenge No. 1"""
for _ in range(10):
    t.home()
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()


"""Challenge No. 2"""
def shape(angle):
    t.home()
    t.forward(100)
    while t.distance((0.00, 0.00)) > 1:
        t.left(angle)
        t.forward(100)


choice = input("Which shape do you want to print?\n").lower()

shapes = {
    "triangle": 120,
    "square": 90,
    "pentagon": 72,
    "hexagon": 60,
    "heptagon": 51.4285714286,
    "octagon": 45,
    "nonagon": 40,
    "decagon": 36
}

selected_angle = shapes.get(choice, None)
if selected_angle is not None:
    shape(selected_angle)
else:
    print("Invalid choice")


"""Challenge No. 3"""
def shape(sides):
    angle = 360/sides
    t.home()
    t.forward(100)
    while t.distance((0.00, 0.00)) > 1:
        t.left(angle)
        t.forward(100)


colors = appealing_colors = ['red', 'green', 'blue', 'cyan', 'magenta', 'yellow', 'orange', 'purple', 'sky blue',
                             'light green', 'light blue', 'pink', 'deep pink', 'coral', 'sea green', 'lime green',
                             'teal', 'turquoise', 'lavender', 'peach puff']

for i in range(3, 11):
    t.color(random.choice(colors))
    shape(i)


"""Challenge No. 4"""
colors = appealing_colors = ['red', 'green', 'blue', 'cyan', 'magenta', 'yellow', 'orange', 'purple', 'sky blue',
                             'light green', 'light blue', 'pink', 'deep pink', 'coral', 'sea green', 'lime green',
                             'teal', 'turquoise', 'lavender', 'peach puff']

t.width(7)
while True:
    angle = [0, 90, 180, 270]
    t.color(random.choice(colors))
    t.left(random.choice(angle))
    t.forward(30)
    t.speed("fastest")


"""Challenge No. 5"""
def color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    randcolor = (r, g, b)
    return randcolor


t.width(7)
while True:
    angle = [90, 180, 270]
    t.color(color())
    t.left(random.choice(angle))
    t.forward(30)
    t.speed("fastest")


"""Challenge No. 6"""
def color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    randcolor = (r, g, b)
    return randcolor


t.width(3)
t.speed("fastest")
for _ in range(0, 72):
    t.color(color())
    t.circle(100)
    heading = t.heading()
    t.setheading(heading + 5)


Screen().exitonclick()
