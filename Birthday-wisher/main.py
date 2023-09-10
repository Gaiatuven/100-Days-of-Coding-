##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

# Import necessary libraries
import smtplib 
import datetime as dt  
import csv 
import random  
import os  

# Read the current date and time
current_date = dt.datetime.now()

# Define the folder path where letter templates are stored
folder_path = 'Birthday-wisher/letter_templates'

# List all the files in the letter templates folder
letter_files = os.listdir(folder_path)

# Randomly select a letter template to send
letter_to_send = random.choice(letter_files)

# Open and read the CSV file containing birthday data
with open('Birthday-wisher/birthdays.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # Iterate through each row in the CSV file
    for row in csv_reader:
        # Extract data from the CSV row
        name = row['name']
        email = row['email']
        birth_year = int(row['year'])
        birth_month = int(row['month'])
        birth_day = int(row['day'])

        # Create a datetime object for the birthday
        birthday = dt.datetime(birth_year, birth_month, birth_day)

        # Check if today's date matches the birthday
        if current_date.month == birthday.month and current_date.day == birthday.day:
           # Read the contents of the selected letter template
            with open(os.path.join(folder_path, letter_to_send), 'r') as letter:
                letter_contents = letter.read()

            # Replace [NAME] with the actual name
            letter_contents = letter_contents.replace('[NAME]', name)

            