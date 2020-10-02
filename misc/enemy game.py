
from enemy import*
from info import*
from images import images
from keybinding import keybinding
from maps import*
from intro import*
from item import*
import turtle
import math
import random
import time
import winsound

for image in images:
    turtle.register_shape(image)

#intro screen
#------------------------------
intro()

#main screen 
#------------------------------

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("7 Dungeons Deep (7DD)")
wn.setup(1900,930)
wn.bgpic(".\\art\\background.gif")
wn.tracer(0)

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


        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        
        self.shape(".\\art\\heroright.gif")

          
    def drink(self):
        
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
            
    def fireball(self):
        if info.fire_scroll>0:
            info.fire_scroll-=1
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
                enemies.append(Enemy(screen_x, screen_y,player,walls))

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
                enemies.append(Enemy2(screen_x, screen_y,player,walls))


            if character =="N":
                npcs.append(Npc(screen_x, screen_y))

            if character =="Q":
                quests.append(Quest(screen_x, screen_y))

            if character =="B":
                quest_items.append(Quest_item(screen_x, screen_y))

            if character =="I":
                fake_walls.append(Fake_wall(screen_x, screen_y))

            if character =="J":
                enemies.append(Enemy3(screen_x, screen_y,player,walls))

            if character =="L":
                enemies.append(Enemy4(screen_x, screen_y,player,walls))

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

keybinding(player)

for enemy in enemies:
    turtle.ontimer(enemy.move(walls,player),t=250)

      

#bob=0

while True:
    
   # bob+=1
  #  while bob ==300:

      #  for enemy in enemies:
         #    turtle.ontimer(enemy.move(walls,player),t=100)
       # bob=0
        
    
    missile.move()
    missile2.move()

    for particle in particles:
        particle.move()
        
    for armour in armours:

        if player.is_collision(armour):

            armour.destroy()

            if armourupgrade==1:
                info.armourstats+=4
                game.armour=("Mythril Plate")
                game.show_armour()
                info.show_defense()
                armourupgrade+=1
                winsound.PlaySound(".\\sound\\armour.wav", winsound.SND_ASYNC)

            if armourupgrade==0:
                info.armourstats+=6
                game.armour=("Steel Plate")
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
                info.exp+=quest.exp
                info.show_exp()
                Quest.destroy(quest)


    for quest2 in quests2:

        if player.is_collision2(quest2):
            if info.boss ==0:
                game.start2()
            
            if info.boss ==1:
                game.end2()
                info.exp+=200
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
                info.weaponstats+=4
                game.weapon=("Mythril Sword")
                game.show_weapon()
                info.show_strength()
                weaponupgrade+=1
                winsound.PlaySound(".\\sound\\sword.wav", winsound.SND_ASYNC)

            if  weaponupgrade==0:
                info.weaponstats+=6
                game.weapon=("Steel Sword")
                game.show_weapon()
                info.show_strength()
                weaponupgrade+=1
                winsound.PlaySound(".\\sound\\sword.wav", winsound.SND_ASYNC)

    for firescroll in firescrolls:

        if player.is_collision(firescroll):

            firescroll.destroy()
            info.fire_scroll+=1
            info.show_fire_scroll()
            winsound.PlaySound(".\\sound\\scroll.wav", winsound.SND_ASYNC)


    for healing in healings:

        if player.is_collision(healing):

            healing.destroy()
            info.potion+=1
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
            enemy.hp -= (info.strength+info.weaponstats)
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
            info.exp += enemy.exp
            info.boss+=enemy.boss
            info.kill+=1
            info.show_exp()
            winsound.PlaySound(".\\sound\\orkdeath.wav", winsound.SND_ASYNC)

            if info.exp>70 and info.level2_claimed:
                info.hp=1100
                info.fullhp=1100
                info.strength=20
                info.defense=4
                info.level=2
                info.level2_claimed = False
                info.show_defense()
                info.show_health()
                info.show_strength()
                info.show_level()
                winsound.PlaySound(".\\sound\\levelup.wav", winsound.SND_ASYNC)
                time.sleep(1)
           

            if info.exp>150 and info.level3_claimed:
                info.hp=1200
                info.fullhp=1200
                info.strength=25
                info.defense=8
                info.level=3
                info.level3_claimed = False
                info.show_defense()
                info.show_health()
                info.show_strength()
                info.show_level()
                winsound.PlaySound(".\\sound\\levelup.wav", winsound.SND_ASYNC)
                time.sleep(1)
           
            if info.exp>300 and info.level4_claimed:
                info.hp=1300
                info.fullhp=1300
                info.strength=30
                info.defense=12
                info.level=4
                info.level4_claimed = False
                info.show_defense()
                info.show_health()
                info.show_strength()
                info.show_level()
                winsound.PlaySound(".\\sound\\levelup.wav", winsound.SND_ASYNC)
                time.sleep(1)
            

            if info.exp>450 and info.level5_claimed:
                info.hp=1500
                info.fullhp=1500
                info.strength=40
                info.defense=20
                info.level=5
                info.level5_claimed = False
                info.show_defense()
                info.show_health()
                info.show_strength()
                info.show_level()
                winsound.PlaySound(".\\sound\\levelup.wav", winsound.SND_ASYNC)
                time.sleep(1)

            if info.exp>700 and info.level6_claimed:
                info.hp=1700
                info.fullhp=1700
                info.strength=60
                info.defense=25
                info.level=6
                info.level6_claimed = False
                info.show_defense()
                info.show_health()
                info.show_strength()
                info.show_level()
                winsound.PlaySound(".\\sound\\levelup.wav", winsound.SND_ASYNC)
                time.sleep(1)

            if info.exp>950 and info.level7_claimed:
                info.hp=2000
                info.fullhp=2000
                info.strength=80
                info.defense=30
                info.level=7
                info.level7_claimed = False
                info.show_defense()
                info.show_health()
                info.show_strength()
                info.show_level()
                winsound.PlaySound(".\\sound\\levelup.wav", winsound.SND_ASYNC) 
                time.sleep(1)

            if info.exp>1400 and info.level8_claimed:
                info.hp=2200
                info.fullhp=2200
                info.strength=100
                info.defense=50
                info.level=8
                info.level8_claimed = False
                info.show_defense()
                info.show_health()
                info.show_strength()
                info.show_level()
                winsound.PlaySound(".\\sound\\levelup.wav", winsound.SND_ASYNC) 
                time.sleep(1)
    
    for coin in coins:
        if player.is_collision(coin):
            game.gold += coin.gold
            game.show_gold()
            #print("Player Gold: {}".format (game.gold))
            coin.destroy()
            coins.remove(coin)
            winsound.PlaySound(".\\sound\\coin.wav", winsound.SND_ASYNC)

    for enemy in enemies:
        if player.is_collision(enemy):
            attack=enemy.damage
            reduce_damage=attack-(info.defense+game.armourstats)
            if reduce_damage <0 :
                reduce_damage=0

            info.hp-=reduce_damage
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
                turtle.ontimer(enemy.move(walls,player),t=250)
    
    if info.hp<=0:
        game.dead()
        player.destroy()
        winsound.PlaySound(".\\sound\\death.wav", winsound.SND_ASYNC)
        time.sleep(2)
        info.show_health()
        break
       
    wn.update()
