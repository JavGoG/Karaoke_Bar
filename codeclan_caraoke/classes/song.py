class Song:
    def __init__(self, name_of_new_song):
        self.name = name_of_new_song
        self.list_of_songs = [self.rock_songs, self.pop_songs, self.opera_songs]
        self.rock_songs = ["A_rock", "B_rock", "C_rock"]
        self.pop_songs = [" pop_1", "pop_2, pop_3"]
        self.opera_songs = ["opera_1", "opera_2", "opera_3"]

    def intro_song(self, name_new_song, room_for_new_song):
        self.name = name_new_song
        self.room = room_for_new_song
        
    