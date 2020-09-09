#------------------------------------------#
# Title: CD_Inventory.py
# Desc: The CD Inventory App main Module
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
# AHanson, 2020-Sep-03, expanded track class
# AHanson, 2020-Sep-03, expanded CD class
# AHanson, 2020-Sep-06, expanded error catching

#------------------------------------------#

import ProcessingClasses as PC #contains functions to proccess data
import IOClasses as IO #contains functions to process IO

lstFileNames = ['AlbumInventory.txt', 'TrackInventory.txt']
lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames) #loads inventory from file before user interaction

while True:
    IO.ScreenIO.print_menu() #this displays the menu to the user
    strChoice = IO.ScreenIO.menu_choice() #this captures user input

    #this choice exits the user from the program, asks for confimation
    if strChoice == 'x':
        print('Please do not forget to save your data!')
        confirm = input('Type "yes" to continue and exit the program. Otherwise exit will be canceled: ')

        if confirm == 'yes':
            break

        else:
            print ('Input not "yes", returning to main menu!')
            continue

    #this choice reloads the inventory, warning and confirmation present
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('Type \'yes\' to continue and reload from file. Otherwise reload will be canceled: ')

        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)
            IO.ScreenIO.show_inventory(lstOfCDObjects)

        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.

    #this choice allows adding a CD to the inventory system
    elif strChoice == 'a':
        tplCdInfo = IO.ScreenIO.get_CD_info()
        PC.DataProcessor.add_CD(tplCdInfo, lstOfCDObjects)
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.

    #this choice displays the current in memory inventory to the user
    elif strChoice == 'd':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.

    #this choice opens a sub menu for interacting with a specific CD object
    elif strChoice == 'c':
        IO.ScreenIO.menu_CD_loop(lstOfCDObjects) #this function is complicated
        continue # start loop back at top.

    #this choice allows manual saving of the inventory in memory to the inventory file
    elif strChoice == 's':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()

        if strYesNo == 'y':
            IO.FileIO.save_inventory(lstFileNames, lstOfCDObjects)

        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.

    #catch-all, should not be possible
    else:
        print('General menu Error')