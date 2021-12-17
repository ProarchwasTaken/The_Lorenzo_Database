import time
import json

#This script is responsible for loading and displaying Entry Logs

while True:
    print('\n' * 150)
    time.sleep(0.5)
    
    # Prompts the user to enter the ID of the Log they wish to read
    id = input('Enter the ID of the Entry Log you wish to read: ')

    idJson = id + ".json"
    print('\n' * 150)

    # Opens requested .json file for reading
    file = open('logs/' + idJson, 'r')
    entry = json.load(file)
    
    #This displays what information is on the .json
    print(" Name: ",entry['name'], '\n' * 2, "Type: ",entry['type'], '\n'* 2, "Description: ",entry['desc'])
    
    time.sleep(1)

    # Asks the user if they wanna load another entry log.
    command = input("\nPress 'y' then enter if you wanna load another entry log: ")
    print(command)
    
    time.sleep(0.5)

    #Scrip loops when command is 'y'. The loop ends if anything other than y is entered.
    if command != "y":
        break
    else:
        pass

