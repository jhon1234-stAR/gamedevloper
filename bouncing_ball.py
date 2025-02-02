#setting up sreen
import pygame
pygame.init()
width=1200
height=500
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("bouncy blue ball")
#macking the ball
ball=pygame.draw.circle(surface=screen,color="dark blue",center=[100,100],radius=40)

speed=[1,1]


#wil always be at the end
while True:
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()

#making the colour of the background 
    screen.fill("white")
    #movment og the ball
    ball=ball.move(speed)
    if ball.left<=0 or ball.right>=width:
        speed[0]=-speed[0]
    if ball.top<=0 or ball.bottom>=height:
        speed[1]=-speed[1]
    pygame.draw.circle(surface=screen,color="dark blue",center=ball.center,radius=40)
    pygame.display.update()








