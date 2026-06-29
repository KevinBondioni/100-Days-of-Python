import turtle
import pandas

data=pandas.read_csv("50_states.csv")
states=data["state"]

screen= turtle.Screen()
screen.title("U.S. States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)

new_state=turtle.Turtle()
new_state.hideturtle()
new_state.penup()

guessed_state=[]
#missing_state=[]

while len(guessed_state) <50:
    user_choice = screen.textinput(title=f"{len(guessed_state)}/50 States Correct", prompt="What's another state's name?").title()
    if user_choice == "Exit":
        missing_state=[state for state in states if state not in guessed_state]
        new_data=pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break

    for state_name in states:
        if state_name==user_choice:
            if user_choice not in guessed_state:
                date_line = data[data.state == user_choice]
                new_state.goto(date_line["x"].item(), date_line["y"].item())
                new_state.write(state_name, align="center", font=("Arial", 8, "normal"))
                screen.update()
                guessed_state.append(user_choice)
