from classes.guest import Guest
from classes.room import Room
import unittest
import pdb

from classes.room import Room

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room1 = Room("Rock", 10, 5)
        self.guest1 = Guest("Michael",100)
        self.Rock_list = []
    
    def test_check_in_guests_to_room(self):
        self.room1.check_in_guests_to_room("Michael", "Rock", 5)
        # pdb.set_trace()
        print(self.room1.room_list)
        self.assertEqual(True, "Michael" in self.room1.room_list )
    
    def test_check_out_guests_from_room(self):
        # pdb.set_trace()
        self.room1.check_in_guests_to_room("Michael", "Rock", 5)
        self.room1.check_out_guests_from_room("Michael")
        self.assertEqual(False, "Michael" in self.room1.room_list )


    def test_add_entry_fee_room(self):
        self.room1.add_entry_fee_room("Michael", "Rock", 5)
        self.assertEqual("Michael", self.room1.list_of_fees["Rock"])

    def test_remove_entry_fee_room(self):
        self.room1.remove_entry_fee_room("Michael", "Rock")
        self.assertEqual("no fee", self.room1.list_of_fees["Rock"])
    
    def test_track_entry_fee_per_room(self):
        self.room1.add_entry_fee_room("John", "Opera", 7)
        # Why if I do not call the add_entry_fee() 
        # the track_entry_fee_per_room() do not pass the test
        # Is it because every test is independent and the previous 
        # tests do not hold any value on its variables? 
        self.room1.track_entry_fee_per_room("Opera")
        self.assertEqual(self.room1.list_of_fees["Opera"], "John" )

    def test_get_total_fee(self):
        self.room1.check_in_guests_to_room("Michael", "Rock", 5)
        self.room1.get_total_fee()
        self.assertEqual(5, self.room1.fee_total)

