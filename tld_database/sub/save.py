import time
import json
from datetime import date

#This script is used to create and save an entry log to logs.json


# Loads up the json containing the old entry logs
oldLogs = open('logs.json', 'r')

# Sets logs's value to the json with the old entry logs
logs = json.load(oldLogs)

print('\n' * 150)
time.sleep(0.5)

# Prompts the user to enter the information for the log. Info will be saved as a dictionary to newLog.
newLog = {
"name": input('What will be the name of this Entry to the Database?: '),
"author": input('Who is the Author(s) of this Log?: '),
"type": input('What type of Entry Log is this? (examples: Human, Locations, Food, Journal Entry): '),
"desc": input('Please type the description of this Entry Log: '),
"date": time.strftime("%d/%m/%Y")
}

# Temporarily adds newLog without the dictionary to get the list ID to display for the user to use to load up their log for reading
logs.append('newLog')
time.sleep(0.5)
print('\n' * 2, "<ENTRY ADDED TO THE DATABASE> Your new logs ID is: ", logs.index('newLog'))
logs.remove('newLog')

# Fully add newLog with dictionary to the list
logs.append(newLog.copy())

file = open('logs.json', 'w+')

#Logs updates logs.json with indentation.
json.dump(logs, file, indent=4)

time.sleep(1)
print('\n' * 2)
input("Press ENTER to continue: ")