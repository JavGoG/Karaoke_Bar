import unittest
from classes.song import Song
import pdb

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song1 = Song("Highway to Hell", "Rock")        

    def test_song_go_to_different_list(self):
        # pdb.set_trace()
        self.assertEqual("Highway to Hell",self.song1.song_go_to_different_list("Highway to Hell", "Rock"))
