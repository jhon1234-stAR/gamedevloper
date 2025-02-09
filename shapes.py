import pygame 
pygame.init()
width=800
height=800
screen=pygame.display.set_mode((width,height))
screen.fill("black")

#macking the blueprints
class mrcircle():
    def __init__ (self,color,pos,radius):
        self.color=color
        self.radius=radius
        self.pos=pos
        self.screen=screen

    def draw(self):
        pygame.draw.circle(self.screen,self.color,self.pos,self.radius)
    def bigcircle(self,y):
        self.radius+=y
        pygame.draw.circle(self.screen,self.color,self.pos,self.radius)
#creatinf the objects
whitecircle=mrcircle("white",10,(300,300))
bigcircle1=mrcircle("violet",25,(400,400))
bigcircle2=mrcircle("pink",50,(400,400))
bigcircle3=mrcircle("blue",75,(400,400))
bigcircle4=mrcircle("green",100,(400,400))
bigcircle5=mrcircle("yellow",125,(400,400))
bigcircle6=mrcircle("orange",150,(400,400))
bigcircle7=mrcircle("red",175,(400,400))


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            whitecircle.draw()
            bigcircle1.draw()
            bigcircle2.draw()
            bigcircle3.draw()
            bigcircle4.draw()
            bigcircle5.draw()
            bigcircle6.draw()
            bigcircle7.draw()
            pygame.display.update()
        elif event.type==pygame.MOUSEBUTTONUP:
            whitecircle.bigcircle(4)
            bigcircle1.bigcircle()
            bigcircle2.bigcircle()
            bigcircle3.bigcircle()
            bigcircle4.bigcircle()
            bigcircle5.bigcircle()
            bigcircle6.bigcircle()
            bigcircle7.bigcircle()
            pygame.display.update()



            
    

















