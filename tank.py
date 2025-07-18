import pygame, random
pygame.init()
height=800
width=800
screen=pygame.display.set_mode((width,height))
screen.fill("white")

class bob(pygame.sprite.Sprite):
    def __init__(self,color,width,height):
        super().__init__()
        self.image=pygame.Surface([width,height])
        self.image.fill(color)
        self.rect=self.image.get_rect()blocklist=pygame.sprite.Group()
    allspritelist=pygame.sprite.Group()
    

    
#

    def resetpos(self):

        self.rect.x=random.randint(1,800)
        self.rect.y=random.randint(-200,-20)
    def update(self):
        self.rect.y+=2

        if self.rect.bottom>800:
            self.resetpos() 
for i in range(51):
    bb=bob("red",15,20)
    bb.rect.x=random.randint(0,800)
    bb.rect.y=random.randint(0,800)
    blocklist.add(bb)
    allspritelist.add(bb)
"""def draw():
    tank=pygame.image.load("tank2.jpg")
    screen.blit(tank,(300,300))

def s1rmove(keys_pressed):
    if keys_pressed[pygame.K_SPACE]:
        """

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    

    
    allspritelist.update()
    blockhitlist=pygame.sprite.spritecollide(aa,blocklist,False)
    pygame.display.update()



     
    ##s1rmove(keys_pressed)



