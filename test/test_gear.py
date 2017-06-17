import unittest
from lib import gear

class GearTest(unittest.TestCase):
    def test_teeth(self):
        """A gear has teeth"""
        test_gear = gear.Gear(teeth=12)
        self.assertEqual(test_gear.teeth, 12)
