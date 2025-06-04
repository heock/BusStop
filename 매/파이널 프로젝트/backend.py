import turtle
import time
from tool import propotion3_5

def germany_flag():
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)

    propotion3_5(t)

    colors = ["black", "red", "yellow"]
    y_position = 120

    for color in colors:
        t.penup()
        t.goto(-200, y_position)
        t.pendown()
        t.begin_fill()
        t.color(color)
        for _ in range(2):
            t.forward(400)
            t.left(90)
            t.forward(80)
            t.left(90)
        t.end_fill()
        y_position -= 80

    time.sleep(2)
    screen.bye()











          







