import unittest
from classes.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song1 = Song("Highway to Hell")

    def intro_rock_song_list_test(self):
        self.assertEqual(True,"Highway to hell" in  self.song1.rock_songs_list)
        