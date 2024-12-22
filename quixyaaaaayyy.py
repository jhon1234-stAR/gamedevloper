
import pgzrun
TITLE="BOB"



WIDTH=801
HEIGHT=500


scrollybox=Rect(1,1,800,81)
boxy=Rect(21,100,600,91)
ans1=Rect(21,212,130,91)
ans2=Rect(173,212,130,91)
ans3=Rect(21,323,130,91)
ans4=Rect(173,323,130,91)
timey=Rect(630,100,121,91)
skipy=Rect((630,212,121,185))

def draw():
    screen.clear()
    screen.fill("black")
    screen.draw.filled_rect(scrollybox,"yellow")
    screen.draw.filled_rect(boxy,"yellow")
    screen.draw.filled_rect(ans1,"yellow")
    screen.draw.filled_rect(ans2,"yellow") 
    screen.draw.filled_rect(ans3,"yellow")
    screen.draw.filled_rect(ans4,"yellow")
    screen.draw.filled_rect(timey,"yellow") 
    screen.draw.filled_rect(skipy,"yellow")






pgzrun.go()
































