from classes.guest import Guest
import unittest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Michael", 100)

    def test_name_of_guest(self):
        self.assertEqual("Michael", self.guest1.name)

    def test_wallet_of_guest(self):
        self.assertEqual(100, self.guest1.wallet)
