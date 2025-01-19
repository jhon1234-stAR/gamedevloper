
import pgzrun
TITLE="BOB"

score=0
timeleft=30
WIDTH=871

HEIGHT=651
qfile="questions.txt"
gameover=False
win=False
q=[]
qcount=0
qinex=0

scrollybox=Rect(1,1,872,81)
boxy=Rect(21,100,600,151)
ans1=Rect(21,270,300,151)
ans2=Rect(370,270,300,151)
ans3=Rect(20,450,300,151)
ans4=Rect(370,450,300,151)
timey=Rect(700,100,121,151)
skipy=Rect((700,270,121,330))
aboxys=[ans1,ans2,ans3,ans4]
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

    txt=f"welcome to the quiz!!question number:{qinex} of {qcount}  "
    screen.draw.textbox(txt,scrollybox,color="black",shadow=(0.5,0.5),scolor="red")
    screen.draw.textbox(str(timeleft),timey,color="black",shadow=(0.5,0.5),scolor="red")
    screen.draw.textbox("skip",skipy,color="black",angle=-90,shadow=(0.5,0.5),scolor="red")
    screen.draw.textbox(question[0],boxy,color="black",shadow=(0.5,0.5),scolor="red")
    hi=1
    for i in aboxys:
        screen.draw.textbox(question[hi].strip(),i,color="black",shadow=(0.5,0.5),scolor="red")
        hi+=1
    

def readquestions():
    global qcount
    with open (qfile) as d:
        for i in d:
            q.append(i)
            qcount+=1

def update():
    scrollybox.x-=2
    if scrollybox.right<0:
        scrollybox.x=871

def nextquestions():
    global qinex

    qinex+=1
    return q.pop(0).split("|")
def bobisalwaywrong():
    global gameover,timeleft,question
    mes=f"gameover you got {score}/11"
    question=[mes,"_","_","_","_",0]
    timeleft=0
    gameover=True


def bobiscorrect():
    global timeleft
    global question
    global score
    score+=1
    if q:
        question=nextquestions()
        timeleft=30
    else:
        bobisalwaywrong()



def on_mouse_down(pos):
    box=1

    for i in aboxys:
        if i.collidepoint(pos):
            if box is int(question[5]):
                bobiscorrect()
            else:
                bobisalwaywrong()
        box+=1
    if skipy.collidepoint(pos):
        s()
def timer():
    global timeleft
    if timeleft:
        timeleft-=1
    else:
        bobisalwaywrong()
    


def s():
    global timeleft,question
    if q:
        question=nextquestions()
        timeleft=30
    else:
        bobisalwaywrong()








clock.schedule_interval(timer,1)
readquestions()
question=nextquestions()

pgzrun.go()
































