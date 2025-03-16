import pygame
pygame.init()
width=1200
height=500

screen=pygame.display.set_mode((width,height))
drawer=False

lastpos=None
currentpos=None
colour="purple"
screen.fill("white")
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                drawer=True
                lastpos=event.pos
                pygame.display.update()
        elif event.type==pygame.MOUSEBUTTONUP:
                if event.button==1:
                    drawer=False
                    pygame.display.update()

        elif event.type==pygame.MOUSEMOTION:
                if drawer:
                    currentpos=event.pos
                    pygame.draw.line(screen,colour,lastpos,currentpos,width=6)
                    lastpos=currentpos
                    pygame.display.update()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_1:
                   colour="yellow"
            if event.key==pygame.K_2:
                   colour="pink"
            if event.key==pygame.K_3:
                   colour="purple"
            if event.key==pygame.K_4:
                   colour="red"

            if event.key==pygame.K_5:
                   colour="black"
            if event.key==pygame.K_6:
                   colour="blue"
            if event.key==pygame.K_7:
                   colour="brown"
            if event.key==pygame.K_8:
                   colour="green"
            if event.key==pygame.K_9:
                   colour="dark blue"
            if event.key==pygame.K_0:
              screen.fill("white")

                   
              
            

                   


            pygame.display.update()