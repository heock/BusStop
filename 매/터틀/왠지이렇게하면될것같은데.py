import turtle as t              #터틀을 t로 치환
t.title('옥슬립앵초 꽃 그리기')  #창의 이름을 '옥슬립앵초 꽃 그리기'로 정함.
t.goto(0,0)                     #시작 위치를 (0,0)으로 고정
t.speed(0)                      #이동속도를 가장 빠르게 함.
t.bgcolor("cyan")               #배경색을 'cyan'으로 지정함.
n = 6                           #꽃잎을 6개 그립니다.
m = 4                           #4겹으로 그립니다.
sizes = [80, 60, 40, 20]        #8~9행 딕셔너리 이용, 크기에 따라 'yellow'와 'cyan'을 번갈아 사용합니다. 
colors = ["yellow", "white", "yellow", "white"]
for i in range(m) :             #10~14행 반복문을 이용하여 색딕셔너리에 저장된 색을 이용합니다. 
    t.penup()                   
    t.goto(0, 0)
    t.pendown()
    t.color(colors[i])
    size = sizes[i]             #'size'라는 변수에 사이즈딕셔너리를 저장합니다.
    for x in range(n) :  #16~21행 이중반복문을 이용해 딕셔너리에 저장된 크기의 호를 그리고,이전에 결정된 색으로 채움.
        t.begin_fill()
        t.circle(size, 120)
        t.left(60)
        t.circle(size, 120)
        t.end_fill()
    
t.mainloop()                    #창이 꺼지지 않도록 합니다.



