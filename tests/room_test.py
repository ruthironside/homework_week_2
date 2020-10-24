import unittest
from classes.room import *
from classes.guest import *
from classes.song import *

class TestRoom(unittest.TestCase):
    def setUp(self):


        self.guest_1 = Guest("Finn", 12)
        self.guest_2 = Guest("Jake", 28)
        self.guest_3 = Guest("Ice King", 1043)
        self.guest_4 = Guest("BMO", 1000)
        guests = [self.guest_1, self.guest_2, self.guest_3, self.guest_4]

        self.song_1 = Song("Wannabe", "Spice Girls", "Pop")
        self.song_2 = Song("Angels", "Robbie Williams", "Pop")
        self.song_3 = Song("Baggy Trousers", "Madness", "Ska")
        self.song_4 = Song("Country House", "Blur", "Brit Pop")
        self.song_5 = Song("Should I Stay Or Should I Go", "The Clash", "Rock")
        self.song_6 = Song("Achy Breaky Heart", "Billy Ray Cyrus", "Country")
        songs = [self.song_1, self.song_2, self.song_3, self.song_4, self.song_5, self.song_6]

        self.room = Room("one", 10, songs)
        self.room_1 = Room("one", 10, songs)
        self.room_2 = Room("two", 12, songs)
        self.room_3 = Room("three", 15, songs)
        self.room_4 = Room("four", 20, songs)
        rooms = [self.room_1, self.room_2, self.room_3, self.room_4]



    def test_room_has_name(self):
        self.assertEqual("one", self.room.name)

    def test_room_has_capacity(self):
        self.assertEqual(12, self.room_2.capacity)

    def test_song_has_name(self):
        self.assertEqual("Wannabe", self.song_1.name)

    def test_starts_with_no_guests(self):
        self.assertEqual(0, self.room.guest_count())

    def test_can_check_in_guest_to_room(self):
        guest = Guest("Lumpy Space Princess", 14)
        self.room.check_in_guest(guest)
        self.assertEqual(1, self.room.guest_count())

    def test_can_check_out_guest_from_room(self):
        guest = Guest("Lumpy Space Princess", 14)
        self.room.check_in_guest(guest)
        self.room.check_out_guest(guest)
        self.assertEqual(0, self.room.guest_count())

    def test_room_song_count(self):
        self.assertEqual(6, self.room_4.song_count())

    def test_add_song_to_room(self):
        song = Song("Ring of Fire", "Johnny Cash", "Country")
        self.room.add_song_to_room(song)
        self.assertEqual(7, self.room_1.song_count())