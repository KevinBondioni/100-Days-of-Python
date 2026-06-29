import random
from turtle import Turtle,Screen
import turtle as t

screen=Screen()
t.colormode(255)

color_list=[
    (198, 13, 32), (248, 236, 25), (40, 76, 188), (39, 216, 69),
    (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15),
    (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120),
    (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62)
    ]

tim=Turtle()
tim.speed("fastest")
tim.hideturtle()

def draw(points):
    for _ in range (points):
        color=random.choice(color_list)
        tim.dot(20,color)
        tim.forward(50)

start_x = -250
start_y = -250
tim.penup()
tim.goto(start_x,start_y)
for riga in range(1,11):
    draw(10)
    new_y= start_y + (riga*50)
    tim.goto(start_x,new_y)



















screen.exitonclick()



