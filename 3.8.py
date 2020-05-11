import math
pos=[0,0]
while True:
    s=input()
    if not s:
        break
    movement=s.slip("")
    direction=movement[0]
    steps=int(movement[1])
    if diretion=="UP":
        pos[0]+=steps
    elif diretion=="DOWN":
        pos[0]-=steps
    elif diretion=="LEFT":
        pos[1]-=steps
    elif diretion=="RIGHT":
        pos[1]+=steps
    else:
        pass
    #####################
    print(int(round(math.sqrt(pos[1]**2+pos[0]**2))))
