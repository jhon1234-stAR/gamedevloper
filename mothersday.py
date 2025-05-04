import pygame, time
pygame.init()
width=1200
height=800
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("hi")
wr="happy mother's day"
hi=[]
letterindex=0
letterspacing=60
speed=letterspacing
font=pygame.font.SysFont(None,125)
image=pygame.transform.scale(pygame.image.load("flowerfeild.jpg"),(1200,800))

robot=pygame.transform.scale(pygame.image.load("C:\\Users\\rache\\OneDrive\\Desktop\\pro develepor\\robot.jpg"),(175,175))
screen.fill("white")

rect=pygame.Rect(50,200,175,175)
screen.blit(robot,(rect.x,rect.y))
clock=pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    screen.blit(image,(0,0))
    
    keys=pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:    
        if letterindex<len(wr):
            hi.append((wr[letterindex],rect.x,rect.y))
            letterindex+=1
        rect.x+=speed
    screen.blit(robot,(rect.x,rect.y))
    for letter,x,y in hi:
        text=font.render(letter,True,"white")
        screen.blit(text,(x,y))
    clock.tick(30)
    
    pygame.display.update()  
