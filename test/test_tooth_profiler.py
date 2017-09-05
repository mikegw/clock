import unittest
import math
from lib.tooth_profiler import ToothProfiler
from lib.rotation import Rotation
from lib.vector import Vector

class ToothProfilerTest(unittest.TestCase):
    def setUp(self):
        self.profiler = ToothProfiler(density = 20, module = 2)
        self.profile = self.profiler.create_profile(12)

    def test_tooth_profiler_creates_tooth_vertices(self):
        self.assertEqual(len(self.profile), 20)

    def test_tooth_profile_starts_at_the_x_axis(self):
        self.assertEqual(self.profile[0].direction(), Vector(1, 0, 0))

    def test_tooth_profile_fits_in_the_circular_pitch(self):
        end_of_profile = self.profile[-1]
        rotation = Rotation(math.pi/6, Vector(0, 0, 1))
        expected_direction = rotation.apply(Vector(1, 0, 0))
        self.assertEqual(end_of_profile.direction(), expected_direction)
