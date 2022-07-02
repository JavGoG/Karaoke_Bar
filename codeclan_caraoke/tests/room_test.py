from classes.guest import Guest
import unittest

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.guest1 = Guest("Peter", "Rock")
        self.guest2 = Guest("Thomas", "Opera")
        self.list_of_rooms = [
                                {"Rock":[]  },
                                {"Pop":[] },
                                {"Opera":[] }
                            ]
    
    def test_check_in_guests_to_rooms(self):
        self.assertEqual("Peter", self.guest1.check_in_guests_to_rooms(self.guest1.name, self.guest1.room))
    
    
        
