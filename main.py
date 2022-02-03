import turtle
from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("Identify Indian Sates")
image = "India_map_1.gif"
screen.addshape(image)
screen.setup(height=700, width=600)
turtle.shape(image)

data = pandas.read_csv("India.csv")
all_states = data.State.tolist()
identified_states = []

while len(identified_states) < 35:
    user_input = screen.textinput(title=f"{len(identified_states)}/35 Guessed States",
                                  prompt="Enter the name of the state").title()
    if user_input == "Exit":
        missing_states = []
        for state in all_states:
            if state not in identified_states:
                missing_states.append(state)
        missing_data = pandas.DataFrame(missing_states)
        missing_data.to_csv("Missing state data.csv")
        print(missing_data)
        break
    if user_input in all_states:
        identified_states.append(user_input)
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_name = data[data.State == user_input]
        t.goto(int(state_name.X), int(state_name.Y))
        t.write(state_name.State.item())






