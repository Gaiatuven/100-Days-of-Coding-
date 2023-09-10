import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

csv_file = './50_states.csv'
state = pd.read_csv(csv_file)
all_states = state.state.to_list()
guess_states = []

while len(guess_states) < 50:
    answer_state = screen.textinput(title=f"{len(guess_states)}/50 States Correct", prompt="Enter a state name: ").title()

    if answer_state is None:
        break  # Exit the loop if the user cancels the input box

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guess_states:
                missing_states.append(state)
        new_data = pd.DataFrame({'state': missing_states})
        new_data.to_csv("state_to_learn.csv")
        break

    if answer_state in all_states:
        guess_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = state[state['state'] == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)



turtle.mainloop()


