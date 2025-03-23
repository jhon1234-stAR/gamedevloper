import pygame
pygame.init()
width=800
height=800
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("title")

class bobby(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("rocket.png")
        self.rect=self.image.get_rect()
    def update(self,move):

        if move[pygame.K_UP]:
            self.rect.move_ip(0,-10)
        if move[pygame.K_DOWN]:
            self.rect.move_ip(0,10)
        if move[pygame.K_RIGHT]:
            self.rect.move_ip(10,0)
        if move[pygame.K_LEFT]:
            self.rect.move_ip(-10,0)
        if self.rect.left<0:
            self.rect.left=0
        
        
        
              
              
        
mrrocket=bobby()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    move=pygame.key.get_pressed()
    mrrocket.update(move)
    screen.blit(pygame.image.load("space.png"),(0,0))
    screen.blit(mrrocket.image,mrrocket.rect.topleft)
    pygame.display.update()


     
        
    