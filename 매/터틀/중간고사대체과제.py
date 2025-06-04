"""import turtle as t
t.title('옥슬립앵초 꽃 그리기')
t.goto(0,0)
t.speed(0)
t.bgcolor("cyan")
t.color("yellow")
n = 6
for x in range(n):
    
    t.begin_fill()
    t.left(120)
    t.circle(80, 120)
    t.left(60)
    t.circle(80, 120)
    t.end_fill()
t.penup()
t.goto(0,0)
t.color("white")
t.pendown()

for x in range(n):
    t.begin_fill()
    t.left(120)
    t.circle(60, 120)
    t.left(60)
    t.circle(60, 120)
    t.end_fill()

t.penup()
t.goto(0,0)
t.color("yellow")
t.pendown()
for x in range(n):
    t.begin_fill()
    t.left(120)
    t.circle(40, 120)
    t.left(60)
    t.circle(40, 120)
    t.end_fill()
t.penup()
t.goto(0,0)
t.color("white")
t.pendown()
for x in range(n):
    t.begin_fill()
    t.left(120)
    t.circle(20, 120)
    t.left(60)
    t.circle(20, 120)
    t.end_fill()
t.mainloop()
"""
"""
def ogamdo(num) :
    for i in range(1, num + 1):
        print('제 {0}의 아해'.format(i))
        if i == 5:
            return
            """
import random
def getnumber():
    return random.randrange(1,46)
lotto = []
num = 0
print("**로또 추첨을 시작합니다.**\n");
while True :
    num = getnumber()
    if lotto.count(num) == 0 :
        lotto.append(num)
    if len(lotto) >= 6 :
        break
print("추첨된 로또번호 ==> ", end = '')
lotto.sort()
for i in range(0, 6):
    print("%d "%lotto[i], end = '')