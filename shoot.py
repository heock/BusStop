# 심화프로그래밍 기말과제 허준혁_20230868
import pygame
import random
from datetime import datetime
pygame.init()
size = [360, 640]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Shooting Game")
clock = pygame.time.Clock()

pygame.mixer.music.load("C:/위대한 첫 걸음/source/tetrismusic.mp3")
pygame.mixer.music.play(-1)

class obj:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.move = 0

    def put_img(self, address):
        if address[-3:] == "png":
            self.img = pygame.image.load(address).convert_alpha()
        else:
            self.img = pygame.image.load(address)
        self.sx, self.sy = self.img.get_size()

    def change_size(self, sx, sy):
        self.img = pygame.transform.scale(self.img, (sx, sy))
        self.sx, self.sy = self.img.get_size()

    def show(self):
        screen.blit(self.img, (self.x, self.y))

def crash(a, b):
    if (a.x - b.sx <= b.x) and (b.x <= a.x + a.sx):
        if (a.y - b.sy <= b.y) and (b.y <= a.y + a.sy):
            return True
    return False

black = (0, 0, 0)
white = (255, 255, 255)

plane = obj()
plane.put_img("C:/위대한 첫 걸음/source/plane.png")
plane.change_size(40, 60)
plane.x = round(size[0] / 2 - plane.sx / 2)
plane.y = size[1] - plane.sy - 10
plane.move = 5

left_go = right_go = space_go = False
m_list = []
a_list = []
k = 0
GO = 0
kill = 0
loss = 0

waiting = True
while waiting:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                waiting = False

    screen.fill(black)
    font = pygame.font.Font("C:/Windows/Fonts/Arial.ttf", 18)
    text = font.render("PRESS SPACE TO START", True, white)
    screen.blit(text, (90, size[1] // 2 - 10))
    pygame.display.flip()

start_time = datetime.now()

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GO = 0
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left_go = True
            elif event.key == pygame.K_RIGHT:
                right_go = True
            elif event.key == pygame.K_SPACE:
                space_go = True
                k = 0
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left_go = False
            elif event.key == pygame.K_RIGHT:
                right_go = False
            elif event.key == pygame.K_SPACE:
                space_go = False

    if left_go:
        plane.x -= plane.move
        if plane.x < 0:
            plane.x = 0
    if right_go:
        plane.x += plane.move
        if plane.x > size[0] - plane.sx:
            plane.x = size[0] - plane.sx

    if space_go and k % 6 == 0:
        m = obj()
        m.put_img("C:/위대한 첫 걸음/source/missile.png")
        m.change_size(4, 12)
        m.x = plane.x + plane.sx // 2 - m.sx // 2
        m.y = plane.y - m.sy
        m.move = 12
        m_list.append(m)
    k += 1

    d_list = []
    for i, m in enumerate(m_list):
        m.y -= m.move
        if m.y < -m.sy:
            d_list.append(i)
    for i in reversed(d_list):
        del m_list[i]

    if random.random() > 0.98:
        a = obj()
        a.put_img("C:/위대한 첫 걸음/source/alien.png")
        a.change_size(40, 40)
        a.x = random.randint(0, size[0] - a.sx)
        a.y = 10
        a.move = 1
        a_list.append(a)

    d_list = []
    for i, a in enumerate(a_list):
        a.y += a.move
        if a.y > size[1]:
            d_list.append(i)
    for i in reversed(d_list):
        del a_list[i]
        loss += 1

    dm_list = []
    da_list = []
    for i, m in enumerate(m_list):
        for j, a in enumerate(a_list):
            if crash(m, a):
                dm_list.append(i)
                da_list.append(j)
    for i in sorted(set(dm_list), reverse=True):
        del m_list[i]
    for j in sorted(set(da_list), reverse=True):
        del a_list[j]
        kill += 1

    for a in a_list:
        if crash(a, plane):
            GO = 1
            break

    if GO == 1:
        break

    screen.fill(black)
    plane.show()
    for m in m_list:
        m.show()
    for a in a_list:
        a.show()

    now_time = datetime.now()
    delta = round((now_time - start_time).total_seconds())

    font = pygame.font.Font("C:/Windows/Fonts/Arial.ttf", 16)
    screen.blit(font.render(f"Killed: {kill}  Missed: {loss}", True, (255, 255, 0)), (10, 5))
    screen.blit(font.render(f"Time: {delta}", True, white), (size[0]-100, 5))

    pygame.display.flip()

game_over = True
while game_over:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = False

    screen.fill(black)
    font = pygame.font.Font("C:/Windows/Fonts/Arial.ttf", 36)
    text = font.render("GAME OVER", True, (255, 0, 0))
    screen.blit(text, (90, 300))
    pygame.display.flip()

pygame.quit()
