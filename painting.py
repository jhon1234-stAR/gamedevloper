import pygame
pygame.init()
width=1200
height=500

screen=pygame.display.set_mode((width,height))
drawer=False
colours=["purple","red","blue","brown","light blue","pink","wheat","black"]
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
            if event.key==pygame.K_m:
                   index=colours.index(colour)

                   colour=colours[(index+1)%len(colours)]
            pygame.display.update()


                    
                    


              
     

        
 