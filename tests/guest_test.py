import unittest
from classes.guest import *
from classes.careoke_club import *

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Batman", 28, 15)

    def test_guest_has_name(self):
        self.assertEqual("Batman", self.guest.name)
    
    def test_guest_has_age(self):
        self.assertEqual(28, self.guest.age)

    def test_guest_has_money(self):
        self.assertEqual(15, self.guest.money)

    # def test_guest_can_afford_entryfee__sufficient_funds(self):
    #     can_afford_entryfee = guest_can_afford_entryfee(guest, self.entryfee)
    #     self.assertEqual(True, can_afford_entryfee)

    # def test_sufficient_funds__true_if_enough(self):
    #     self.assertEqual(True, self.guest.money(self.entryfee))

