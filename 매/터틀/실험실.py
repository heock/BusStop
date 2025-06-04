import turtle 
import random
mt, tx, ty, tc, ts, tshape = [None]*6
shapelist = []
playersturtle = []
swidth, sheight = 500, 500
if __name__ == "__main__" :
    turtle.title('거북 리스트 활용')
    turtle.setup(width = swidth + 50, height = sheight + 50)
    turtle.screensize(swidth, sheight)
    shapelist = turtle.getshapes()
    for i in range(0, 100) :
        random.shuffle(shapelist)
        mt = turtle.Turtle(shapelist[0])
        tx = random.randrange(-swidth // 2, swidth // 2)
        ty = random.randrange(-sheight // 2, sheight // 2)
        r = random.random(); g = random.random(); b = random.random()
        ts = random.randrange(1, 3)
        playersturtle.append([mt, tx, ty, ts, r, g, b])
    for i in range(0, 100) :
        mt = playersturtle[i][0]
        mt.color((playersturtle[i][4], playersturtle[i][5], playersturtle[i][6]))
        mt.pencolor((playersturtle[i][4], playersturtle[i][5], playersturtle[i][6])) 
        mt.turtlesize(playersturtle[i][3])
        mt.goto(playersturtle[i][1], playersturtle[i][2])
    turtle.done()   
 