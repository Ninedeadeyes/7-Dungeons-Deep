import turtle
import random
import math


class Enemy(turtle.Turtle):
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

    def move(self,block,bob):
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


        if self.is_close(bob):
            if bob.xcor()<self.xcor():
                self.direction="left"

            elif bob.xcor()>self.xcor():
                self.direction="right"

            elif bob.ycor()<self.ycor():
                self.direction="down"

            elif bob.ycor()>self.ycor():
                self.direction="up"
                                                                        
            
        # Calculate the spot to move to 
        move_to_x = self.xcor()+ dx
        move_to_y = self.ycor()+ dy

        if (move_to_x, move_to_y) not in block:
            self.goto(move_to_x, move_to_y)

        else:
            self.direction=random.choice(["up","down","left", "right"])

        turtle.ontimer(self.move(block,bob),t=random.randint(100,300))


    def destroy(self):
        self.goto(1998,1998)
        self.hideturtle()

    


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

    def move(self,block,bob):
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


        if self.is_close(bob):
            if bob.xcor()<self.xcor():
                self.direction="left"

            elif bob.xcor()>self.xcor():
                self.direction="right"

            elif bob.ycor()<self.ycor():
                self.direction="down"

            elif bob.ycor()>self.ycor():
                self.direction="up"
                                                                        
            
        # Calculate the spot to move to 
        move_to_x = self.xcor()+ dx
        move_to_y = self.ycor()+ dy

        if (move_to_x, move_to_y) not in block:
            self.goto(move_to_x, move_to_y)
        else:
            self.direction=random.choice(["up","down","left", "right"])

        turtle.ontimer(self.move(block,bob),t=random.randint(100,300))

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

    def move(self,block,bob):
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


        if self.is_close(bob):
            if bob.xcor()<self.xcor():
                self.direction="left"

            elif bob.xcor()>self.xcor():
                self.direction="right"

            elif bob.ycor()<self.ycor():
                self.direction="down"

            elif bob.ycor()>self.ycor():
                self.direction="up"
                                                                        
            
        # Calculate the spot to move to 
        move_to_x = self.xcor()+ dx
        move_to_y = self.ycor()+ dy

        if (move_to_x, move_to_y) not in block:
            self.goto(move_to_x, move_to_y)
        else:
            self.direction=random.choice(["up","down","left", "right"])

        turtle.ontimer(self.move(block,bob),t=random.randint(100,300))

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

    def move(self,block,bob):
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


        if self.is_close(bob):
            if bob.xcor()<self.xcor():
                self.direction="left"

            elif bob.xcor()>self.xcor():
                self.direction="right"

            elif bob.ycor()<self.ycor():
                self.direction="down"

            elif bob.ycor()>self.ycor():
                self.direction="up"
                                                                        
            
        # Calculate the spot to move to 
        move_to_x = self.xcor()+ dx
        move_to_y = self.ycor()+ dy

        if (move_to_x, move_to_y) not in block:
            self.goto(move_to_x, move_to_y)
        else:
            self.direction=random.choice(["up","down","left", "right"])

        turtle.ontimer(self.move(block,bob),t=random.randint(100,300))
