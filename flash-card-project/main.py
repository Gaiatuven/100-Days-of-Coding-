import tkinter as tk
from PIL import Image, ImageTk 
from tkinter import PhotoImage
import csv
import random
import pandas as pd

# Constants
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
words_to_learn = {}

try:
    data = pd.read_csv('data/french_words.csv')
except FileNotFoundError:
    # If the file is not found, read a default data file (you might want to handle this case more gracefully)
    original_data = pd.read_csv('data/french_words.csv')
    print(original_data)
    words_to_learn = original_data.to_dict(orient="records")
    words_to_learn = pd.to_dict(orient='records')
else:
    words_to_learn = data.to_dict(orient="records")

# Function to show the next flashcard
def next_card():
    global current_card, flip_timer 
    root.after_cancel(flip_timer)
    current_card = random.choice(words_to_learn)
    canvas.itemconfig(card_title, text='French', fill='Black')
    canvas.itemconfig(card_word, text=current_card['French'], fill='Black')
    canvas.itemconfig(card_background_image, image=card_front_image)
    flip_timer = root.after(3000, func=flip_card)

# Function to flip the flashcard
def flip_card():        
    canvas.itemconfig(card_title, text='English', fill="White")
    canvas.itemconfig(card_word, text=current_card['English'], fill="White") 
    canvas.itemconfig(card_background_image, image=card_back_image)

# Function to mark a word as known
def is_known():
    words_to_learn.remove(current_card)
    print(len(words_to_learn))
    data = pd.DataFrame(words_to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# Create the main application window
root = tk.Tk()
root.title("Flash-Card")
root.configure(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Initialize the flip timer
flip_timer = root.after(3000, func=flip_card)

# Create the canvas for displaying flashcards
canvas = tk.Canvas(root, width=800, height=526, bg=BACKGROUND_COLOR)
canvas.grid(column=0, row=0, sticky="nsew", columnspan=2)
card_front_image = PhotoImage(file='images/card_front.png')
card_back_image = PhotoImage(file='images/card_back.png')
card_background_image = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# Create buttons for "wrong" and "right" answers
wrong_button_img = Image.open("images/wrong.png")
wrong_button_img = ImageTk.PhotoImage(wrong_button_img)
wrong_button = tk.Button(root, image=wrong_button_img, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

right_button_img = Image.open("images/right.png")
right_button_img = ImageTk.PhotoImage(right_button_img)
right_button = tk.Button(root, image=right_button_img, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

# Display the initial random word
next_card()

# Start the Tkinter main event loop
root.mainloop()
