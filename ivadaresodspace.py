import pygame
pygame.init()
height=800
width=1200
winner=""
gameover=False
b1=[]
b2=[]

screen=pygame.display.set_mode((width,height))
border=pygame.Rect(585,0,30,801)
s1=pygame.transform.rotate(pygame.transform.scale(pygame.image.load("rocket1.png"),(49,50)),90)
s2=pygame.transform.rotate(pygame.transform.scale(pygame.image.load("rocket2.png"),(49,50)),270)
bg=pygame.transform.scale(pygame.image.load("space1.png"),(1200,800))
s1r=pygame.Rect(100,50,49,50)
s2r=pygame.Rect(1000,500,47,50)
#to change how much health you get
plh1=5
plh2=5
font=pygame.font.SysFont("sanfransisco",50)

def draw():
    screen.blit(bg,(0,0))
    hlpt1=font.render(f"health:{plh1}",True,"white")
    hlpt2=font.render(f"health:{plh2}",True,"white")
    pygame.draw.rect(screen,"black",border)
    screen.blit(hlpt1,(20,20))
    screen.blit(hlpt2,(1000,20))
    screen.blit(s1,(s1r.x,s1r.y))
    screen.blit(s2,(s2r.x,s2r.y))
    gt=font.render(f"player {winner} wins",True,"black")
    if gameover:
        screen.fill("red")
        screen.blit(gt,(150,450))
    for i in b1:
        pygame.draw.rect(screen,"blue",i)
    for i in b2:
        pygame.draw.rect(screen,"blue",i)
    
def s1rmove(keys_pressed):
    if keys_pressed[pygame.K_w] and s1r.y>0:

        
        s1r.y-=5
    if keys_pressed[pygame.K_s] and s1r.y<780:
        s1r.y+=5
def s2rmove(keys_pressed):
    if keys_pressed[pygame.K_UP ] and s2r.y>0:
        s2r.y-=5
    if keys_pressed[pygame.K_DOWN] and s2r.y<780:
        s2r.y+=5

def gamesover():
    global plh1, winner, plh2, gameover
    if plh2==0:
        gameover=True
        winner="yellow "
    if plh1==0:
        gameover=True
        winner="red "




#bulletmovement
def bmove(b1,b2):
    global plh1,plh2
    
    for i in b1:
        i.x+=5
        if s2r.colliderect(i):
            b1.remove(i)
            plh2-=1
        elif i.x>1200:
            b1.remove(i)
    for i in b2:
        i.x-=5
        if s1r.colliderect(i):
            b2.remove(i)
            plh1-=1
        elif i.x<0:
            b2.remove(i)
        
    
    
            

    
    



while True:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_d:
                bullet1=pygame.Rect(s1r.x,s1r.y,10,5)
                b1.append(bullet1)
            if event.key==pygame.K_RIGHT:
                bullet2=pygame.Rect(s2r.x,s2r.y,10,5)
                b2.append(bullet2)
    

    draw() 
    bmove(b1,b2)
    keys_pressed=pygame.key.get_pressed()
    s1rmove(keys_pressed)
    s2rmove(keys_pressed)
    gamesover()
    

    pygame.display.update()










