import random

balls = []

for i in range(5):

    ball = sphere(
        pos=vector(random.randint(-10,-5),random.randint(-5,5),0),
        radius=0.7,
        color=color.red)
for i in range(5):

    ball = sphere(pos=vector(random.randint(-10,-5),
            random.randint(-5,5),0),
        radius=0.7,
        color=color.yellow)]
while True : 
    k = keysdown()
     if ' 'in k :
       ball.pos.x = random.uniform(-10, 5)
       ball.pos.y = random.uniform(-5, 5)


