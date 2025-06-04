"""
import turtle as t
t.shape("turtle")
t.circle(50)
t.color("red")
t.pensize(3)
for i in range(4) :
    t.fd(100)
    t.left(90)
"""
"""
import turtle as t
t.shape("turtle")
n = 50
t.bgcolor("black")
t.color("green")
t.speed(0)
for x in range(n):
    t.circle(80)
    t.left(360/n)"
"""
import turtle as t
def turn_right() : 
    t.setheading(0)
    t.fd(10)
def turn_up() : 
    t.setheading(90)
    t.fd(10)
def turn_left() : 
    t.setheading(180)
    t.fd(10)
def turn_down() : 
    t.setheading(270)
    t.fd(10)
def turn_blank() : 
    t.clear()
t.shape("turtle")
t.speed(0)
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.onkeypress(turn_blank, "Escape")
t.listen()