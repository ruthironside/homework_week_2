import unittest
from classes.careoke_club import *

class TestCareokeClub(unittest.TestCase):
    def setUp(self):
        self.careoke_club = CareokeClub(200, 40)

    def test_club_has_entry_fee(self):
        self.assertEqual(40, self.careoke_club.entryfee)
    
    def test_club_has_till(self):
        self.assertEqual(200, self.careoke_club.till)

    # def test_guest_can_afford_entry_fee__returns_true(self):
    #     self.assertEqual(True, self.careoke_club.sufficient_funds(self.guest_1, self.entryfee))