#------------------------------------------#
# Title: IO Classes
# Desc: A Module for IO Classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
#------------------------------------------#

if __name__ == '__main__':
    raise Exception('This file is not meant to run by itself')

import DataClasses as DC
import ProcessingClasses as PC

class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    @staticmethod
    def save_inventory(file_name: list, lst_Inventory: list) -> None:
        """


        Args:
            file_name (list): list of file names [CD Inventory, Track Inventory] that hold the data.
            lst_Inventory (list): list of CD objects.

        Returns:
            None.

        """

        file_name_CD = file_name[0]
        file_name_trk = file_name[1]
        try:
            with open(file_name_CD, 'w') as file:
                for disc in lst_Inventory:
                    file.write(disc.get_record())
            with open(file_name_trk, 'w') as file:
                for disc in lst_Inventory:
                    tracks = disc.cd_tracks
                    disc_id = disc.cd_id
                    for trk in tracks:
                        if trk is not None:
                            record = '{},{}'.format(disc_id,trk.get_record())
                            file.write(record)
        except Exception as e:
            print('There was a general error!', e, e.__doc__, type(e), sep='\n')

    @staticmethod
    def load_inventory(file_name: list) -> list:
        """


        Args:
            file_name (list): list of file names [CD Inventory, Track Inventory] that hold the data.

        Returns:
            list: list of CD objects.

        """

        lst_Inventory = []
        file_name_CD = file_name[0]
        file_name_trk = file_name[1]
        try:
            with open(file_name_CD, 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    row = DC.CD(data[0], data[1], data[2])
                    lst_Inventory.append(row)
            with open(file_name_trk, 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    cd = PC.DataProcessor.select_cd(lst_Inventory, int(data[0]))
                    track = DC.Track(int(data[1]),data[2],data[3])
                    cd.add_track(track)
        except EOFError as e:
            print('NO DATA IN FILE!')
            print(e,e.__doc__)
        except IOError as e:
            print("No Inventory File!")
            print(e,e.__doc__,type(e))
        except Exception as e:
            print('There was a general error!', e, e.__doc__, type(e), sep='\n')
        return lst_Inventory

class ScreenIO:
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Main Menu\n\n[l] load Inventory from file\n[a] Add CD / Album\n[d] Display Current Inventory')
        print('[c] Choose CD / Album\n[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, d, c, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'd', 'c', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, d, c, s or x]: ').lower().strip()
            if choice not in ['l', 'a', 'd', 'c', 's', 'x']:
                print('Invalid input, try again!')
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def print_CD_menu():
        """Displays a sub menu of choices for CD / Album to the user

        Args:
            None.

        Returns:
            None.
        """

        print('CD Sub Menu\n\n[a] Add track\n[d] Display cd / Album details\n[r] Remove track\n[x] exit to Main Menu')
        print('[-] Remove CD\n')

    @staticmethod
    def menu_CD_choice():
        """Gets user input for CD sub menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices a, d, r or x

        """
        choice = ' '
        while choice not in ['a', 'd', 'r', 'x','-']:
            choice = input('Which operation would you like to perform? [a, d, r, -, or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def menu_CD_loop(lst):
        """This function is responsible for the logic that controls user flow through the CD sub menu.

        Args:
            lst: (list of CD objects) 

        Returns:
            None.

        """

        c = True
        while c:

            ScreenIO.show_inventory(lst)
            cd_idx = input('Select the CD / Album index: ')
            
            if cd_idx.upper().strip() == "BACK":
                break

            con = 0
            for cd in lst:
                if str(cd_idx) == str(cd.cd_id):
                    con += 1

            if con:
                cd = PC.DataProcessor.select_cd(lst, cd_idx)

            else:
                print("Can not find the CD! try again! enter 'BACK' to exit!")
                continue

            while True:
                ScreenIO.print_CD_menu()
                strCDchoice = ScreenIO.menu_CD_choice()

                if strCDchoice.lower().strip() == 'x':
                    c = False
                    break

                elif strCDchoice == 'a':
                    a = True

                    while a:
                        position = input('What is the number of the track in the album?: ')

                        if position.upper().strip() == 'BACK':
                            c = False
                            break

                        try: 
                            int(position)

                        except ValueError:
                            print("Track position must be a number! Try agin! Enter 'BACK' to exit!")
                            continue

                        except Exception as e:
                            print("Unexpected error! Try agin! Enter 'BACK' to exit!")
                            print(e,e.__doc__)
                            continue

                        title = input("What is the title of the track?: ")
                        if title.upper().strip() == 'BACK':
                            c = False
                            break

                        length = input("What is the length of the track?: ")
                        if position.upper().strip() == 'BACK':
                            c = False
                            break

                        position = int(position)
                        tpl = position,title,length
                        PC.DataProcessor.add_track(tpl,cd)
                        print(f'{cd.get_track(position)} added to {cd}')
                        break
                    continue

                elif strCDchoice == 'd':
                    print(DC.CD.get_long_record(cd))
                    continue

                elif strCDchoice == 'r':
                    cd.get_tracks()
                    ID = input('Enter the number of the track you would like removed: ')
                    cd.rmv_track(ID)
                    continue

                elif strCDchoice == '-':

                    try:
                        CD_to_delete = PC.DataProcessor.select_cd(lst,cd_idx)
                        confirm = input(f"'ype \'yes\' to continue and remove {CD_to_delete.__str__()} from file. Otherwise removal will be canceled: ")

                        if confirm == 'yes':

                            try:
                                PC.DataProcessor.delete_entry(cd_idx, lst)
                                print('CD was removed! Returning to main menu!')
                                c = False
                                break

                            except Exception as e:
                                print ('Error removing track')

                                if cd_idx.isnumeric():
                                    print(e,e.__doc__)

                                elif int(cd_idx) <= 0:
                                    print('CD_id must be positive!')

                                else:
                                    print('CD_id must be numeric and positive!')
                                    print(e,e.__doc__)

                        else:
                            print('Input not "yes", returning to menu.')
                            continue

                    except Exception as e:
                        print("Invalid input for CD to remove!")
                        print(e,e.__doc__)
                        continue

                else:
                    print('Invalid input, try again!')
                    continue

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print(row)
        print('======================================')

    @staticmethod
    def show_tracks(cd):
        """Displays the Tracks on a CD / Album

        Args:
            cd (CD): CD object.

        Returns:
            None.

        """
        print('====== Current CD / Album: ======')
        print(cd)
        print('=================================')
        print(cd.get_tracks())
        print('=================================')

    @staticmethod
    def get_CD_info():
        """function to request CD information from User to add CD to inventory


        Returns:
            cdId (string): Holds the ID of the CD dataset.
            cdTitle (string): Holds the title of the CD.
            cdArtist (string): Holds the artist of the CD.

        """

        cdId = input('Enter ID: ').strip()
        cdTitle = input('What is the CD\'s title? ').strip()
        cdArtist = input('What is the Artist\'s name? ').strip()
        return cdId, cdTitle, cdArtist

    @staticmethod
    def get_track_info():
        """function to request Track information from User to add Track to CD / Album


        Returns:
            trkId (string): Holds the ID of the Track dataset.
            trkTitle (string): Holds the title of the Track.
            trkLength (string): Holds the length (time) of the Track.

        """

        trkId = input('Enter Position on CD / Album: ').strip()
        trkTitle = input('What is the Track\'s title? ').strip()
        trkLength = input('What is the Track\'s length? ').strip()
        return trkId, trkTitle, trkLength

