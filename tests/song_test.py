import unittest
from classes.song import *

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Dancing Queen", "Abba", "Pop")

    def test_song_has_name(self):
        self.assertEqual("Dancing Queen", self.song.name)

    def test_song_has_artist(self):
        self.assertEqual("Abba", self.song.artist)

    def test_song_has_genre(self):
        self.assertEqual("Pop", self.song.genre)