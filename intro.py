import winsound
import turtle
import time 



def Intro(): 

    pn= turtle.Screen()
    winsound.PlaySound(".\\sound\\intro.wav", winsound.SND_ASYNC)
    pn.bgcolor("black")
    pn.title("7 Dungeons Deep(7DD)")
    pn.setup(1900,930)
    pn.bgpic(".\\art\\Image2.gif")
    tn=turtle.Turtle()
    tn.ht()
    tn.penup()
    tn.goto(0,20)
    tn.pencolor("white")
    tn.write("Seven Dungeons Deep",move=False,align="center",font=("Times",30,"bold"))
    tn.goto(10,-200)
    tn.write("Loading...",move=False,align="center",font=("Times",20,"bold"))
    tn.goto(10,-300)
    tn.write("WASD = To attack,  Arrowkeys = To move,  Spacebar = Drink healing potion,  Z = Use fireball scroll ",move=False,align="center",font=("Times",15,"bold"))
    tn.goto(10,-350)
    tn.write("Music/Sound from Freesound.org        Art/Programming by Tommy Kwong",move=False,align="center",font=("Times",15,"bold"))



    pn.tracer(0)
    time.sleep(6)
    pn.tracer(0)
    pn.clear()
    tn.clear()



