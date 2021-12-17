from os import name
import time
import json

# This script is used to list all avalible entry logs that can be loaded

print('\n' * 150)
time.sleep(0.5)
print("Here is a list of how many entry logs are avalible to load. (Scroll up if list goes off screen)")
time.sleep(2)

print('\nID]══[NAME]════════════════════════[DATE]═════════════════════════')

# Gathers every logs in logs.json and prints them into a list.

file = open('logs.json', 'r')
list = json.load(file)

for i in list:
    print(list.index(i), ' - ', i['name'], '       -       ', i['date'])
    time.sleep(0.2)
print("══════════════════════════════════════════════════════════════════")


print("\nPlease note that you only need the number, not the name to load a entry log.")

time.sleep(0.5)
input("\nPress ENTER to continue: ")