import unittest
from classes.song import *

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song()