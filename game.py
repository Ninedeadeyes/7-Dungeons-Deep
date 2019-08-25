

import turtle
import math
import random
import time
import winsound



images=[".\\art\\wall.gif",".\\art\\orkleft.gif",".\\art\\ork.gif",".\\art\\orkup.gif",".\\art\\gold.gif",".\\art\\fire.gif",".\\art\\door.gif",".\\art\\orkright.gif",".\\art\\arrowup.gif",
        ".\\art\\arrowdown.gif",".\\art\\arrowright.gif",".\\art\\arrowleft.gif",".\\art\\heroleft.gif",".\\art\\heroright.gif",".\\art\\herodown.gif",".\\art\\heroup.gif",".\\art\\fire.gif",
        ".\\art\\scroll.gif",".\\art\\potion.gif",".\\art\\armour.gif",".\\art\\zombieleft.gif",".\\art\\zombiedown.gif",".\\art\\zombieup.gif",".\\art\\zombieright.gif",".\\art\\torch.gif",".\\art\\skeleton.gif"
        ,".\\art\\npc.gif",".\\art\\tree.gif",".\\art\\rock.gif",".\\art\\background.gif",".\\art\\black.gif",".\\art\\bossdown.gif",".\\art\\bossright.gif",".\\art\\bossleft.gif",".\\art\\bossup.gif",
        ".\\art\\ghost.gif",".\\art\\ghostback.gif",".\\art\\cage.gif",".\\art\\key.gif",".\\art\\capture.gif",".\\art\\sword.gif",".\\art\\crown.gif",".\\art\\Image2.gif"]


for image in images:
    turtle.register_shape(image)


#intro screen
#------------------------------
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


#main screen 
#---------------------------------------------------------


wn = turtle.Screen()
wn.bgcolor("black")
wn.title("7 Dungeons Deep (7DD)")
wn.setup(1900,930)
wn.bgpic(".\\art\\background.gif")
wn.tracer(0)









class Info():
    def __init__(self):
        self.pen = turtle.Turtle()
        self.pen2 = turtle.Turtle()
        self.pen3 = turtle.Turtle()
        self.pen4 = turtle.Turtle()
        self.pen5 = turtle.Turtle()
        self.pen6 = turtle.Turtle()
        self.pen7 = turtle.Turtle()
        self.pen8 = turtle.Turtle()
        self.pen9 = turtle.Turtle()
        
        
    def draw_border(self):
        #Draw border
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.pensize(3)
        self.pen.penup()
        self.pen.goto(-410, 324)
        self.pen.pendown()
        for side in range(4):
            self.pen.fd(820)
            self.pen.rt(90)
            self.pen.fd(750)
            self.pen.rt(90)
            
        self.pen.penup()
        self.pen.ht()
        self.pen.pendown()

    def draw_border2(self):
        #Draw border
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.pensize(3)
        self.pen.penup()
        self.pen.goto(-410, 445)
        self.pen.pendown()
        for side in range(4):
            self.pen.fd(820)
            self.pen.rt(90)
            self.pen.fd(121)
            self.pen.rt(90)
            
        self.pen.penup()
        self.pen.ht()
        self.pen.pendown()

    def draw_border3(self):
        #Draw border
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.pensize(3)
        self.pen.penup()
        self.pen.goto(-60, 445)
        self.pen.pendown()
        self.pen.rt(90)
        self.pen.fd(121)
            
            
        self.pen.penup()
        self.pen.ht()
        self.pen.pendown()

    def draw_border4(self):
        #Draw border
        self.pen9.speed(0)
        self.pen9.color("white")
        self.pen9.pensize(3)
        self.pen9.penup()
        self.pen9.goto(310, 445)
        self.pen9.pendown()
        self.pen9.rt(90)
        self.pen9.fd(121)
            
            
        self.pen9.penup()
        self.pen9.ht()
        self.pen9.pendown()

    
        
    def show_gold(self):
        self.pen9.undo()
        self.pen9.ht()
        msg = "Gold: %s"  %(player.gold)
        self.pen9.penup()
        self.pen9.goto(-400, 325)
        self.pen9.write(msg, font=("Arial", 16, "normal"))
        


    def show_rules(self):
        msg = ("Controls: W,A,S,D Arrow Keys, Spacebar = Potion, Z = Magic  ")
        self.pen.penup()
        self.pen.goto(-290, -400)
        self.pen.write(msg, font=("Arial", 16, "normal"))
        self.pen.pendown()
        self.pen.penup()
        self.pen.ht()
     

    def win(self):

        
        if player.kill==0:    # If player does not kill anything is given an alternative ending 

            msg= (""" 
            You found the Crown of Yendor.
            The world is saved. You smile
            finding the answer you were
            looking for...
                   """)
            self.pen.penup()
            self.pen.goto(-120,304)
            self.pen.write(msg, font=("Arial", 16, "normal"))
            winsound.PlaySound(".\\sound\\victory.wav",0)
            self.pen.undo()

            msg= (""" 
            A peaceful solution.
            You are unchained.
            Thank you for playing
            Click (x) to exit                        
                   """)
            self.pen.write(msg, font=("Arial", 16, "normal"))


        else:

            
            msg= (""" 
            You found the Crown of Yendor.
            Even though the world is saved
            and you are praised as a hero
                  
                   """)
            self.pen.penup()
            self.pen.goto(-120,304)
            self.pen.write(msg, font=("Arial", 16, "normal"))
            winsound.PlaySound(".\\sound\\victory.wav",0)
            self.pen.undo()
            
            
            msg= (""" 
            You drift back into the darkness
            and continue your PATH OF EXILE..
            Was it victory you were searching
            for or something else ?      
                   """)
            self.pen.write(msg, font=("Arial", 16, "normal"))
            winsound.PlaySound(".\\sound\\ending.wav",0)
            self.pen.undo()


            msg= (""" 
            Thank you for playing
            Click (x) to exit
                      
                   """)
            self.pen.write(msg, font=("Arial", 16, "normal"))

        
              


    def start(self):
    
        msg= (""" 
              Human, find the key to this cage
              I need to get back to my fortress

              
               """)
        self.pen.penup()
        self.pen.goto(-120,304)
        self.pen.write(msg, font=("Arial", 16, "normal"))
        time.sleep(.2)
        self.pen.undo()


    def start2(self):
    
        msg= (""" 
              Defeat the butcher and    
              avenge my death !! 
              
               """)
        self.pen.penup()
        self.pen.goto(-120,304)
        self.pen.write(msg, font=("Arial", 16, "normal"))
        time.sleep(.2)
        self.pen.undo()


    def end2(self):
    
        msg= (""" 
               You have killed the butcher
               and avenged my death, thank you
               (+200 EXP ) 
 
               """)
        self.pen.penup()
        self.pen.goto(-120,304)
        self.pen.write(msg, font=("Arial", 16, "normal"))
        time.sleep(2)
        self.pen.undo()

    def end(self):
    
        msg= (""" 
               Thank you for releasing me
               my ekur obur !! (+100 EXP ) 
 
               """)
        self.pen.penup()
        self.pen.goto(-120,304)
        self.pen.write(msg, font=("Arial", 16, "normal"))
        time.sleep(2)
        self.pen.undo()
        


    def intro(self):
    
        msg= (""" 
            You who walk the path of exile !!

            
               """)
        self.pen.penup()
        self.pen.goto(-120,304)
        self.pen.write(msg, font=("Arial", 16, "normal"))
        time.sleep(2)
        self.pen.undo()
        
        
        msg= (""" 
              Find the Crown of Yendor to save
              the world from IMPENDING DOOM 
                  
               """)
        self.pen.write(msg, font=("Arial", 16, "normal"))
        time.sleep(2)
        self.pen.undo()

        msg= (""" 
              I would help, but I took an arrow
              in my knee. Farewell mighty warrior !!                
 
               """)
        self.pen.write(msg, font=("Arial", 16, "normal"))
        time.sleep(2)
        self.pen.undo()
        
    

    def dead(self):
        msg= (""" 
                        (Game Over)    
                      Click (x) to exit
 
               """)
        self.pen.penup()
        self.pen.goto(-120,304)
        self.pen.write(msg, font=("Arial", 16, "normal"))
        
    def show_health(self):
        self.pen.undo()
        self.pen.ht()
        msg = " HP:%s" %(player.hp)
        self.pen.penup()
        self.pen.goto(-410,355)
        self.pen.color("white")         
        self.pen.write(msg, font=("Arial", 16, "normal"))

    def show_strength(self):
        self.pen2.undo()
        self.pen2.ht()
        msg = " Attack :%s" %((player.strength+player.weaponstats))
        self.pen2.penup()
        self.pen2.goto(-410,385)
        self.pen2.color("white")         
        self.pen2.write(msg, font=("Arial", 16, "normal"))



    def show_defense(self):
        self.pen7.undo()
        self.pen7.ht()
        msg = " Defense :%s" %((player.defense+player.armourstats))
        self.pen7.penup()
        self.pen7.goto(-410,415)
        self.pen7.color("white")         
        self.pen7.write(msg, font=("Arial", 16, "normal"))

    def show_level(self):
        self.pen3.undo()
        self.pen3.ht()
        msg = "Level:%s" %(player.level)
        self.pen3.penup()
        self.pen3.goto(325,385)
        self.pen3.color("white")         
        self.pen3.write(msg, font=("Arial", 16, "normal"))

    def show_healthpotion(self):
        self.pen4.undo()
        self.pen4.ht()
        msg = "Health Potion:%s" %(player.potion)
        self.pen4.penup()
        self.pen4.goto(-270,355)
        self.pen4.color("white")         
        self.pen4.write(msg, font=("Arial", 16, "normal"))


    def show_fire_scroll(self):
        self.pen5.undo()
        self.pen5.ht()
        msg = "Fire Scroll:%s" %(player.fire_scroll)
        self.pen5.penup()
        self.pen5.goto(-270,325)
        self.pen5.color("white")         
        self.pen5.write(msg, font=("Arial", 16, "normal"))
    

    def show_exp(self):
        self.pen6.undo()
        self.pen6.penup()
        self.pen6.ht()
        self.pen6.goto(320,415)
        self.pen6.color("white")
        msg = " XP:%s" %(player.exp)        
        self.pen6.write(msg, font=("Arial", 16, "normal"))

    def show_armour(self):
        self.pen2.undo()
        self.pen2.ht()
        msg = " Armour:%s" %(player.armour)
        self.pen2.penup()
        self.pen2.goto(-280,415)
        self.pen2.color("white")         
        self.pen2.write(msg, font=("Arial", 16, "normal"))

    def show_weapon(self):
        self.pen3.undo()
        self.pen3.ht()
        msg = " Weapon:%s" %(player.weapon)
        self.pen3.penup()
        self.pen3.goto(-280,385)
        self.pen3.color("white")         
        self.pen3.write(msg, font=("Arial", 16, "normal"))

                

    def lose(self):     #this is just experimenting , not in game
        wn.clear()
        wn.bgcolor("blue")
        self.goto(0, 0)
        self.color("white")
        self.write("Sorry, you lose."'\n'  "Your xp: {} points".format(self.exp), False, align="center",
                         font=("Arial", 16, "normal"))

        

class Missile(turtle.Turtle):
    def __init__(self,startx, starty):
        turtle.Turtle.__init__(self)
        self.speed = 3
        self.fd(10)
        self.penup()
        self.color("yellow")
        self.status = "ready"
        self.goto(-1000, 1000)

    def is_collision(self,other):
        a = self.xcor()- other.xcor()
        b = self.ycor()- other.ycor()
        distance = math.sqrt ((a ** 2)+(b ** 2) )

        if distance < 22: # LESS THAN 25 OR YOU ATTACK DIAGANAL 
            return True
        else:
            return False

    def is_far(self,other):
        a = self.xcor()- other.xcor()
        b = self.ycor()- other.ycor()
        distance = math.sqrt ((a ** 2)+(b ** 2) )

        if distance >25:
            return True
        else:
            return False
            

    def fire(self):
         if self.status == "ready":
            self.goto(player.xcor(), player.ycor())
            self.setheading(player.heading())
            self.status = "firing"
            if lives != 3:
                winsound.PlaySound(".\\sound\\swing.wav", winsound.SND_ASYNC)


           
            
    def move(self):
    
        if self.status == "ready":
            self.goto(-2456, 3422)
            
        
        if self.status == "firing":
            self.fd(self.speed) 
            
        #Border check


        if missile.is_far(player):
            self.setheading(player.heading())
            self.status = "ready"               
        
          
        if self.xcor() < -400 or self.xcor() > 400 or \
            self.ycor()< -400 or self.ycor()> 400:
            self.setheading(player.heading())
            self.status = "ready"

        if (self.xcor(), self.ycor()) in walls:           
            self.setheading(player.heading())
            self.status = "ready"
            
class Missile2(turtle.Turtle):
    def __init__(self,startx, starty):
        turtle.Turtle.__init__(self)
        self.shape(".\\art\\fire.gif")
        self.speed = 3
        self.fd(10)
        self.damage=400
        self.penup()
        self.color("yellow")
        self.status = "ready"
        self.goto(-1000, 1000)

    def is_collision(self,other):
        a = self.xcor()- other.xcor()
        b = self.ycor()- other.ycor()
        distance = math.sqrt ((a ** 2)+(b ** 2) )

        if distance < 30:
            return True
        else:
            return False

    def is_far(self,other):
        a = self.xcor()- other.xcor()
        b = self.ycor()- other.ycor()
        distance = math.sqrt ((a ** 2)+(b ** 2) )

        if distance >125:
            return True
        else:
            return False
            

    def fire(self):
         if self.status == "ready":
            self.goto(player.xcor(), player.ycor())
            self.setheading(player.heading())
            self.status = "firing"
            if lives != 3:
                winsound.PlaySound(".\\sound\\fireball.wav", winsound.SND_ASYNC)


           
            
    def move(self):
    
        if self.status == "ready":
            self.goto(-2456, 3422)
            
        
        if self.status == "firing":
            self.fd(self.speed) 
            
        #Border check


        if missile2.is_far(player):
            self.setheading(player.heading())
            self.status = "ready"               
        
          
        if self.xcor() < -400 or self.xcor() > 400 or \
            self.ycor()< -400 or self.ycor()> 400:
            self.setheading(player.heading())
            self.status = "ready"

        if (self.xcor(), self.ycor()) in walls:           
            self.setheading(player.heading())
            self.status = "ready"





class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
        self.fd(0)


class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape(".\\art\\heroright.gif")
        self.penup()
        self.speed()
        self.fd(0)
        self.right=1
        self.left=0
        self.up=0
        self.down=0
        self.hp=1000
        self.fullhp=1000
        self.strength=10
        self.level=1
        self.gold=0
        self.potion=0
        self.exp=0
        self.fire_scroll=0
        self.defense=0
        self.weapon=(" Iron Sword")
        self.weaponstats=2
        self.armour=(" Iron Plate")
        self.armourstats=2
        self.boss=0
        self.kill=0
        self.level2_claimed = True
        self.level3_claimed = True
        self.level4_claimed = True
        self.level5_claimed = True
        self.level6_claimed = True
        self.level7_claimed = True
        self.level8_claimed = True

    def headright(self):

        if self.right==1:
            pass

        if self.down==1:
            self.rt(270)
            self.down=0
            self.right=1         
            
        if self.left==1:
            self.rt(180)
            self.left=0
            self.right=1

        if self.up==1:
            self.rt(90)
            self.up=0
            self.right=1

        self.shape(".\\art\\heroright.gif")
        missile.shape(".\\art\\arrowright.gif")
        missile.fire()


    def headdown(self):

        if self.down==1:
            pass

        if self.left==1:
            
            self.rt(270)
            self.left=0
            self.down=1


        if self.up==1:
            
            self.rt(180)
            self.up=0
            self.down=1
    
        if self.right==1:
            
            self.rt(90)
            self.right=0
            self.down=1

        self.shape(".\\art\\herodown.gif")
        missile.shape(".\\art\\arrowdown.gif")
        missile.fire()



    def headleft(self):

        if self.left==1:
            pass

        if self.up==1:
            
            self.rt(270)
            self.up=0
            self.left=1

        if self.right==1:
            
            self.rt(180)
            self.right=0
            self.left=1

        if self.down==1:
            
            self.rt(90)
            self.down=0
            self.left=1

        self.shape(".\\art\\heroleft.gif")
        missile.shape(".\\art\\arrowleft.gif")
        missile.fire()
            
    def headup(self):
          
        if self.up==1:
            pass

        if self.right==1:
            
            self.rt(270)
            self.right=0
            self.up=1

        if self.down==1:
            
            self.rt(180)
            self.down=0
            self.up=1

        if self.left==1:
            
            self.rt(90)
            self.left=0
            self.up=1
            
        self.shape(".\\art\\heroup.gif")
        missile.shape(".\\art\\arrowup.gif")
        missile.fire()
            



         

    def go_up(self):

        if self.up==1:
            pass

        if self.right==1:
            
            self.rt(270)
            self.right=0
            self.up=1

        if self.down==1:
            
            self.rt(180)
            self.down=0
            self.up=1

        if self.left==1:
            
            self.rt(90)
            self.left=0
            self.up=1

        move_to_x = self.xcor()
        move_to_y = self.ycor()+24

        self.shape(".\\art\\heroup.gif")

        
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
            
      
        
    def go_down(self):

        if self.down==1:
            pass

        if self.left==1:
            
            self.rt(270)
            self.left=0
            self.down=1


        if self.up==1:
            
            self.rt(180)
            self.up=0
            self.down=1
    
        if self.right==1:
            
            self.rt(90)
            self.right=0
            self.down=1


        
        move_to_x = self.xcor()
        move_to_y = self.ycor()-24
        self.shape(".\\art\\herodown.gif")
        
        if (move_to_x, move_to_y) not in walls and npcs:
            self.goto(move_to_x, move_to_y)
        
        
    def go_left(self):

        if self.left==1:
            pass

        if self.up==1:
            
            self.rt(270)
            self.up=0
            self.left=1

        if self.right==1:
            
            self.rt(180)
            self.right=0
            self.left=1

        if self.down==1:
            
            self.rt(90)
            self.down=0
            self.left=1
            
        move_to_x = self.xcor()-24
        move_to_y = self.ycor()
        self.shape(".\\art\\heroleft.gif")
        
        if (move_to_x, move_to_y) not in walls :
            self.goto(move_to_x, move_to_y)


        
        
    def go_right(self):

        if self.right==1:
            pass

        if self.down==1:
            self.rt(270)
            self.down=0
            self.right=1         
            
        if self.left==1:
            self.rt(180)
            self.left=0
            self.right=1

        if self.up==1:
            self.rt(90)
            self.up=0
            self.right=1
        
        move_to_x = player.xcor()+24
        move_to_y = player.ycor()
        self.shape(".\\art\\heroright.gif")
        
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)



            
    def drink(self):
        
        
        if player.potion>0 and player.hp is not player.fullhp : 
            player.potion-=1
            info.show_healthpotion()

            if player.hp < player.fullhp-300:
                player.hp+=300
                info.show_health()
            else:
                player.hp=player.fullhp
                info.show_health()
        else:
            pass
            
    def fireball(self):
        if player.fire_scroll>0:
            player.fire_scroll-=1
            info.show_fire_scroll()
            missile2.fire()
            
            

        else:
            pass
                 

    def is_collision(self,other):
        a = self.xcor()- other.xcor()
        b = self.ycor()- other.ycor()
        distance = math.sqrt ((a ** 2)+(b ** 2) )

        if distance < 10:
            return True
        else:
            return False

    def is_collision2(self,other):
        a = self.xcor()- other.xcor()
        b = self.ycor()- other.ycor()
        distance = math.sqrt ((a ** 2)+(b ** 2) )

        if distance < 50:
            return True
        else:
            return False


    def destroy(self):
        self.goto(500,500)
        self.hideturtle()


class Item(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("turtle")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold= 1
        self.goto(x,y)

    def destroy(self):
        self.goto(1998,1998)
        self.hideturtle()




class Crown(Item):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape(".\\art\\crown.gif")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold= 100
        self.goto(x,y)

    def destroy(self):
        self.goto(1998,1998)
        self.hideturtle()


class Healing (Item):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape((".\\art\\potion.gif"))
        self.color("red")
        self.penup()
        self.goto(x,y)




class Fake_wall (Item):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape((".\\art\\wall.gif"))
        self.color("red")
        self.penup()
        self.goto(x,y)


class Npc (Item):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape(".\\art\\npc.gif")
        self.color("red")
        self.penup()
        self.goto(x,y)


class Quest (Item):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape(".\\art\\capture.gif")
        self.color("red")
        self.penup()
        self.exp=100
        self.goto(x,y)

class Quest2 (Item):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("black")
        self.penup()
        self.goto(x,y)


class Quest_item (Item):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape((".\\art\\key.gif"))
        self.penup()
        self.goto(x,y)



class Armour (Item):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape(".\\art\\armour.gif")
        self.color("grey")
        self.penup()
        self.goto(x,y)


class Sword (Item):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape(".\\art\\sword.gif")
        self.color("grey")
        self.penup()
        self.goto(x,y)


class Firescroll (Item):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape((".\\art\\scroll.gif"))
        self.color("yellow")
        self.penup()
        self.goto(x,y)
        
        
class Coin(Item):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape(".\\art\\gold.gif")
        self.color("gold")
        self.penup()
        self.gold= 100
        self.goto(x,y)


class Door(Item):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape((".\\art\\door.gif"))
        self.color("brown")
        self.penup()
        self.gold= 100
        self.goto(x,y)

class Enemy(Item):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape(".\\art\\orkleft.gif")
        self.color("red")
        self.penup()
        self.exp= 5
        self.speed(0)
        self.boss=0
        self.goto(x,y)
        self.direction=random.choice(["up","down","left","right"])
        self.hp=30
        self.damage=15
        self.alive = True


    def is_close(self,other):
        a = self.xcor()- other.xcor()
        b = self.ycor()- other.ycor()
        distance = math.sqrt ((a ** 2)+(b ** 2) )

        if distance < 100:
            return True
        else:
            return False
                


    def move(self):
        if self.direction =="up":
            dx= 0
            dy= 24
            self.shape(".\\art\\orkup.gif")
            
        elif self.direction =="down":
            dx= 0
            dy= -24
            self.shape(".\\art\\ork.gif")
          
        elif self.direction =="left":
            dx= -24
            dy= 0
            self.shape(".\\art\\orkleft.gif")

        elif self.direction =="right":
            dx= 24
            dy= 0
            self.shape(".\\art\\orkright.gif")
 
        else:
            dx = 0
            dy = 0


        if self.is_close(player):
            if player.xcor()<self.xcor():
                self.direction="left"

            elif player.xcor()>self.xcor():
                self.direction="right"

            elif player.ycor()<self.ycor():
                self.direction="down"

            elif player.ycor()>self.ycor():
                self.direction="up"
                                                                        
            
        # Calculate the spot to move to 
        move_to_x = self.xcor()+ dx
        move_to_y = self.ycor()+ dy

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            self.direction=random.choice(["up","down","left", "right"])

        turtle.ontimer(self.move,t=random.randint(100,300))


class Enemy2(Enemy):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape(".\\art\\zombiedown.gif")
        self.color("red")
        self.penup()
        self.exp= 10
        self.speed(0)
        self.goto(x,y)
        self.direction=random.choice(["up","down","left","right"])
        self.hp=70
        self.damage=30
        self.boss=0
        self.alive = True

    def is_close(self,other):
        a = self.xcor()- other.xcor()
        b = self.ycor()- other.ycor()
        distance = math.sqrt ((a ** 2)+(b ** 2) )

        if distance < 50:
            return True
        else:
            return False



    def move(self):
        if self.direction =="up":
            dx= 0
            dy= 24
            self.shape(".\\art\\zombieup.gif")
            
            
        elif self.direction =="down":
            dx= 0
            dy= -24
            self.shape(".\\art\\zombiedown.gif")
            
          
        elif self.direction =="left":
            dx= -24
            dy= 0
            self.shape(".\\art\\zombieleft.gif")
            

        elif self.direction =="right":
            dx= 24
            dy= 0
            self.shape(".\\art\\zombieright.gif")
            
 
        else:
            dx = 0
            dy = 0


        if self.is_close(player):
            if player.xcor()<self.xcor():
                self.direction="left"

            elif player.xcor()>self.xcor():
                self.direction="right"

            elif player.ycor()<self.ycor():
                self.direction="down"

            elif player.ycor()>self.ycor():
                self.direction="up"
                                                                        
            
        # Calculate the spot to move to 
        move_to_x = self.xcor()+ dx
        move_to_y = self.ycor()+ dy

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            self.direction=random.choice(["up","down","left", "right"])

        turtle.ontimer(self.move,t=random.randint(100,200))



class Enemy3(Enemy):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape(".\\art\\bossdown.gif")
        self.color("red")
        self.penup()
        self.exp= 200
        self.speed(0)
        self.goto(x,y)
        self.direction=random.choice(["up","down","left","right"])
        self.hp=8000
        self.damage=80
        self.boss=1
        self.alive = True

    def is_close(self,other):
        a = self.xcor()- other.xcor()
        b = self.ycor()- other.ycor()
        distance = math.sqrt ((a ** 2)+(b ** 2) )

        if distance < 150:
            return True
        else:
            return False



    def move(self):
        if self.direction =="up":
            dx= 0
            dy= 24
            self.shape(".\\art\\bossup.gif")
            
            
        elif self.direction =="down":
            dx= 0
            dy= -24
            self.shape(".\\art\\bossdown.gif")
            
          
        elif self.direction =="left":
            dx= -24
            dy= 0
            self.shape(".\\art\\bossleft.gif")
            

        elif self.direction =="right":
            dx= 24
            dy= 0
            self.shape(".\\art\\bossright.gif")
            
 
        else:
            dx = 0
            dy = 0


        if self.is_close(player):
            if player.xcor()<self.xcor():
                self.direction="left"

            elif player.xcor()>self.xcor():
                self.direction="right"

            elif player.ycor()<self.ycor():
                self.direction="down"

            elif player.ycor()>self.ycor():
                self.direction="up"
                                                                        
            
        # Calculate the spot to move to 
        move_to_x = self.xcor()+ dx
        move_to_y = self.ycor()+ dy

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            self.direction=random.choice(["up","down","left", "right"])

        turtle.ontimer(self.move,t=random.randint(150,300))

class Enemy4(Enemy):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape(".\\art\\ghost.gif")
        self.color("red")
        self.penup()
        self.exp= 20
        self.speed(0)
        self.goto(x,y)
        self.direction=random.choice(["up","down","left","right"])
        self.hp=300
        self.damage=50
        self.boss=0
        self.alive = True

    def is_close(self,other):
        a = self.xcor()- other.xcor()
        b = self.ycor()- other.ycor()
        distance = math.sqrt ((a ** 2)+(b ** 2) )

        if distance < 100:
            return True
        else:
            return False



    def move(self):
        if self.direction =="up":
            dx= 0
            dy= 24
            self.shape(".\\art\\ghostback.gif")
            
            
        elif self.direction =="down":
            dx= 0
            dy= -24
            self.shape(".\\art\\ghost.gif")
            
          
        elif self.direction =="left":
            dx= -24
            dy= 0
            self.shape(".\\art\\ghost.gif")
            

        elif self.direction =="right":
            dx= 24
            dy= 0
            self.shape(".\\art\\ghost.gif")
            
 
        else:
            dx = 0
            dy = 0


        if self.is_close(player):
            if player.xcor()<self.xcor():
                self.direction="left"

            elif player.xcor()>self.xcor():
                self.direction="right"

            elif player.ycor()<self.ycor():
                self.direction="down"

            elif player.ycor()>self.ycor():
                self.direction="up"
                                                                        
            
        # Calculate the spot to move to 
        move_to_x = self.xcor()+ dx
        move_to_y = self.ycor()+ dy

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            self.direction=random.choice(["up","down","left", "right"])

        turtle.ontimer(self.move,t=random.randint(150,300))

class Particle(Item):
    def __init__(self, spriteshape, color, startx, starty):
        turtle.Turtle.__init__(self, shape = spriteshape)
        self.shapesize(stretch_wid=0.1, stretch_len=0.1, outline=None)
        self.penup()
        self.goto(-1000,-1000)
        self.frame = 0
        self.speed(0)
        self.penup()
        self.color(color)
        self.fd(0)

        
    def explode(self, startx, starty):
        self.goto(startx,starty)
        self.setheading(random.randint(0,360))
        self.frame = 1

    def move(self):
        if self.frame > 0:
            self.fd(10)
            self.frame += 1

        if self.frame > 15:
            self.frame = 0
            self.goto(-1000, -1000)



particles = []

for i in range(15):
        particles.append(Particle("circle", "red", 0, 0))
mission=0
lives=0
quests2=[]
quests=[]
quest_items=[]
armourupgrade=0
weaponupgrade=0
crowns=[]
enemies2 =[]
enemies =[]   
coins =[]
doors =[]
healings=[]
fake_walls=[]
npcs=[]
firescrolls=[]
swords=[]
armours=[]
walls=[]

levels = [""]

level_1 =[
                 
"GGGGGGGGGGGGGGGGGGGGGGGGGGGGGG",
"G    R    P      GG          G",
"G                      G     G",
"G  GGG   GG    GG            G",
"G                      GG    G",
"G  R                         G",
"G  GGG    G GG     R         G",
"G                            G",
"G GG   GG              GG    G",
"G          G           G     G",
"G  GG      GGG               G",
"G  GG G          G  GGG      G",
"G  G                     R   G",
"G    G  G  G   G             G",
"GRRRRRRR           GGG       G",
"G      R   G                 G",
"G  RR              GG   GG   G",
"G  RRR                       G",
"G    R GGG             G     G",
"G   R      GG  T   T         G",
"G   R          X   X   R     G",
"G  ER    GG    T   T         G",
"GR RR       XXXX  NXXXX      G",
"GR RRRR     X         X      G",
"GR F  R     X    D    X G    G",
"GRCC HR     X         X GG   G",
"GRRRRRR     XXXTXYXTXXX      G",
"GGGGGGGGGGGGGGGGGGGGGGGGGGGGGG",
    ]


level_2 =[


"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X  P       XXXCCCH           X",
"XXXX   XXXXXXXXXXXXXXYXXX    X",
"XFFX   X         E           X",
"X  X   XXXXXT  TXXXXXXXXXXXXXX",
"X                  X       CCX",
"X     XXXXX   E    X         X",
"XC X  X   X        X       E X",
"XC X  X   X                  X",
"XXXX  T   XXXXXXXXXXXT   TXXXX",
"X                    X       X",
"X     T              X       X",
"X     X              X   E   X",
"X     X    E         X       X",
"X     X        F     XCC     X",
"XXXXXXXXXT   TXXXXXXXXXXX    X",
"X                            X",
"X   XXXXXXXXXXXXXXXXXX       X",
"X   XH             F X E     X",
"X   X                X    E  X",
"X   X  E       CCCCC X A     X",
"X   XXXXXT   TXXXXXXXXXXX    X",
"X                            X",
"X                            X",
"X   XXXXXXXXXXXXXXXXXXXXXXXXXX",
"X               E      E    FX",
"XD                     E    HX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    ]


level_3 =[


"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X P    X       CCCCCCCCCFX D X",
"X      X   X   XXXXXXXXXXT   X",
"X          XE  XFCCCCCC      X",
"X  X   XXXXX   XXXXXXXXXXT   X",
"X  X   X  E              X   X",
"X  X   XXXXXXXXXXXXXXXXX X   X",
"X  X   X       CCC     X X   X",
"X  XXXXX   E   CCC     X X   X",
"X              CCC    HX X   X",
"XXX    XXXXXXXXT   TXXXX X   X",
"X      X  FFF  X   X   E     X",
"X      XECCCCC X   X         X",
"X  E   X  E    X   X         X",
"X  E   XXXXXX  XF  X         X",
"X  E   X       XXXXXXXXXXX   X",
"X      X       X     H XE    X",
"X         E    X       X     X",
"X   VVVVVVVVVVVV       X     X",
"X   V  Z       V   EE  X     X",
"X   V  Z       V       X     X",
"X   VVVVVVVVVVVV   XXXXX     X",
"X                            X",
"X  E         X EEE           X",
"XXXXXXXT   TXXXXXXXXXXXXXYXYXX",
"XF             X   CCC    S  X",
"X      E           CCC       X",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    ]

level_4 =[

"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X                            X",
"X  TXXXXXXXXXXXXXXXXXXXXXX   X",
"X          EE  CCCCCCCCCFX   X",
"X  TXXXXXXXXXXXXXXXXXXXXXX   X",
"X  X   E                     X",
"X  X   XXXX    XXXXXXXT  TXXXX",
"X  X   X       X             X",
"X  X   XE  Z   XEE           X",
"X  X   X   XXXXXXXXX   Z     X",
"X  X   X   Y       Y         X",
"X  XE  TXXXX       X       F X",
"X  X          CCC  XXXXXXXXXXX",
"X  X          CCC          P X",
"X  X   TXXXX  CCC  XXXXXXXXXXX",
"X  X   X   X       X    X    X",
"X  X   XE  Y       Y  X X X  X",
"X  X   XE  XXXXXXXXX  X X X  X",
"X  X   XXX    X  ZZZZZX X X  X",
"X  X     X XX X  XZZZZX   X  X",
"X  XXXXX X XX XX XXXXXXXXXX  X",
"X  XH  X   XX    X      D X  X",
"X  X   XXXXXXXXXXX        X  X",
"X                   Z     X  X",
"X      E                  X  X",
"X  XXXXXXXX      X     TXXX  X",
"X  XCCCCCCE     EX           X",
"XXXXXXXXXXXXXXXXXXXXXXXTXXXXXX",


    ]


level_5 =[


"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XZCCCCCCCCCCCCC       XT     X",
"XCCCCCCCCCCCCCC            D X",
"XHCCCCCCCCCCCCC       XT     X",
"XXXXXXXXXXXXXXXXXXXXXXXXX    X",
"XIIIIIIIIIIIYXXXXXXXXFFFXZ   X",
"XIXXXXXXXX   E      X   X    X",
"XIX   XXXX F      H X   X    X",
"XIX   XXXX     S    X   X    X",
"XII   XXXX          X  XXX   X",
"XXT   TXXXXXXXXXXXXXX  XXX   X",
"X                      XXX   X",
"X  Z                         X",
"X          XXXXXXXXX         X",
"X  XXXX    X   Z        X    X",
"X  XXXX    XF           TXXXXX",
"X  XXXXZ   XXXXXXXXXZ     CCCX",
"X  XCCCC                TXXXXX",
"X  XXXXXXXXXXXXXXX      XCCC X",
"X      CCCCCCCCXXX Z    XCCC X",
"X                       XCCC X",
"X  X   Z           XXXXXX    X",
"X  X                   Z     X",
"X  XXXXXXXXXXXXXXXXZZ       ZX",
"X      T        XXXXXXXXXXXXXX",
"X         EEEEEE             X",
"X      T  EEEEEE           P X",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
]


level_6 =[


"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X  V               TXX       X",
"X QV   EE              XX    X",
"XVVV               TXXXXX  P X",
"X  E       Z  XXXXXXXXXXXXXXXX",
"X      E      X            F X",
"XXXXXXXXXXXX  X   XXXXXXX    X",
"X   CCCCCCFX  X   X  L HX    X",
"X   XXXXXXXT  T   X     X    X",
"X                 X   L X    X",
"X   XXXXXXXXXXXXYIX     X    X",
"X   XF A  EE    IIX     XZ   X",
"X   XF    EE    XXX     T    X",
"X   XXXXXXXXXXXXXXXX         X",
"X   XH  L  X    FF X         X",
"X   XC      L      X    T    X",
"X   XC Z           X    X    X",
"X   XC     X       X    X    X",
"X   XXXXXXXXXX   XXX    X    X",
"X                  X    X    X",
"XXXXXXXXXXXXXT   TXXX  XX    X",
"XCCC               X         X",
"XCCC   ZZ          X   LLLL  X",
"XCCC        XT   TXXXX L  L  X",
"XXXXXXXXXXXXX        X       X",
"X     L              X       X",
"X  D       ZZZ       X B     X",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
]



level_7 =[

"         K                   ",
"XXXXXXXTXYXTXXXXXXXXXXXXXXXXXX",
"X  P                         X",
"X                   XXXX     X",
"XXXXXXXXXXXXX       XXXXL    X",
"X                   XXXX     X",
"X  L                         X",
"X              XXXX          X",
"X  XXXX        XXXX          X",
"X  XXXXL       XXXX          X",
"X  XXXX                      X",
"X          L           XXXX  X",
"X                      XXXX  X",
"X          XXXX        XXXX  X",
"X XXXX     XXXX              X",
"X XXXX     XXXX     XXXX     X",
"X XXXX              XXXX     X",
"X       XXXX        XXXX     X",
"X       XXXX         J       X",
"X       XXXX             L   X",
"X  XXXX              XXXX    X",
"X  XXXX     XXXXT    XXXX    X",
"X  XXXX   L X        XXXX    X",
"XH          X  XT          H X",
"XXXXXXXXXXXXX  XXXXXXXXXXXXXXX",
"X  E   E    T  T    E  E     X",
"X                      D     X",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
]


level_8 =[

"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XCCCCCCCCCCCCCCCCCCCCCCCCCCCCX",
"XCCCCCCCCCCCCCCCCCCCCCCCCCCCCX",
"XCCCCCCCCCCCCCCCCCCCCCCCCCCCCX",
"XCCCCCCCCCCCCCCCCCCCCCCCCCCCCX",
"XCCCCCCCCCCCCCCCCCCCCCCCCCCCCX",
"XCCCCCCCCCCCCCCCCCCCCCCCCCCCCX",
"XCCCCCCXXXXXXXXXXXXXXCCCCCCCCX",
"XCCCCCCXL L L L L L XCCCCCCCCX",
"XCCCCCCXZ Z Z Z Z ZZXCCCCCCCCX",
"XCCCCCCXZE E E E E ZXCCCCCCCCX",
"XCCCCCCX EVVVVVVEZLZXCCCCCCCCX",
"XCCCCCCXZ V P  V E  XCCCCCCCCX",
"XCCCCCCX EV    VLZ ZXCCCCCCCCX",
"XCCCCCCXZEVV  VVE   XCCCCCCCCX",
"XCCCCCCXZ  V  V  ZZZXCCCCCCCCX",
"XCCCCCCXL LV  V L L XCCCCCCCCX",
"XCCCCCCXXXXT  TXXXXXXCCCCCCCCX",
"XCCCCCCCX         XCCCCCCCCCCX",
"XCCCCCCCX         XCCCCCCCCCCX",
"XCCCCCCCX         XCCCCCCCCCCX",
"XCCCCCCCXXXT   TXXXCCCCCCCCCCX",
"XCCCCCCCX         XCCCCCCCCCCX",
"XCCCCCCCI         ICCCCCCCCCCX",
"XCCCCCCCXXT     TXXCCCCCCCCCCX",
"XCCCCCCCCCX  M  XCCCCCCCCCCCCX",
"XCCCCCCCCCX     XCCCCCCCCCCCCX",
"XXXXXXXXXXXTXYXTXXXXXXXXXXXXXX",

]



levels.append(level_1)
levels.append(level_2)
levels.append(level_3)
levels.append(level_4)
levels.append(level_5)
levels.append(level_6)
levels.append(level_7)
levels.append(level_8)

#row are y ( up/down) column are x (left and right )
# 

def setup_maze(level):
    for y in range (len(level)): #tell how many rows there is 
        for x in range(len(level[y])): # acquire every x of the y row
            #Get the character at each x,y coordinate
            #NOTE the order of Y AND X in the next line
            character = level [y][x]
            #Calculate the screen x,y coordinates.  Furtherest left upper corner is (0,0)
            screen_x = -350 + (x*24)
            screen_y = 288 - (y*24)

            #check if it is an x  represent a wall
            if character == "X":   
                pen.goto(screen_x, screen_y)
                pen.shape(".\\art\\wall.gif")
                pen.stamp()
                walls.append((screen_x,screen_y))

            if character == "T":   
                pen.goto(screen_x, screen_y)
                pen.shape(".\\art\\torch.gif")
                pen.stamp()
                walls.append((screen_x,screen_y))

            if character == "Y":   
                pen.goto(screen_x, screen_y)
                pen.shape(".\\art\\skeleton.gif")
                pen.stamp()
                walls.append((screen_x,screen_y))

            if character == "G":   
                pen.goto(screen_x, screen_y)
                pen.shape(".\\art\\tree.gif")
                pen.stamp()
                walls.append((screen_x,screen_y))

            if character == "R":   
                pen.goto(screen_x, screen_y)
                pen.shape(".\\art\\rock.gif")
                pen.stamp()
                walls.append((screen_x,screen_y))

            if character == "V":   
                pen.goto(screen_x, screen_y)
                pen.shape(".\\art\\cage.gif")
                pen.stamp()
                walls.append((screen_x,screen_y))




            
            if character == "P":   # p= player 
                player.goto(screen_x, screen_y)

            if  character == "C":
                coins.append(Coin(screen_x, screen_y))
                
            if character =="E":
                enemies.append(Enemy(screen_x, screen_y))

            if character =="D":
                doors.append(Door(screen_x, screen_y))

            if character =="M":
                crowns.append(Crown(screen_x, screen_y))

            if character =="H":
                healings.append(Healing(screen_x, screen_y))

            if character =="F":
                firescrolls.append(Firescroll(screen_x, screen_y))

            if character =="A":
                armours.append(Armour(screen_x, screen_y))

            if character =="S":
                swords.append(Sword(screen_x, screen_y))

            if character =="Z":
                enemies.append(Enemy2(screen_x, screen_y))


            if character =="N":
                npcs.append(Npc(screen_x, screen_y))

            if character =="Q":
                quests.append(Quest(screen_x, screen_y))

            if character =="B":
                quest_items.append(Quest_item(screen_x, screen_y))

            if character =="I":
                fake_walls.append(Fake_wall(screen_x, screen_y))

            if character =="J":
                enemies.append(Enemy3(screen_x, screen_y))

            if character =="L":
                enemies.append(Enemy4(screen_x, screen_y))

            if character =="K":
                quests2.append(Quest2(screen_x, screen_y))
              
              
pen=Pen()
player= Player()
missile = Missile(0, 0)
missile2 = Missile2(0, 0)


setup_maze(levels[1])
maze=("level1")

info=Info()
game=Info()
game.draw_border()
game.draw_border2()
game.draw_border3()
game.draw_border4()
game.show_rules()
game.show_gold()
game.show_armour()
game.show_weapon()
info.show_health()
info.show_strength()
info.show_level()
info.show_healthpotion()
info.show_fire_scroll()
info.show_exp()
info.show_defense()





#keyboard binding

turtle.listen()
turtle.onkey(player.go_left, "Left")
turtle.onkey(player.go_right, "Right")
turtle.onkey(player.go_up, "Up")
turtle.onkey(player.go_down, "Down")
turtle.onkey(player.headright, "d")
turtle.onkey(player.headleft, "a")
turtle.onkey(player.headdown,"s")
turtle.onkey(player.headup,"w")
turtle.onkey(player.headright, "D")
turtle.onkey(player.headleft, "A")
turtle.onkey(player.headdown,"S")
turtle.onkey(player.headup,"W")
turtle.onkey(player.drink,"space")
turtle.onkey(player.fireball,"z")
turtle.onkey(player.fireball,"Z")


for enemy in enemies:
    turtle.ontimer(enemy.move,t=250)

      #(experiementing with inputs within game ) 



while True:

    
    missile.move()
    missile2.move()

    for particle in particles:
        particle.move()
        
    for armour in armours:

        if player.is_collision(armour):

            armour.destroy()

            if armourupgrade==1:
                player.armourstats+=4
                player.armour=("Mythril Plate")
                game.show_armour()
                info.show_defense()
                armourupgrade+=1
                winsound.PlaySound(".\\sound\\armour.wav", winsound.SND_ASYNC)

            if armourupgrade==0:
                player.armourstats+=6
                player.armour=("Steel Plate")
                game.show_armour()
                info.show_defense()
                armourupgrade+=1
                winsound.PlaySound(".\\sound\\armour.wav", winsound.SND_ASYNC)

    for npc in npcs:

        if player.is_collision(npc):          
            game.intro()         
            Npc.destroy(npc)
                
    for quest in quests:

        if player.is_collision2(quest):
            if mission ==0:
                game.start()
            
            if mission ==1:
                game.end()
                player.exp+=quest.exp
                info.show_exp()
                Quest.destroy(quest)


    for quest2 in quests2:

        if player.is_collision2(quest2):
            if player.boss ==0:
                game.start2()
            
            if player.boss ==1:
                game.end2()
                player.exp+=200
                info.show_exp()
                Quest.destroy(quest2)

    for quest_item in quest_items:
        if player.is_collision(quest_item):
            mission=1
            Quest_item.destroy(quest_item)
            winsound.PlaySound(".\\sound\\key.wav", winsound.SND_ASYNC)
        
                            


 
    for sword in swords:

        if player.is_collision(sword):

            sword.destroy()

            if  weaponupgrade==1:
                player.weaponstats+=4
                player.weapon=("Mythril Sword")
                game.show_weapon()
                info.show_strength()
                weaponupgrade+=1
                winsound.PlaySound(".\\sound\\sword.wav", winsound.SND_ASYNC)

            if  weaponupgrade==0:
                player.weaponstats+=6
                player.weapon=("Steel Sword")
                game.show_weapon()
                info.show_strength()
                weaponupgrade+=1
                winsound.PlaySound(".\\sound\\sword.wav", winsound.SND_ASYNC)






    for firescroll in firescrolls:

        if player.is_collision(firescroll):

            firescroll.destroy()
            player.fire_scroll+=1
            info.show_fire_scroll()
            winsound.PlaySound(".\\sound\\scroll.wav", winsound.SND_ASYNC)


    for healing in healings:

        if player.is_collision(healing):

            healing.destroy()
            player.potion+=1
            info.show_healthpotion()
            winsound.PlaySound(".\\sound\\potion.wav", winsound.SND_ASYNC)
        

        

    for crown in crowns:
        
        if player.is_collision(crown):
            
            #winsound.PlaySound(".\\sound\\victory.wav",0)
            player.destroy()
            crown.destroy()
            crowns.remove(crown)
            lives=3
            game.win()
            
            
                 

    for enemy in enemies:
        if missile.is_collision(enemy):
            enemy.hp -= (player.strength+player.weaponstats)
            missile.status = "ready"
            winsound.PlaySound(".\\sound\\orkdeath.wav", winsound.SND_ASYNC)

        if missile2.is_collision(enemy):
            enemy.hp -= missile2.damage
            missile2.status = "ready"
            winsound.PlaySound(".\\sound\\orkdeath.wav", winsound.SND_ASYNC)


        if enemy.hp<=0 and enemy.alive==True:
            enemy.alive=False 
            Enemy.destroy(enemy)
            missile.status = "ready"
            player.exp += enemy.exp
            player.boss+=enemy.boss
            player.kill+=1
            info.show_exp()
            winsound.PlaySound(".\\sound\\orkdeath.wav", winsound.SND_ASYNC)

            if player.exp>70 and player.level2_claimed:
                player.hp=1100
                player.fullhp=1100
                player.strength=20
                player.defense=4
                player.level=2
                player.level2_claimed = False
                info.show_defense()
                info.show_health()
                info.show_strength()
                info.show_level()
                winsound.PlaySound(".\\sound\\levelup.wav", winsound.SND_ASYNC)
                time.sleep(1)
           

            if player.exp>150 and player.level3_claimed:
                player.hp=1200
                player.fullhp=1200
                player.strength=25
                player.defense=8
                player.level=3
                player.level3_claimed = False
                info.show_defense()
                info.show_health()
                info.show_strength()
                info.show_level()
                winsound.PlaySound(".\\sound\\levelup.wav", winsound.SND_ASYNC)
                time.sleep(1)
           
            if player.exp>300 and player.level4_claimed:
                player.hp=1300
                player.fullhp=1300
                player.strength=30
                player.defense=12
                player.level=4
                player.level4_claimed = False
                info.show_defense()
                info.show_health()
                info.show_strength()
                info.show_level()
                winsound.PlaySound(".\\sound\\levelup.wav", winsound.SND_ASYNC)
                time.sleep(1)
            

            if player.exp>450 and player.level5_claimed:
                player.hp=1500
                player.fullhp=1500
                player.strength=40
                player.defense=20
                player.level=5
                player.level5_claimed = False
                info.show_defense()
                info.show_health()
                info.show_strength()
                info.show_level()
                winsound.PlaySound(".\\sound\\levelup.wav", winsound.SND_ASYNC)
                time.sleep(1)

            if player.exp>700 and player.level6_claimed:
                player.hp=1700
                player.fullhp=1700
                player.strength=60
                player.defense=25
                player.level=6
                player.level6_claimed = False
                info.show_defense()
                info.show_health()
                info.show_strength()
                info.show_level()
                winsound.PlaySound(".\\sound\\levelup.wav", winsound.SND_ASYNC)
                time.sleep(1)

            if player.exp>950 and player.level7_claimed:
                player.hp=2000
                player.fullhp=2000
                player.strength=80
                player.defense=30
                player.level=7
                player.level7_claimed = False
                info.show_defense()
                info.show_health()
                info.show_strength()
                info.show_level()
                winsound.PlaySound(".\\sound\\levelup.wav", winsound.SND_ASYNC) 
                time.sleep(1)

            if player.exp>1400 and player.level8_claimed:
                player.hp=2200
                player.fullhp=2200
                player.strength=100
                player.defense=50
                player.level=8
                player.level8_claimed = False
                info.show_defense()
                info.show_health()
                info.show_strength()
                info.show_level()
                winsound.PlaySound(".\\sound\\levelup.wav", winsound.SND_ASYNC) 
                time.sleep(1)

                               
                               
            
    for coin in coins:
        if player.is_collision(coin):
            player.gold += coin.gold
            game.show_gold()
            #print("Player Gold: {}".format (game.gold))
            coin.destroy()
            coins.remove(coin)
            winsound.PlaySound(".\\sound\\coin.wav", winsound.SND_ASYNC)

    for enemy in enemies:
        if player.is_collision(enemy):
            attack=enemy.damage
            reduce_damage=attack-(player.defense+player.armourstats)
            if reduce_damage <0 :
                reduce_damage=0

            player.hp-=reduce_damage
            info.show_health()

            for particle in particles:
                particle.explode(player.xcor(), player.ycor())

            
            

       
            

    for door in doors:
        if player.is_collision(door):
            walls.clear()
            pen.clear()
            wn.bgpic(".\\art\\black.gif")
            for enemy in enemies:
                Enemy.destroy(enemy)
            for coin in coins:
                Coin.destroy(coin)
            for door in doors:
                Door.destroy(door)
            for armour in armours:
                Armour.destroy(armour)
            for sword in swords:
                Sword.destroy(sword)
            for healing in healings:
                Healing.destroy(healing)
            for firescroll in firescrolls:
                Firescroll.destroy(firescroll)
            for npc in npcs:
                Npc.destroy(npc)
            for quest in quests:
                Quest.destroy(quest)
            for quest_item in quest_items:
                Quest_item.destroy(quest_item)
            for fake_wall in fake_walls:
                Fake_wall.destroy(fake_wall)
            for quest2 in quests2:
                Quest2.destroy(quest2)
                
            

                
            winsound.PlaySound(".\\sound\\unlock.wav", winsound.SND_ASYNC)
    
            
            if maze==("level1"):
            
                setup_maze(levels[2])
                maze=("level2")
                
                
            elif maze ==("level2"):
                setup_maze(levels[3])
                maze=("level3")
                
                
            elif maze==("level3"):
                setup_maze(levels[4])
                maze=("level4")
                

            elif maze==("level4"):
                setup_maze(levels[5])
                maze=("level5")

            elif maze==("level5"):
                setup_maze(levels[6])
                maze=("level6")

            elif maze==("level6"):
                setup_maze(levels[7])
                maze=("level7")

            elif maze==("level7"):
                setup_maze(levels[8])
                maze=("level8")
            
                   
            else:
                pass

            
             
            for enemy in enemies:
                turtle.ontimer(enemy.move,t=250)
    
    if player.hp<=0:
        game.dead()
        player.destroy()
        winsound.PlaySound(".\\sound\\death.wav", winsound.SND_ASYNC)
        time.sleep(2)
        info.show_health()
        break
       


              
        

    wn.update()

