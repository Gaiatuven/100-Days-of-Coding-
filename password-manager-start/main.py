from tkinter import *
from random import choice, shuffle
from tkinter import messagebox
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for i in range(8, 10)]
    password_symbols = [choice(symbols) for i in range(2, 4)]
    password_numbers = [choice(numbers) for i in range(2, 4)]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Fields can't be empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():
    website_name = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Data file Found.")
    else:
        if website_name in data:
            email = data[website_name]['email']
            password = data[website_name]['password']
            messagebox.showinfo(title=website_name, message=f"Email: {email})\nPassword: {password}")



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=250, height=200)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0)

#Lables
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

#Entries
website_entry = Entry(width=32)
website_entry.grid(column=1, row=1, columnspan=1)
email_entry = Entry(width=43)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "gaia@gmail.com")
password_entry =Entry(width=32)
password_entry.grid(column=1, row=3)

#Button
generate_button = Button(text="Generate", command=generate_password)
add_button = Button(text="Add", width=41, command=save)
search_button = Button(text="Search", width=8, command=find_password)

generate_button.grid(column=2, row=3)
add_button.grid(column=1, row=4, columnspan=2)
search_button.grid(column=2, row=1)




window.mainloop()