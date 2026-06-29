import turtle as t
from random import randint

t.colormode(255)
tim=t.Turtle()
tim.speed("fastest")


def random_colour():
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)
    color=r,g,b
    return color
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.pencolor(random_colour())
        tim.seth(tim.heading()+ size_of_gap)
        tim.circle(50)

draw_spirograph(5)


screen=t.Screen()
screen.exitonclick()