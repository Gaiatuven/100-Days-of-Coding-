import pandas as pd

data = pd.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
information = data["Primary Fur Color"].value_counts()
print(information)
with open('info.txt', 'w') as f:
    f.write(information.to_string())
