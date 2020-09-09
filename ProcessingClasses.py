#------------------------------------------#
# Title: Processing Classes
# Desc: A Module for processing Classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
#------------------------------------------#

if __name__ == '__main__':
    raise Exception('This file is not meant to ran by itself')

import DataClasses as DC

class DataProcessor:
    """Processing the data in the application"""
    @staticmethod
    def add_CD(CDInfo, table):
        """function to add CD info in CDinfo to the inventory table.

        Args:
            CDInfo (tuple): Holds information (ID, CD Title, CD Artist) to be added to inventory.
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """

        cdId, title, artist = CDInfo
        try:
            cdId = int(cdId)
            row = DC.CD(cdId, title, artist)
            table.append(row)
        except:
            print('ID must be an Integer!')
            
    @staticmethod
    def delete_entry(ID, table):
        """Deletes an entry from memory.
                    Modifies table to remove selected entry.

        Args:
            table (list of CD objects): 2D data structure (list of objects) that holds the data during runtime
            ID (integer): numerical ID for CD entry
            
        Returns:
            None.
        """
        blnCDRemoved = False
        for row in table:
            print(row.cd_id)
            print(ID)
            if str(row.cd_id) == str(ID):
                table.remove(row)
                blnCDRemoved = True
                break
            
        if blnCDRemoved:
            print('The CD was removed')
            
        else:
            print('Could not find this CD!')

    @staticmethod
    def select_cd(table: list, cd_idx: int) -> DC.CD:
        """selects a CD object out of table that has the ID cd_idx

        Args:
            table (list): Inventory list of CD objects.
            cd_idx (int): id of CD object to return

        Raises:
            Exception: If id is not in list.

        Returns:
            row (DC.CD): CD object that matches cd_idx

        """
        try: cd_idx = int(cd_idx)
        except ValueError as e:
            print('ID is not an Integer!')
            print(e.__doc__)
        if int(cd_idx) <= 0:
            print ("CD ID must be positive!")
        try:
            lstIDs = []
            for CD in table:
                lstIDs.append(CD.cd_id)
        except Exception as e:
            print(e,e.__doc__)
        if cd_idx not in lstIDs:
            raise Exception('ID not in list!')
        try:
            for CD in table:
                if cd_idx == CD.cd_id:
                    return CD
        except Exception as e:
            print(e,e.__doc__)


    @staticmethod
    def add_track(track_info: tuple, cd: DC.CD) -> None:
        """adds a Track object with attributes in track_info to cd


        Args:
            track_info (tuple): Tuple containing track info (position, title, Length).
            cd (DC.CD): cd object the tarck gets added to.

        Raises:
            Exception: DESCraised in case position is not an integer.

        Returns:
            None: DESCRIPTION.

        """
        pos = track_info[0]
        if type(pos) != type(0):
            raise Exception ('position must be an integer!')
        tite = track_info[1]
        leng = track_info[2]
        track = DC.Track(pos,tite,leng)
        cd.add_track(track)


