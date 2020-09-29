
import turtle
import math
import random



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


