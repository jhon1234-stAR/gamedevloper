import pgzrun
from random import randint
from time import time
#vairibles
HEIGHT=800
WIDTH=800
bones=[]
lines=[]
st=0
gameover=False
win=False
currentbone=0
numbones=10
def bonecreater():
    for t in range(numbones):
        bone=Actor("christmas_tree")
        bone.pos=randint(20,780),randint(50,740)
        bones.append(bone)
def draw():
    screen.blit("cabin2",(0,0))
    num1=1

    for t in bones:
        screen.draw.text(str(num1),(t.pos[0],t.pos[1]+70))
        t.draw()
        num1+=1
    if currentbone<numbones:
        totaltime=time()-st
        screen.draw.text(str(round(totaltime)),(40,40),fontsize=25)
    for i in lines:
        screen.draw.line(i[0],i[1],"white")

    if gameover:
        screen.draw.text("you lost",(400,400),fontsize=100,color="white")
    if win:
        sreen.draw.text("you won",(400,400),fontsize=1000,color="white")
def update():
    pass
def timeup():
    global win
    global gameover
    if len(lines)==9:
        win=True
    else:
        gameover=True

def on_mouse_down(pos):
    global currentbone
    global numbones
    global lines
    if currentbone<numbones:
        if bones[currentbone].collidepoint(pos):
            if currentbone:
             lines.append((bones[currentbone-1].pos,bones[currentbone].pos))
            currentbone+=1
        else:
            lines=[]
            currentbone=0
            
    
    


bonecreater()
st=time()
clock.schedule(timeup,20)
pgzrun.go()