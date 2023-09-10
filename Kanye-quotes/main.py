# Import necessary modules
from tkinter import *
import requests
import json

# Function to get a Kanye West quote from the API and display it
def get_quote():
    # Define the API URL
    api_url = 'https://api.kanye.rest'
    
    # Send a GET request to the API
    response = requests.get(api_url)
    
    # Raise an exception if the request fails (e.g., due to network issues)
    response.raise_for_status()
    
    # Parse the JSON response into a Python dictionary
    data = response.json()
    
    # Extract the quote from the response data
    quote = data['quote']
    
    # Update the text displayed on the canvas with the fetched quote
    canvas.itemconfig(quote_text, text=quote)

# Create the main window
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50, bg='#F3FDE8')

# Create a canvas for displaying the background image and text
canvas = Canvas(width=300, height=410, bg='#A8DF8E')
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)

# Create a text element for displaying the quote
quote_text = canvas.create_text(150, 207, text='', width=250, font=("Arial", 15, "bold"), fill="white")
canvas.grid(row=0, column=0)

# Create a button with Kanye West's image that triggers the get_quote function when clicked
kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote, bg='#CEDEBD')
kanye_button.grid(row=1, column=0)

# Start the main event loop
window.mainloop()
