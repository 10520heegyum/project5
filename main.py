Web VPython 3.2

reds = []
bullets = []

gun = arrow(pos=vector(6, 0, 0),axis=vector(-1.5, 0, 0),color=color.blue)

for i in range(10):
    r = sphere(pos=vector(-5, i - 4.5, 0),radius=0.4,color=color.red)
    reds.append(r)

def shoot():
    b = sphere(pos=gun.pos,radius=0.15,color=color.white)
    b.v = vector(-0.4, 0, 0)
    bullets.append(b)

while True:
    rate(100)

    gun.pos.y = gun.pos.y + 0.05
    
    if gun.pos.y > 5:
        gun.pos.y = -5
    
    if ' ' in keysdown():
        shoot()
    
    for b in bullets[:]:
        b.pos = b.pos + b.v 
        
        if b.pos.x < -8:
            b.visible = False
            bullets.remove(b)
        
        for r in reds[:]:
            if mag(b.pos - r.pos) < 0.8:
                r.visible = False
                b.visible = False
                reds.remove(r)
                bullets.remove(b)
               
    if len(reds) == 0 :
        label(pos=vector(0, 0, 0),text="YOU WIN!",color=color.red)
Web VPython 3.2

reds = []
bullets = []

gun = arrow(pos=vector(6, 0, 0),axis=vector(-1.5, 0, 0),color=color.blue)

for i in range(10):
    r = sphere(pos=vector(-5, i - 4.5, 0),radius=0.4,color=color.red)
    reds.append(r)

def shoot():
    b = sphere(pos=gun.pos,radius=0.15,color=color.white)
    b.v = vector(-0.4, 0, 0)
    bullets.append(b)

while True:
    rate(100)

    gun.pos.y = gun.pos.y + 0.05
    
    if gun.pos.y > 5:
        gun.pos.y = -5
    
    if ' ' in keysdown():
        shoot()
    
    for b in bullets[:]:
        b.pos = b.pos + b.v 
        
        if b.pos.x < -8:
            b.visible = False
            bullets.remove(b)
        
        for r in reds[:]:
            if mag(b.pos - r.pos) < 0.8:
                r.visible = False
                b.visible = False
                reds.remove(r)
                bullets.remove(b)
               
    if len(reds) == 0 :
        label(pos=vector(0, 0, 0),text="YOU WIN!",color=color.red)
        Web VPython 3.2

reds = []
bullets = []

gun = arrow(pos=vector(6, 0, 0),axis=vector(-1.5, 0, 0),color=color.blue)

for i in range(10):
    r = sphere(pos=vector(-5, i - 4.5, 0),radius=0.4,color=color.red)
    reds.append(r)

def shoot():
    b = sphere(pos=gun.pos,radius=0.15,color=color.white)
    b.v = vector(-0.4, 0, 0)
    bullets.append(b)

while True:
    rate(100)

    gun.pos.y = gun.pos.y + 0.05
    
    if gun.pos.y > 5:
        gun.pos.y = -5
    
    if ' ' in keysdown():
        shoot()
    
    for b in bullets[:]:
        b.pos = b.pos + b.v 
        
        if b.pos.x < -8:
            b.visible = False
            bullets.remove(b)
        
        for r in reds[:]:
            if mag(b.pos - r.pos) < 0.8:
                r.visible = False
                b.visible = False
                reds.remove(r)
                bullets.remove(b)
               
    if len(reds) == 0 :
        label(pos=vector(0, 0, 0),text="YOU WIN!",color=color.red)
         break
