
import turtle
import math
import random
import winsound


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
        self.kill=0

    def headright(self,proj,bug):

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
        proj.shape(".\\art\\arrowright.gif")
        proj.fire(self,bug)


    def headdown(self,proj,bug):

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
        proj.shape(".\\art\\arrowdown.gif")
        proj.fire(self,bug)

    def headleft(self,proj,bug):

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
        proj.shape(".\\art\\arrowleft.gif")
        proj.fire(self,bug)
            
    def headup(self,proj,bug):
          
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
        proj.shape(".\\art\\arrowup.gif")
        proj.fire(self,bug)
 

    def go_up(self,block):

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

        
        if (move_to_x, move_to_y) not in block:
            self.goto(move_to_x, move_to_y)
            

    def go_down(self,block):

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
        
        if (move_to_x, move_to_y) not in block:
            self.goto(move_to_x, move_to_y)
        
        
    def go_left(self,block):

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
        
        if (move_to_x, move_to_y) not in block :
            self.goto(move_to_x, move_to_y)
        
    def go_right(self,block):

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
        
        move_to_x = self.xcor()+24
        move_to_y = self.ycor()


        if (move_to_x, move_to_y) not in block:
            self.goto(move_to_x, move_to_y)
        
        self.shape(".\\art\\heroright.gif")

          
    def drink(self,info):
        
        if info.potion>0 and info.hp is not info.fullhp : 
            info.potion-=1
            info.show_healthpotion()

            if info.hp < info.fullhp-300:
                info.hp+=300
                info.show_health()
            else:
                info.hp=info.fullhp
                info.show_health()
        else:
            pass
            
    def fireball(self,proj2,info,bug):
        if info.fire_scroll>0:
            info.fire_scroll-=1
            info.show_fire_scroll()
            proj2.fire(self,bug)
            
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
