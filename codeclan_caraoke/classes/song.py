class Song:
    def __init__(self, name_of_new_song):
        self.name = name_of_new_song
        self.list_of_lists_songs = [self.rock_songs, self.pop_songs, self.opera_songs]
        self.rock_songs_list = []
        self.pop_songs_list = []
        self.opera_songs_list = []

    def intro_rock_song(self, new_song):
        self.rock_songs_list += new_song
    
    def intro_pop_song(self, new_song):
        self.pop_songs_list += new_song

    def intro_opera_song(self, new_song):
        self.opera_songs_list += new_song
    
    def play_song(self, favourite):
        for favourite in self.list_of_songs:
            for song in favourite:
                print("Whohoo!")

    def add_rock_list_to_all_songs_list(self):
        self.list_of_lists_of_songs += self.rock_songs_list


    def add_pop_list_to_all_songs_list(self):
        self.list_of_lists_of_songs += self.pop_songs_list
    

    def add_opera_list_to_all_songs_list(self):
        self.list_of_lists_of_songs += self.opera_songs_list