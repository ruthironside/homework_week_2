import unittest
from classes.guest import *
from classes.careoke_club import *

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Finn", 12, 15)

    def test_guest_has_name(self):
        self.assertEqual("Finn", self.guest.name)
    
    def test_guest_has_age(self):
        self.assertEqual(12, self.guest.age)

    def test_guest_has_money(self):
        self.assertEqual(15, self.guest.money)

    # def test_sufficient_funds__true_if_enough(self):
    #     self.assertEqual(True, self.guest.sufficient_funds(self.entry_fee))

