
import turtle 




def keybinding(self):

    turtle.listen()
    turtle.onkey(self.go_left, "Left")
    turtle.onkey(self.go_right, "Right")
    turtle.onkey(self.go_up, "Up")
    turtle.onkey(self.go_down, "Down")
    turtle.onkey(self.headright, "d")
    turtle.onkey(self.headleft, "a")
    turtle.onkey(self.headdown,"s")
    turtle.onkey(self.headup,"w")
    turtle.onkey(self.headright, "D")
    turtle.onkey(self.headleft, "A")
    turtle.onkey(self.headdown,"S")
    turtle.onkey(self.headup,"W")
    turtle.onkey(self.drink,"space")
    turtle.onkey(self.fireball,"z")
    turtle.onkey(self.fireball,"Z")
