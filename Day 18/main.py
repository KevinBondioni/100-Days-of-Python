import random
from turtle import Turtle, Screen

tim=Turtle()
tim.shape("turtle")
tim.color("SpringGreen4")

def draw_shape(num_sides):
    for _ in range(num_sides):
        tim.forward(100)
        tim.right((360/num_sides))

shape_colors = [
    "red",
    "crimson",
    "deepPink",
    "indianRed",
    "blue",
    "deepSkyBlue",
    "navy",
    "royalBlue",
    "green",
    "forestGreen",
    "lime",
    "seaGreen",
    "gold",
    "orange",
    "darkOrange",
    "yellow",
    "purple",
    "magenta",
    "chocolate",
    "slateGray",
]

for _ in range(3,11):
    tim.pencolor(random.choice(shape_colors))
    draw_shape(_)







screen=Screen()
screen.exitonclick()