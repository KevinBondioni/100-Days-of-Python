from random import choice,randint
from turtle import Turtle, Screen
import turtle as t



t.colormode(255)
tim=Turtle()
tim.shape("turtle")
tim.hideturtle()
tim.speed("fast")
tim.width(10)

def random_color():
    r =randint(0,255)
    g = randint(0, 255)
    b = randint(0, 255)
    color=(r,g,b)
    return color

#definisco le direzioni (nord, est, sud, ovest)
direction=[0,90,180,270]

def move():
    tim.pencolor(random_color())
    tim.seth(choice(direction)) #tim punta in una direzione casuale
    tim.forward(30) #tim avanza

for _ in range(100):
    move()

screen=Screen()
screen.exitonclick()


