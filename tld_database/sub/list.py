import time
import os.path
from glob import glob

#This script is used to list all avalible entry logs that can be loaded

print('\n' * 150)
time.sleep(0.5)
print("Here is a list of how many entry logs are avalible to load. (Scroll up if list goes off screen)")
time.sleep(2)

print('\n══════════════════════════════════════════════════════════════════')

#Gathers every .json in 'logs/' and prints them into a list.
pattern = os.path.join('logs/', '*.json')
for logs in glob(pattern):
    print(logs.replace('.json', ''))
    time.sleep(0.2)

print("\nPlease note that you only need the number, not the 'logs/' to load a entry log.")

time.sleep(0.5)
input("\nPress ENTER to continue: ")