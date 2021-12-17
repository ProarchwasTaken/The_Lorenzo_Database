import time
import os

time.sleep(1)

# Changes the terminal's color to green.
os.system("color A")

while True:

    # Clears the screen when the loop restarts
    print('\n' * 150)
    time.sleep(0.5)

    # Splash text including, title, credits, and list of useable commands.
    print('''
    ┌───────────────────────────────────────────────────────────────────────────┐
    │░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│
    │░░░░░░░╔════╦╗░░░░░╔╗░░░░░░░░░░░░░░░░░░░░░╔═══╗░░╔╗░░░╔╗░░░░░░░░░░░░░░░░░░░│
    │░░░░░░░║╔╗╔╗║║░░░░░║║░░░░░░░░░░░░░░░░░░░░░╚╗╔╗║░╔╝╚╗░░║║░░░░░░░░░░░░░░░░░░░│
    │░░░░░░░╚╝║║╚╣╚═╦══╗║║░░╔══╦═╦══╦═╗╔═══╦══╗░║║║╠═╩╗╔╬══╣╚═╦══╦══╦══╗░░░░░░░░│
    │░░░░░░░░░║║░║╔╗║║═╣║║░╔╣╔╗║╔╣║═╣╔╗╬══║║╔╗║░║║║║╔╗║║║╔╗║╔╗║╔╗║══╣║═╣░░░░░░░░│
    │░░░░░░░░░║║░║║║║║═╣║╚═╝║╚╝║║║║═╣║║║║══╣╚╝║╔╝╚╝║╔╗║╚╣╔╗║╚╝║╔╗╠══║║═╣░░░░░░░░│
    │░░░░░░░░░╚╝░╚╝╚╩══╝╚═══╩══╩╝╚══╩╝╚╩═══╩══╝╚═══╩╝╚╩═╩╝╚╩══╩╝╚╩══╩══╝░░░░░░░░│
    │░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│
    └───────────────────────────────────────────────────────────────────────────┘
    Public Oldschool Database by: Tyler Dillard

    ╔══════════════════╗
    ║     COMMANDS     ║
    ╚══════════════════╝
    save - Write and save a new entry log into the Database.
    load - Load an existing entry log to read.
    list - Lists all entries avalible in the Database
    exit - Closes the program
    
    ''')

    # Program asks the user to type a valid command.
    command = input('Please enter a COMMAND. (Warning: it is case sensitive.): ')
    print(command)

    time.sleep(0.5)

    # Closes the program if the command is exit
    if command == "exit":
        break
    
    # Loads the save python file if the command is save
    if command == "save":
        try:
            os.system("python sub\save.py")
        except:
            pass
    
    # Loads the load.py python file if the command is load
    if command == "load":
        try:
            os.system("python sub\load.py")
        except:
            pass
    
    # Loads the list.py python file if the command is list
    if command == "list":
        try:
            os.system("python sub\list.py")
        except:
            pass