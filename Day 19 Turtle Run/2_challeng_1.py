from turtle import Turtle, Screen

tim=Turtle()
screen=Screen()

def forwards(): #W
    tim.forward(10)
def backwards(): #S
    tim.backward(10)
def counter_clockwise(): #A
    tim.right(10)
def clockwise(): #D
    tim.left(10)
def clear_drawing(): #C
    tim.reset()

screen.listen()
screen.onkey(fun=forwards,key="w")
screen.onkey(fun=backwards,key="s")
screen.onkey(fun=counter_clockwise,key="a")
screen.onkey(fun=clockwise,key="d")
screen.onkey(fun=clear_drawing,key="c")

screen.exitonclick()