from vpython import *
import random

red_balls = []
yellow_balls = []

for i in range(5):
    red_balls.append(sphere(pos=vector(random.uniform(-5,-3), random.uniform(-3,3),0),
                            radius=0.4, color=color.red))
    yellow_balls.append(sphere(pos=vector(random.uniform(-5,-3), random.uniform(-3,3),0),
                               radius=0.4, color=color.yellow))

launcher = arrow(pos=vector(5,0,0), axis=vector(-2,0,0),
                 shaftwidth=0.3, color=color.cyan)

launcher_dir = 1

while True:
    rate(60)
    launcher.pos.y += 0.05 * launcher_dir
    if abs(launcher.pos.y) > 3:
        launcher_dir *= -1
