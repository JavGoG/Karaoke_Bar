from classes.guest import Guest
from classes.room import Room
import unittest

from classes.room import Room

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room1 = Room("Rock", 10, 5)
        self.guest1 = Guest("Michael",100)
    
    def test_check_in_guests_to_rooms(self):
        self.assertEqual("Michael", self.guest1.name)
    
    
        
