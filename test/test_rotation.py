import unittest
import math
from lib.rotation import Rotation
from lib.vector import Vector

class RotationTest(unittest.TestCase):
    def new_rotation(self, angle, axis):
        return Rotation(angle, axis)

    def test_two_rotations_equal_if_they_have_the_same_angle_and_axis(self):
        r1 = self.new_rotation(2*math.pi/3, Vector(1, 2, 3))
        r2 = self.new_rotation(2*math.pi/3, Vector(1, 2, 3))
        self.assertEqual(r1, r2)

    def test_it_equates_all_0_rotations(self):
        r1 = self.new_rotation(0, Vector(1, 2, 3))
        r2 = self.new_rotation(0, Vector(5, -6, 1))
        self.assertEqual(r1, r2)

    def test_equality_comparison_ignores_magnitude_of_axis(self):
        r1 = self.new_rotation(2*math.pi/3, Vector(1, 2, 3))
        r2 = self.new_rotation(2*math.pi/3, Vector(2, 4, 6))
        self.assertEqual(r1, r2)

    def test_equality_comparison_ignores_complete_rotations(self):
        r1 = self.new_rotation(2*math.pi/3, Vector(1, 2, 3))
        r2 = self.new_rotation(8*math.pi/3, Vector(2, 4, 6))
        self.assertEqual(r1, r2)

    def test_equality_comparison_ignores_negative_rotations(self):
        r1 = self.new_rotation(2*math.pi/3, Vector(1, 2, 3))
        r2 = self.new_rotation(-4*math.pi/3, Vector(2, 4, 6))
        self.assertEqual(r1, r2)

    def test_it_equates_clockwise_rotations_with_anticlockwise_rotations_in_negative_directions(self):
        r1 = self.new_rotation(2*math.pi/3, -Vector(1, 2, 3))
        r2 = self.new_rotation(-2*math.pi/3, Vector(1, 2, 3))
        self.assertEqual(r1, r2)

    def test_it_has_a_reciprocal(self):
        rotation = self.new_rotation(1, Vector(1, 2, 3))
        reciprocal = self.new_rotation(1, Vector(-1, -2, -3))
        self.assertEqual(rotation.reciprocal(), reciprocal)

    def test_it_can_be_composed_with_itself(self):
        rotation = self.new_rotation(2*math.pi/3, Vector(1, 2, 3))
        zero_rotation = self.new_rotation(0, Vector(1, 0, 0))
        self.assertEqual(rotation * rotation * rotation, zero_rotation)

    def test_it_can_be_composed_with_other_rotations(self):
        rotation_i = self.new_rotation(math.pi, Vector(1, 0, 0))
        rotation_j = self.new_rotation(math.pi, Vector(0, 1, 0))
        rotation_k = self.new_rotation(math.pi, Vector(0, 0, 1))
        self.assertEqual(rotation_i * rotation_j, rotation_k)

    def test_can_rotate_a_vector_in_2d(self):
        vector = Vector(1, 2, 0)
        rotation = self.new_rotation(math.pi/2, Vector(0, 0, 1))
        rotated = rotation.apply(vector)
        self.assertEqual(rotated, Vector(-2, 1, 0))

    def test_can_rotate_a_vector_in_3d(self):
        vector = Vector(1, 0, 0)
        rotation = self.new_rotation(2*math.pi/3, Vector(1, 1, 1))
        rotated = rotation.apply(vector)
        self.assertEqual(rotated, Vector(0, 1, 0))

    def test_can_rotate_a_vector_around_a_point_in_2d(self):
        vector = Vector(1, 2, 0)
        rotation = self.new_rotation(math.pi/2, Vector(0, 0, 1))
        rotated = rotation.apply(vector, Vector(1, 1, 0))
        self.assertEqual(rotated, Vector(0, 1, 0))

    def test_can_rotate_a_vector_around_a_point_in_3d(self):
        vector = Vector(1, 2, 3)
        rotation = self.new_rotation(math.pi, Vector(2, 1, 0))
        rotated = rotation.apply(vector, Vector(1, 1, 1))
        self.assertEqual(rotated, Vector(1.8, 0.4, -1))
