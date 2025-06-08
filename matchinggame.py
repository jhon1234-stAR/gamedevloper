import pygame
pygame.init()
height=600
width=600
screen=pygame.display.set_mode((width,height))
screen.fill("white")
font=pygame.font.SysFont("Segoe UI Variable Small",50)
sub=pygame.image.load("subway.png")
can=pygame.image.load("candy1.png")
tem=pygame.image.load("templerun.png")
lud=pygame.image.load("ludo.png")


t1=font.render("ludo",True,"black")
t2=font.render("subway surfer",True,"black")
t3=font.render("temple run",True,"black")
t4=font.render("candy crush",True,"black")

screen.blit(t1,(350,50))
screen.blit(t2,(350,200))
screen.blit(t3,(350,350))
screen.blit(t4,(350,500))

screen.blit(sub,(100,50))
screen.blit(can,(100,200))
screen.blit(tem,(100,350))
screen.blit(lud,(100,500))
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        
        if event.type==pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
            pygame.draw.circle(screen,"red",pos,10,0)
            pygame.display.update()

        elif event.type==pygame.MOUSEBUTTONUP:
            pos1=pygame.mouse.get_pos()
            pygame.draw.circle(screen,"red",pos1,10,0)

            pygame.draw.line(screen,"red",pos,pos1,3)

        

        

    
            
    pygame.display.update()