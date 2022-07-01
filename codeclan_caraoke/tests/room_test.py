from classes.guest import Guest
import unittest

class TestRoom:
    def __init__(self, name, name_of_guest):
        self.name = name
        self.name_of_guest = name_of_guest
        self.list_of_rooms = [
                                {"Rock":[]  },
                                {"Pop":[] },
                                {"Opera":[] }
                            ]
    def setUp(self):
        self.guest1 = self.Guest("Peter", "Rock")
    
    def test_check_in_guests_to_rooms(self):
        self.assertEgual("Peter", self.list_of_rooms[0][self.guest1.room])
        
