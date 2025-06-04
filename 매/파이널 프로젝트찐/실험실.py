
import turtle as T
from tool import propotion2_3
T.reset()
T.speed(0)
T.bgcolor("white")
T.title("일본국기 그리기")
propotion2_3()
T.penup()
T.goto(-100, -60)  
T.pendown()
T.color("red")
T.begin_fill()
T.circle(96)
T.end_fill()
T.hideturtle()
T.done()