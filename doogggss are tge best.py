
mport pgzrun,random
HEIGHT=500
WIDTH=500
score=0
gameover=False
dog=Actor("puppy")
bone=Actor("puppy_bone")
dog.pos=0,0
bone.pos=500,500
def draw():
    screen.fill("light green")
    dog.draw()
    bone.draw()
    screen.draw.text("score:"+str(score),color="black",topright=(400,10))
    if gameover:
        screen.fill("red") 
        screen.draw.text("game over !!!score:"+str(score),color="black",midbottom=(250,250))
def update():
    global score
    if keyboard.left:
        dog.x-=5
    if keyboard.right:
        dog.x+=5
    if keyboard.up:
        dog.y-=5
    if keyboard.down:
        dog.y+=5
    if dog.colliderect(bone):
        score+=1
        bone.pos=random.randint(0,500),random.randint(0,500)
def timup():
    global gameover
    gameover=True
clock.schedule(timup,120)
pgzrun.go()
    





        







    


