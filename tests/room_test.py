import unittest
from classes.room import *
from classes.guest import *

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("one", 10)

        self.room_1 = Room("one", 10)
        self.room_2 = Room("two", 12)
        self.room_3 = Room("three", 15)
        self.room_4 = Room("four", 20)
        rooms = [self.room_1, self.room_2, self.room_3, self.room_4]

        self.guest_1 = Guest("Finn", 12)
        self.guest_2 = Guest("Jake", 28)
        self.guest_3 = Guest("Ice King", 1043)
        self.guest_4 = Guest("BMO", 1000)
        guests = [self.guest_1, self.guest_2, self.guest_3, self.guest_4]

    def test_room_has_name(self):
        self.assertEqual("one", self.room.name)