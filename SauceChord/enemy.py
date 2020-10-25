from direction import Direction
from item import Item
import turtle
import math
import random

class Enemy(Item):
    hero = None
    walls = None

    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.proximity = 100
        self.moveTimerMin = 100
        self.moveTimerMax = 300        
        self.upShape = "undefined"
        self.downShape = "undefined"
        self.leftShape = "undefined"
        self.rightShape = "undefined"
        self.exp = 5
        self.boss = 0
        self.hp = 30
        self.damage = 15
        self.alive = True
        
        self.color("red")
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.direction = Direction.random()

    def face(self, direction):
        if (direction == Direction.up):
            self.shape(self.upShape)
        elif (direction == Direction.down):
            self.shape(self.downShape)
        elif (direction == Direction.left):
            self.shape(self.leftShape)
        elif (direction == Direction.right):
            self.shape(self.rightShape)

    def is_close(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt ((a ** 2) + (b ** 2))
        return distance < self.proximity

    def move(self):
        if self.is_close(Enemy.hero):
            if Enemy.hero.xcor() < self.xcor():
                self.direction = Direction.left
            elif Enemy.hero.xcor() > self.xcor():
                self.direction = Direction.right
            elif Enemy.hero.ycor() < self.ycor():
                self.direction = Direction.down
            elif Enemy.hero.ycor() > self.ycor():
                self.direction = Direction.up
            
        if self.direction == Direction.up:
            dx = 0
            dy = 24
        elif self.direction == Direction.down:
            dx = 0
            dy = -24
        elif self.direction == Direction.left:
            dx = -24
            dy = 0
        elif self.direction == Direction.right:
            dx = 24
            dy = 0

        # Calculate the spot to move to 
        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy

        if (move_to_x, move_to_y) not in Enemy.walls:
            self.goto(move_to_x, move_to_y)
        else:
            self.direction = Direction.random()

        self.face(self.direction)

        turtle.ontimer(self.move, t = random.randint(self.moveTimerMin, self.moveTimerMax))

class Orc(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.upShape = ".\\art\\orkup.gif"
        self.downShape = ".\\art\\ork.gif"
        self.leftShape = ".\\art\\orkleft.gif"
        self.rightShape = ".\\art\\orkright.gif"
        self.proximity = 100
        self.moveTimerMin = 100
        self.moveTimerMax = 300        
        self.exp = 5
        self.hp = 30
        self.damage = 15
        self.boss = 0
        self.face(self.direction)

class Zombie(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.upShape = ".\\art\\zombieup.gif"
        self.downShape = ".\\art\\zombiedown.gif"
        self.leftShape = ".\\art\\zombieleft.gif"
        self.rightShape = ".\\art\\zombieright.gif"
        self.proximity = 50
        self.moveTimerMin = 100
        self.moveTimerMax = 200        
        self.exp = 10
        self.hp = 70
        self.damage = 30
        self.boss = 0
        self.face(self.direction)

class Boss(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.upShape = ".\\art\\bossup.gif"
        self.downShape = ".\\art\\bossdown.gif"
        self.leftShape = ".\\art\\bossleft.gif"
        self.rightShape = ".\\art\\bossright.gif"
        self.proximity = 150
        self.moveTimerMin = 150
        self.moveTimerMax = 300        
        self.exp = 200
        self.hp = 8000
        self.damage = 80
        self.boss = 1
        self.face(self.direction)

class Ghost(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.upShape = ".\\art\\ghostback.gif"
        self.downShape = ".\\art\\ghost.gif"
        self.leftShape = ".\\art\\ghost.gif"
        self.rightShape = ".\\art\\ghost.gif"
        self.proximity = 100
        self.moveTimerMin = 150
        self.moveTimerMax = 300        
        self.exp = 20
        self.hp = 300
        self.damage = 50
        self.boss = 0
        self.face(self.direction)