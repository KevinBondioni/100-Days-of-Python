import turtle
import pandas

data=pandas.read_csv("regioni_italia_coordinate.csv")
region=data["regioni"]

screen= turtle.Screen()
screen.title("Regioni d'italia")
image="Immagine 2026-06-21 211844.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)

new_state=turtle.Turtle()
new_state.hideturtle()
new_state.penup()

guessed_state=[]
missing_state=[]


while len(guessed_state) <20:
    user_choice = screen.textinput(title=f"{len(guessed_state)}/20 Regioni Corrette", prompt="Qual'è il nome di un altra regione?").title()
    if user_choice == "Exit":
        for state in region:
            if state not in guessed_state:
                missing_state.append(state)
        new_data=pandas.DataFrame(missing_state)
        new_data.to_csv("Regioni da studiare.csv")
        break

    for state_name in region:
        if state_name==user_choice:
            if user_choice not in guessed_state:
                date_line = data[data.regioni == user_choice]
                new_state.goto(date_line["x"].item(), date_line["y"].item())
                new_state.write(state_name, align="center", font=("Arial", 8, "normal"))
                screen.update()
                guessed_state.append(user_choice)
