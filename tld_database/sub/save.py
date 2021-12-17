import time
import json

#This script is used for creating and saving your own entry logs.

while True:
    print('\n' * 150)
    time.sleep(0.5)
    
    # Prompts the user to enter the informantion for the log. Said info will be saved in a json file for later use.
    log = {
    "name": input('Type the log name: '),
    "type": input('Type the log type: '),
    "desc": input('Type the log description: ')
    }

    #Prompts the user to type the ID for the log which will be used for the name of the json file.
    id = input("Type the log's ID Number: ")

    idJson = id + ".json"

    # Creates or Opens a .json file.
    file = open('logs/' + idJson, 'w+')

    # Saves previously enterd entry log info onto the .json
    json.dump(log, file)

    time.sleep(1)

    # Asks the user if they wanna make another entry log.
    command = input("\nPress 'y' then enter if you wanna write another entry: ")
    print(command)
    
    time.sleep(0.5)

    #Scrip loops when command is 'y'. The loop ends if anything other than y is entered.
    if command != "y":
        break
    else:
        pass