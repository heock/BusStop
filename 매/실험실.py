"""import turtle as t
t.speed(3)
t.penup()
t.bgcolor("red")
t.begin_fill()
t.goto(-200,-120)

t.pendown()
t.color("white")
t.forward(100)
t.right(72)
t.forward(100)
t.right(234)
t.forward(100)

t.end_fill
t.penup()
t.mainloop()"""



"""import turtle as t

t.speed(0)
t.bgcolor("darkgreen")  # 파키스탄 스타일 배경

# 큰 흰색 원 (초승달의 바탕)
t.penup()
t.goto(-50, 0)
t.color("white")
t.begin_fill()
t.circle(100)
t.end_fill()

# 작은 배경색 원 (겹쳐서 초승달 모양 만들기)
t.goto(-25, 0)
t.color("darkgreen")
t.begin_fill()
t.circle(90)
t.end_fill()

t.mainloop()
t = turtle.Turtle()
t.speed(0)

    # 독일 국기 그리기 (검정, 빨강, 노랑)
colors = ["black", "red", "yellow"]
y_position = 120  # 시작 위치

    # 각 색을 그리기
for color in colors:
    t.penup()
    t.goto(-200, y_position)
    t.pendown()
    t.begin_fill()
    t.color(color)
    for _ in range(2):
        t.forward(400)
        t.left(90)
        t.forward(80)  # 각 색의 높이
        t.left(90)
    t.end_fill()
    y_position -= 80  # 각 색이 80씩 내려가도록

    # 터틀 그래픽 창을 닫지 않도록 대기
turtle.done()"""

import turtle as t
t.speed(0)
t.penup()
t.goto(-50, 0)
t.color("black")
t.forward(30)
t.left(126)
t.forward(30)
t.right(72)

t.begin_fill()
t.circle(100)
t.end_fill()
t.mainloop

