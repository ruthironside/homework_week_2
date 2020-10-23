import unittest
from classes.song import *

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.song = Song()