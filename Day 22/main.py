from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle=Paddle(350)
l_paddle=Paddle(-350)
ball=Ball()
scoreboard=Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.move_up,"Up")
screen.onkeypress(r_paddle.move_down, "Down")
screen.onkeypress(l_paddle.move_up,"w")
screen.onkeypress(l_paddle.move_down, "s")
t_sleep= 0.001

game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collision with the y edge of the screen
    if ball.ycor()== 290 or ball.ycor() == -290:
        ball.y_bounce()

    #detected collision with the palle
    if ball.distance(r_paddle) < 60 and ball.xcor() == 330 or ball.distance(l_paddle) < 60 and ball.xcor() == -330:
        ball.x_bounce()

    #detect if the right paddle miss the ball
    if ball.xcor() >= 400:
        ball.reset_position()
        scoreboard.l_point()


    # detect if the left paddle miss the ball
    if ball.xcor() == -400:
        ball.reset_position()
        scoreboard.r_point()




game_is_on= True


screen.exitonclick()

