import unittest
from lib.clock import *

class ClockUnitTests(unittest.TestCase):
    def test_clock_instantiation(self):
        clock = Clock()
        self.assertIsInstance(clock, Clock)
