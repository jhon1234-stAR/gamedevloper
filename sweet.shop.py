import pgzrun
import random
WIDTH=400
HEIGHT=400
level=10
list=("bag2","bottleimg","chipsimg")
win=False
lose=False
currentlevel=1
items=[]
animation=[]
speed=10
def draw():
    screen.blit(bg,(0,0))
    if lose:
        screen.draw.text("you lost",(200,200),fontsize=60,color="white")
    elif win:
        screen.draw.text("you wom!",(200,200),fontsize=60,color="white")
    else:
        for i in items:
            i.draw()
def update():
    global items
    if len(items)==0:
        items=mega_funtion(currentlevel)






def mega_funtion(num):
    itemchecker=i_t(num)
    itemimg=imgcreator(itemchecker)
    layout(itemimg)
    animators(itemimg)
    return itemimg


   



def i_t(num):
    itemchecker=["paperimg"]
    for i in range(num):
        store=random.choice(list)
        itemchecker.append(store)
    return itemchecker

def imgcreator(itemchecker):
    itemimg=[]
    for i in itemchecker:
        imag=Actor(i)
        itemimg.append(imag)
    return itemimg

def layout(num1):
    numgaps=len(num1)+1
    gapsize=WIDTH/numgaps
    random.shuffle(num1)
    for i,g in enumerate(num1,1):
        xpos=i*gapsize
        g.x=xpos
    
def animators(num2):
    for i in num2:
        timetaken=speed-currentlevel
        i.anchor=("center","bottom")
        anime=animate(i,duration=timetaken,on_finished=gameovers,y=HEIGHT)
        animation.append(anime)

def gameovers():
    global lose

    lose=True

pgzrun.go()

























