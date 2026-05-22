import random

balls = []

for i in range(5):

    ball = sphere(
        pos=vector(random.randint(-10,-5),random.randint(-5,5),0),
        radius=0.7,
        color=color.red)

