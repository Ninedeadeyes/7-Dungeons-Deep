import turtle
import math
import winsound


class Missile(turtle.Turtle):
    def __init__(self,startx, starty,log):
        turtle.Turtle.__init__(self)
        self.speed = 3
        self.fd(10)
        self.penup()
        self.color("yellow")
        self.status = "ready"
        self.goto(-1000, 1000)
        self.lives = 0

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
            

    def fire(self,log,mom):
         if self.status == "ready":
            self.goto(log.xcor(), log.ycor())
            self.setheading(log.heading())
            self.status = "firing"
            if mom != 3:
                winsound.PlaySound(".\\sound\\swing.wav", winsound.SND_ASYNC)     
            
    def move(self,log,block):
    
        if self.status == "ready":
            self.goto(-2456, 3422)
            
        
        if self.status == "firing":
            self.fd(self.speed)
            
            
        #Border check


        if  self.is_far(log):
            self.setheading(log.heading())
            self.status = "ready"               
        
          
        if self.xcor() < -400 or self.xcor() > 400 or \
            self.ycor()< -400 or self.ycor()> 400:
            self.setheading(log.heading())
            self.status = "ready"

        if (self.xcor(), self.ycor()) in block:           
            self.setheading(log.heading())
            self.status = "ready"
            
class Missile2(turtle.Turtle):
    def __init__(self,startx, starty,log):
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
            

    def fire(self,log,mom):
         if self.status == "ready":
            self.goto(log.xcor(), log.ycor())
            self.setheading(log.heading())
            self.status = "firing"
            if mom != 3:
                winsound.PlaySound(".\\sound\\fireball.wav", winsound.SND_ASYNC)

            
    def move(self,log,block):
    
        if self.status == "ready":
            self.goto(-2456, 3422)
            
        
        if self.status == "firing":
            self.fd(self.speed) 
            
        #Border check


        if self.is_far(log):
            self.setheading(log.heading())
            self.status = "ready"               
        
          
        if self.xcor() < -400 or self.xcor() > 400 or \
            self.ycor()< -400 or self.ycor()> 400:
            self.setheading(log.heading())
            self.status = "ready"

        if (self.xcor(), self.ycor()) in block:           
            self.setheading(log.heading())
            self.status = "ready"

