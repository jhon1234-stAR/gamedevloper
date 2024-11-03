import pgzrun
from random import randint
from time import time
#vairibles
HEIGHT=800
WIDTH=800
bones=[]
lines=[]
st=0
currentbone=0
numbones=10
def bonecreater():
    for t in range(numbones):
        bone=Actor("puppy_bone")
        bone.pos=randint(20,780),randint(20,780)
        bones.append(bone)
def draw():
    screen.blit("grass field",(0,0))
    num1=1

    for t in bones:
        screen.draw.text(str(num1),(t.pos[0],t.pos[1]+20))
        t.draw()
        num1+=1
    if currentbone<numbones:
        totaltime=time()-st
        screen.draw.text(str(round(totaltime)),(40,40),fontsize=25)

def update():
    pass



bonecreater()
st=time()
pgzrun.go()






