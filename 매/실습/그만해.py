"""import turtle
swidth, shelight = 500, 500
turtle.title("무지개색 원그리기")
turtle.shape("turtle")
turtle.setup(width = swidth + 50, height = shelight + 50)
turtle.screensize(swidth, shelight)
turtle.penup()
turtle.goto(0, -shelight/2)
turtle.pendown()
turtle.speed(100)
for radius in range(1, 250) : 
    if radius %7 == 0 :
        turtle.pencolor("red")
    elif radius %6 == 0 :
        turtle.pencolor("orange")
    elif radius %5 == 0 :
        turtle.pencolor("yellow")
    elif radius %4 == 0 :
        turtle.pencolor("green")
    elif radius %3 == 0 :
        turtle.pencolor("blue")
    elif radius %2 == 0 :
        turtle.pencolor("navyblue")
    else :
        turtle.pencolor("purple")
    turtle.circle(radius)
turtle.done() 
"""

import turtle
import random
sw, sh, ps, ex = 300, 300, 3, 0
r, g, b, an, di, cuX, cuY = [0] * 7
turtle.title("거북이가 맘대로 다니기")
turtle.shape("turtle")
turtle.pensize(ps)
turtle.setup(width = sw + 30, height = sh + 30)
turtle.screensize(sw, sh)
while True : 
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.pencolor((r, g, b))
    an = random.randrange(0, 360)
    di = random.randrange(1, 360)
    turtle.left(an)
    turtle.fd(di)
    cuX = turtle.xcor()
    cuY = turtle.ycor()

    if (-sw/2 <= cuX and cuY <= sw/2) and 

