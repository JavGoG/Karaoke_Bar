from classes.guest import Guest
import unittest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Michael", 100)