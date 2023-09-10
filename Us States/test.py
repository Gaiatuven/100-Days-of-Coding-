import turtle
import pandas as pd
import tkinter as tk
from tkinter import simpledialog, messagebox

# Initialize the turtle screen
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

# Create a turtle object for drawing
t = turtle.Turtle()
t.penup()
t.hideturtle()

# Load state data from CSV
csv_file = './50_states.csv'
state_data = pd.read_csv(csv_file)

# Create a list of all states and guessed states
all_states = state_data.state.to_list()
guessed_states = []

# Function to update the map with guessed states
def update_map():
    t.clear()
    for state in guessed_states:
        state_info = state_data[state_data['state'] == state]
        x = int(state_info.x)
        y = int(state_info.y)
        t.goto(x, y)
        t.write(state, align="center", font=("Arial", 8, "normal"))

# Main game loop
while len(guessed_states) < 50:
    answer_state = simpledialog.askstring(f"{len(guessed_states)}/50 States Correct", "Enter a state name:")

    if answer_state is None:
        break  # Exit the loop if the user cancels the input box

    answer_state = answer_state.title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        if missing_states:
            new_data = pd.DataFrame({'state': missing_states})
            new_data.to_csv("state_to_learn.csv", index=False)
        messagebox.showinfo("Game Over", "You have finished the game.")
        break

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        update_map()

# Close the turtle graphics window when done
turtle.bye()

# Create a tkinter root window
root = tk.Tk()
root.title("U.S. States Game")

# Create a label to display game completion message
completion_label = tk.Label(root, text="Congratulations! You have guessed all 50 states!", font=("Arial", 12))
completion_label.pack(pady=20)

# Start the tkinter main loop
root.mainloop()
