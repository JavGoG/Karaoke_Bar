import unittest
from classes.song import Song
import pdb

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song1 = Song("Highway to Hell", "Rock") 
        # self.rock_songs_list = []     

    def test_song_go_to_different_list(self):
        # pdb.set_trace()
        self.song1.song_go_to_different_list("Highway to Hell", "Rock")
        print(self.song1.rock_songs_list)
        self.assertEqual(True, "Highway to Hell" in self.song1.rock_songs_list)

    def test_play_song(self):
        self.song1.song_go_to_different_list("Highway to Hell", "Rock")
        self.song1.play_song("Highway to Hell")
        self.assertEqual(True, "Highway to Hell" in self.song1.rock_songs_list)
