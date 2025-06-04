import turtle as t

# 초기 설정
t.title('옥슬립앵초 꽃 그리기')
t.goto(0, 0)
t.speed(0)
t.bgcolor("cyan")

# 꽃잎을 그리는 부분
n = 6  # 꽃잎의 개수

# 꽃잎 크기와 색상 설정
sizes = [80, 60, 40, 20]  # 꽃잎 크기
colors = ["yellow", "white", "yellow", "white"]  # 꽃잎 색상

for i in range(4):  # 꽃잎을 4번 그리기 (크기별로)
    t.penup()
    t.goto(0, 0)
    t.color(colors[i])
    t.pendown()  # 펜 내리기
    
    size = sizes[i]  # 현재 꽃잎의 크기
    
    for x in range(n):  # 6개의 꽃잎 그리기
        t.begin_fill()
        t.circle(size, 120)  # 꽃잎의 크기와 각도 설정
        t.left(60)  # 꽃잎 간격 맞추기
        t.circle(size, 120)  # 두 번째 꽃잎
        t.left(60)  # 꽃잎 간격 맞추기
        t.end_fill()
        t.left(360 / n)  # 6개의 꽃잎을 그리기 위해 적절히 회전

t.mainloop()
