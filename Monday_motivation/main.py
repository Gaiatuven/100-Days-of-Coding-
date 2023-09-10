import smtplib
import datetime as dt
import random

my_email = "ggwiese@gmail.com"
password = "wkxduspufvyxijbo"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 3:
    with open('data.txt') as file:
        all_quotes = file.readlines()
        random_quote = random.choice(all_quotes)
    
   
connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(my_email, password=password)
connection.sendmail(
    from_addr=my_email, 
    to_addrs="gaiatuven@gmail.com", 
    msg="Subject:Happy Birtday\n\nI hope you doing well")
connection.close()