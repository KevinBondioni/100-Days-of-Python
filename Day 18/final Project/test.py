import random
from turtle import Turtle, Screen
import turtle as t

screen = Screen()
t.colormode(255)

color_list = [
    (198, 13, 32), (248, 236, 25), (40, 76, 188), (39, 216, 69),
    (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15),
    (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120),
    (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62)
]

tim = Turtle()
tim.speed("fastest")
tim.hideturtle() # Nascondiamo la tartaruga per vedere solo il dipinto pulito
tim.penup() # La penna sta SEMPRE su, perché tim.dot() non ha bisogno della penna giù!

start_x = -250
start_y = -250

# Un unico ciclo pulito per gestire righe e colonne
for riga in range(10):
    tim.goto(start_x, start_y + (riga * 50))
    for colonna in range(10):
        color = random.choice(color_list)
        tim.dot(20, color)
        tim.forward(50)

screen.exitonclick()