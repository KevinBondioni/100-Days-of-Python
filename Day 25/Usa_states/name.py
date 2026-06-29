from turtle import Turtle

class State(Turtle):
    def __init__(self, x, y, name):
        super().__init__()
        self.penup()
        self.hideturtle()

def new_state(self,name, x, y):
    self.write(name, align="center", font=("Arial", 8, "normal"))
    self.goto(x, y)