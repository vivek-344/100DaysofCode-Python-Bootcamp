import turtle

s = turtle.Screen()
t = turtle.Turtle()


def fd():
    t.fd(10)


def bk():
    t.bk(10)


def cw():
    h = t.heading()
    t.setheading(h+5)


def ccw():
    h = t.heading()
    t.setheading(h-5)


def clear():
    turtle.resetscreen()
    t.home()


s.listen()
s.onkeypress(key="w", fun=fd)
s.onkeypress(key="s", fun=bk)
s.onkeypress(key="a", fun=ccw)
s.onkeypress(key="d", fun=cw)
s.onkeypress(key="c", fun=clear)
s.exitonclick()
