import random
from random import choice
from turtle import Turtle, Screen
from colori import shape_colors

tim=Turtle()
tim.shape("turtle")
tim.hideturtle()
tim.speed("fast")
tim.width(10)

#definisco i movimenti
def t_right():
    tim.right(90), tim.forward(25)
def t_left():
    tim.left(90), tim.forward(25)
def ahead():
    tim.forward(25)
def back():
    tim.back(25)

def move():
    movement = [t_right,t_left,ahead,back]
    scelta_casuale= random.choice(movement)
    scelta_casuale()

for _ in range(200):
    move()
    tim.pencolor(choice(shape_colors))

screen=Screen()
screen.exitonclick()

