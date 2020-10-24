import unittest
from classes.guest import *

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Finn", 12)

    def test_guest_has_name(self):
        self.assertEqual("Finn", self.guest.name)
    
    def test_guest_has_age(self):
        self.assertEqual(12, self.guest.age)