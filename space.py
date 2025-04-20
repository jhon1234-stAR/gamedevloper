import pygame
pygame.init()
height=800
width=1200

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



while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    draw() 
    pygame.display.update()










