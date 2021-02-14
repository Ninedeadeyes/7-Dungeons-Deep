import time
import turtle 
import winsound

class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
        self.fd(0)


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
        self.level2_claimed = True
        self.level3_claimed = True
        self.level4_claimed = True
        self.level5_claimed = True
        self.level6_claimed = True
        self.level7_claimed = True
        self.level8_claimed = True
        
        
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
        msg = "Gold: %s"  %(self.gold)
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
     

    def win(self,bob):

        
        if bob.kill==0:    # If player does not kill anything is given an alternative ending 
                            # for whatever reason won't work with with just 'self' hence had to add parameter 
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
        msg = " HP:%s" %(self.hp)
        self.pen.penup()
        self.pen.goto(-410,355)
        self.pen.color("white")         
        self.pen.write(msg, font=("Arial", 16, "normal"))

    def show_strength(self):
        self.pen2.undo()
        self.pen2.ht()
        msg = " Attack :%s" %((self.strength+self.weaponstats))
        self.pen2.penup()
        self.pen2.goto(-410,385)
        self.pen2.color("white")         
        self.pen2.write(msg, font=("Arial", 16, "normal"))



    def show_defense(self):
        self.pen7.undo()
        self.pen7.ht()
        msg = " Defense :%s" %((self.defense+self.armourstats))
        self.pen7.penup()
        self.pen7.goto(-410,415)
        self.pen7.color("white")         
        self.pen7.write(msg, font=("Arial", 16, "normal"))

    def show_level(self):
        self.pen3.undo()
        self.pen3.ht()
        msg = "Level:%s" %(self.level)
        self.pen3.penup()
        self.pen3.goto(325,385)
        self.pen3.color("white")         
        self.pen3.write(msg, font=("Arial", 16, "normal"))

    def show_healthpotion(self):
        self.pen4.undo()
        self.pen4.ht()
        msg = "Health Potion:%s" %(self.potion)
        self.pen4.penup()
        self.pen4.goto(-270,355)
        self.pen4.color("white")         
        self.pen4.write(msg, font=("Arial", 16, "normal"))


    def show_fire_scroll(self):
        self.pen5.undo()
        self.pen5.ht()
        msg = "Fire Scroll:%s" %(self.fire_scroll)
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
        msg = " XP:%s" %(self.exp)        
        self.pen6.write(msg, font=("Arial", 16, "normal"))

    def show_armour(self):
        self.pen2.undo()
        self.pen2.ht()
        msg = " Armour:%s" %(self.armour)
        self.pen2.penup()
        self.pen2.goto(-280,415)
        self.pen2.color("white")         
        self.pen2.write(msg, font=("Arial", 16, "normal"))

    def show_weapon(self):
        self.pen3.undo()
        self.pen3.ht()
        msg = " Weapon:%s" %(self.weapon)
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

