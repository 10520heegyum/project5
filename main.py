Web VPython 3.2
from vpython import *
import random

d = 1


gun = arrow(pos=vector(8,0,0),axis=vector(-2,0,0),color=color.blue)

reds = []
for i in range(10):
    r = sphere(
        pos=vector(random.uniform(-8,-2),random.uniform(-5,5),0),radius=0.6,color=color.red)
    reds.append(r)

bullets = []
def shoot():
    bullet = sphere(
        pos=gun.pos,
        radius=0.2,
        color=color.white)
    bullet.v = vector(-0.4,0,0)
    bullets.append(bullet)

while True:
    rate(100)
  
    gun.pos.y = gun.pos.y + 0.05 * d

    if gun.pos.y > 5:
        d = d * -1
    if gun.pos.y < -5:
        d = d * 1
  
    if ' ' in keysdown():
        shoot()
        rate(10)

    for bullet in bullets[:]:
        bullet.pos = bullet.pos + bullet.v

        if bullet.pos.x < -10:
            bullet.visible = False
            bullets.remove(bullet)
