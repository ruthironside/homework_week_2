import unittest
from classes.room import *

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.room = Room()