import pygame,random
pygame.init()
height=800
width=800
screen=pygame.display.set_mode((width,height))
class bob(pygame.sprite.Sprite):
    def __init__(self,color,width,height):
        super().__init__()
        self.image=pygame.Surface([width,height])
        self.image.fill(color)
        self.rect=self.image.get_rect()

    def resetpos(self):

        self.rect.x=random.randint(1,800)
        self.rect.y=random.randint(-200,-20)
    def update(self):
        self.rect.y+=1

        if self.rect.bottom>800:
            self.resetpos() 
blocklist=pygame.sprite.Group()
allspritelist=pygame.sprite.Group()
for i in range(51):
    bb=bob("red",15,20)
    bb.rect.x=random.randint(0,800)
    bb.rect.y=random.randint(0,800)
    blocklist.add(bb)
    allspritelist.add(bb)

class p2(bob):
    def update(self):
        pos=pygame.mouse.get_pos()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
aa=p2("blue",15,20)
allspritelist.add(aa)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    screen.fill("white")
    allspritelist.update()
    blockhitlist=pygame.sprite.spritecollide(aa,blocklist,False)
    for i in blocklist:
      i.resetpos()
    allspritelist.draw(screen)
    pygame.display.update()







