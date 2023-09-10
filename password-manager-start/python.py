import json

def find_password(service_name):
    with open("/home/greg/Documents/Udemy - Course/100 Days of Coding/password-manager-start/data.json", "r") as data_file:
        data = json.load(data_file)

        # Check if the service_name exists in the JSON data
        if service_name in data:
            entry = data[service_name]
            print(entry)
        

# Usage example:
search_name= "Facebook"
answer = find_password(search_name)
