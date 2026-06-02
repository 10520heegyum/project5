5월 22일
한 일: 빨간 공을 랜덤한 위치에 생성되게 했다.
배운 점: 이제 랜덤한 모양 코딩?은 쉽게할 수 있을 것 같다
느낀 점:친구랑 의논하면서 코딩을 함께 해보니 혼자하는것보다 재밌고 아이디어도 더 잘 나오는 것 같다.
다음 할 일:다른 색 공을 랜덤한 위치에 생성하게 하고 어떤 키를 누르면 위치가 랜덤하게 바뀌게 하고싶다.

5월29일
한 일: 빨간 공과 노란 공을 각각 5개씩 만들고, 화살표가 위아래로 움직이도록 만들었다.
배운 점:반복문을 사용하면 같은 모양의 공을 여러 개 쉽게 만들 수 있다는 것을 배웠다.
느낀 점: 처음에는 어려웠지만 공과 화살표가 실제로 움직이는 것을 보니 재미있었다.
다음 할 일: 총알 발사 기능과 충돌 기능을 추가하고싶다.


Web VPython 3.2
from vpython import *
import random

d = 1



gun = arrow(pos=vector(8,0,0),axis=vector(-2,0,0),shaftwidth=0.3,color=color.blue)

reds = []

for i in range(10):
    r = sphere(pos=vector(random.uniform(-8,-2),random.uniform(-5,5),0),radius=0.6,color=color.red)
    reds.append(r)


bullets = []


def shoot():
    bullet = sphere(pos=gun.pos,radius=0.2,color=color.white)
    bullet.v = vector(-0.4,0,0)
    bullets.append(bullet)


while True:
    rate(100)

   
    gun.pos.y = gun.pos.y + 0.05 * d

    if gun.pos.y > 5:
        d = d * -1
    if gun.pos.y < -5:
        d = d * -1

   
    if ' ' in keysdown():
        shoot()
        rate(100)

    
    for bullet in bullets[:]:
        bullet.pos = bullet.pos + bullet.v

       
        if bullet.pos.x < -10:
            bullet.visible = False
            bullets.remove(bullet)
        
        for r in reds[:]:
            if mag(bullet.pos - r.pos) < 0.8:
                r.visible = False
                bullet.visible = False
                reds.remove(r)
                bullets.remove(bullet)
                break   

        
        for r in reds[:]:
            if mag(bullet.pos - r.pos) < 0.8:
                r.visible = False
                bullet.visible = False
                reds.remove(r)
                bullets.remove(bullet)
                break

   
    if len(reds) == 0:
        label(
            pos=vector(0,0,0),
            text="YOU WIN!",
            height=40,
            color=color.red,
            box=False)
        break
