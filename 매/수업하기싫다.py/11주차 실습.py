"""def selfcall() :
    print('하', end = '')
    selfcall()
selfcall()"""
"""나는야 폭군 티라노사우루스 몸길이 십오미터 키는 오미터 몸무게 칠톤 날카로운 이빨 삼십센티미터나 된대 
강력한 턱으로 냠냠 쩝쩝 먹이를 뜯어먹지 크아아앙"""

"""리스트와 딕셔너리를 잘 이용해봐자꾸나 나라이름:함수, 국기나오는 높이를 고정하시오. """

"""import math
def stddev(*args):
    def mean():
        return sum(args)/len(args)
    def variance(m):
        total = 0
        for arg in args:
            total += (args-m)**2
        return total/(len(args) - 1)
    v = variance(mean())
    return math.sqrt(v)
print(stddev(2.3, 1.7, 1.4, 0.7, 1.9, 1.3))"""

"""def gen(num):
    for i in range (0, num):
        yield i
        print("제너레이터 진행중")
for data in gen(5):
    print(data)"""

import turtle
import random
myturtle, tx, ty, tc, ts, tshape = [None] * 6
shapelist = []
playerturtles = []
swidth, sheight = 500, 500
if __name__ == "__main__":
    turtle.title('거북이 리스트 활용')
    turtle.setup(width = swidth + 50, height = sheight + 50)
    turtle.screensize(swidth, sheight)
    shapelist = turtle.getshapes()
    for i in range(0, 100):
        random.shuffle(shapelist)
        myturtle = turtle.Turtle(shapelist[0])
        tx = random.randrange(-swidth / 2, swidth / 2)
        ty = random.randrange(-sheight / 2, sheight / 2)
        tsize



 