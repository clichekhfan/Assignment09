#------------------------------------------#
# Title: Data Classes
# Desc: A Module for Data Classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Modified to add Track class, added methods to CD class to handle tracks
#------------------------------------------#

if __name__ == '__main__':
    raise Exception('This file is not meant to run by itself')

class Track():
    """Stores Data about a single Track:

    properties:
        position: (int) with Track position on CD / Album
        title: (str) with Track title
        length: (str) with length / playtime of Track
    methods:
        get_record() -> (str)

    """
    #fields#
    
    __numtracks = 0
    
    
    #contructor#
    
    def __init__(self, p, t, l):
        
        #atributes#
        try:
            self.position = p
            self.title = t
            self.length = l
            Track.incrementer()
        except Exception as e:
            try:
                print('Error setting initial values ({self.position},{self.title},{self.length}) or incrementing _numtracks! ({self._numtracks})')
                print(e,e.__doc__)
            except:
                print('Error setting initial values or incrementing _numtracks!')
                print(e,e.__doc__)
        
        
    #properties#
    
    #Track position
    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, value):
        if type(value) != type(0):
            raise Exception('The position must be an integer!')
        elif value < 0:
            raise Exception(f'position must be positive! not {value}!')
        else:
            self.__position = value
    
    #track title
    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, value):
        if type(value) != type('blah'):
            raise Exception('The title must be a string!')
        else:
            self.__title = value
    
    #track length
    @property
    def length(self):
        return self.__length
    
    @length.setter
    def length(self, value):
        if type(value) != type('blah'):
            raise Exception('The length must be a string!')
        elif ':' not in str(value):
            raise Exception('The length must contain colon! ":"')
        elif not value.split(':')[0].isnumeric() and value.split(':')[1].isnumeric():
            raise Exception('The length must be numeric!')
        else:
            self.__length = value
            
            
    #methods#
    
    def _atributestrings(self):
        return f'{self.position:>2}. {self.title} ({self.length})'
    
    def __str__(self):
        return self._atributestrings()
   
    def get_record(self) -> str:
        return f'{self.position},{self.title},{self.length}\n'
    
    @staticmethod
    def tracks():
        return f"there are {Track.__numtracks} track(s)"
    
    @staticmethod
    def incrementer():
        Track.__numtracks += 1

class CD:
    """Stores data about a CD / Album:

    properties:
        cd_id: (int) with CD  / Album ID
        cd_title: (string) with the title of the CD / Album
        cd_artist: (string) with the artist of the CD / Album
        cd_tracks: (list) with track objects of the CD / Album
    methods:
        get_record() -> (str)
        add_track(track) -> None
        rmv_track(int) -> None
        get_tracks() -> (str)
        get_long_record() -> (str)

    """
    # -- Constructor -- #
    def __init__(self, cd_id: int, cd_title: str, cd_artist: str) -> None:
        """Set ID, Title and Artist of a new CD Object"""
        #    -- Attributes  -- #
        try:
            self.__cd_id = int(cd_id)
            self.__cd_title = str(cd_title)
            self.__cd_artist = str(cd_artist)
            self.__tracks = []
        except Exception as e:
            raise Exception('Error setting initial values:\n' + str(e))

    # -- Properties -- #
    # CD ID
    @property
    def cd_id(self):
        return self.__cd_id

    @cd_id.setter
    def cd_id(self, value):
        try:
            self.__cd_id = int(value)
        except Exception:
            raise Exception('ID needs to be Integer')

    # CD title
    @property
    def cd_title(self):
        return self.__cd_title

    @cd_title.setter
    def cd_title(self, value):
        try:
            self.__cd_title = str(value)
        except Exception:
            raise Exception('Title needs to be String!')

    # CD artist
    @property
    def cd_artist(self):
        return self.__cd_artist

    @cd_artist.setter
    def cd_artist(self, value):
        try:
            self.__cd_artist = str(value)
        except Exception:
            raise Exception('Artist needs to be String!')

    # CD tracks
    @property
    def cd_tracks(self):
        return self.__tracks

    # -- Methods -- #
    def __str__(self):
        """Returns: CD details as formatted string"""
        return f'{self.cd_id:>2}\t{self.cd_title} (by: {self.cd_artist})'
    
    def get_record(self):
        """Returns: CD record formatted for saving to file"""
        return f'{self.cd_id},{self.cd_title},{self.cd_artist}\n'

    def add_track(self, track: Track) -> None:
        """Adds a track to the CD / Album


        Args:
            track (Track): Track object to be added to CD / Album.

        Returns:
            None.

        """
        self.__sort_tracks()
        self.__tracks.append(track)

    def rmv_track(self, track_id: int) -> None:
        """Removes the track identified by track_id from Album


        Args:
            track_id (int): ID of track to be removed.

        Returns:
            None.

        """
        try:
            self.__tracks.pop(track_id-1)
        except Exception as e:
            print ('Error removing track')
            if track_id.isnumeric():
                print(e,e.__doc__)
            elif int(track_id) <= 0:
                print('track_id must be positive!')
                
            else:
                print('track_id must be numeric and positive!')
                print(e,e.__doc__)
        self.__sort_tracks()

    def __sort_tracks(self):
        """Sorts the tracks using Track.position. Fills blanks with None"""
        n = len(self.__tracks)
        for track in self.__tracks:
            if (track is not None) and (n < track.position):
                n = track.position
        tmp_tracks = [None] * n
        for track in self.__tracks:
            if track is not None:
                tmp_tracks[track.position - 1] = track
        self.__tracks = tmp_tracks

    def get_tracks(self) -> str:
        """Returns a string list of the tracks saved for the Album

        Raises:
            Exception: If no tracks are saved with album.

        Returns:
            result (string): formatted string of tracks.

        """
        self.__sort_tracks()
        if len(self.__tracks) < 1:
            raise Exception('No tracks saved for this Album')
        result = ''
        for track in self.__tracks:
            if track is None:
                result += 'No Information for this track\n'
            else:
                result += str(track) + '\n'
        return result

    def get_track(self,ID) -> str:
        """Returns a string of the track saved for the Album

        Args:
            ID: (integer) the position of a track on the CD.

        Raises:
            Exception: If no tracks are saved with album.

        Returns:
            result (string):formatted string of track.

        """
        value = ''
        for track in self.__tracks:
            if track == None:
                pass
            elif ID == track.position:
                value += track.__str__()
        return value

    def get_long_record(self) -> str:
        """gets a formatted long record of the Album: Album information plus track details

        Returns:
            result (string): Formatted information about ablum and its tracks.

        """
        result = self.get_record() + '\n'
        result += self.get_tracks() + '\n'
        return result



