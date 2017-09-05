import unittest
import math
from lib.vector import Vector

class VectorTest(unittest.TestCase):
    def new_vector(self, *args):
        return Vector(*args)

    def setUp(self):
        self.vector = self.new_vector(3, 4, 5, 6)

    def test_it_exposes_individual_values(self):
        self.assertEqual(self.vector[0], 3)
        self.assertEqual(self.vector[1], 4)
        self.assertEqual(self.vector[2], 5)
        self.assertEqual(self.vector[3], 6)

    def test_it_exposes_x_y_and_z_coordinates(self):
        self.assertEqual(self.vector.x, 3)
        self.assertEqual(self.vector.y, 4)
        self.assertEqual(self.vector.z, 5)

    def test_it_gracefully_handles_one_dimensions(self):
        vector = Vector(4)
        self.assertEqual(vector.x, 4)

    def test_it_has_a_dimension(self):
        self.assertEqual(self.vector.dimension(), 4)

    def test_its_length_is_its_dimension(self):
        self.assertEqual(len(self.vector), 4)

    def test_two_vectors_are_equal_if_they_have_the_same_values(self):
        vector1 = self.new_vector(1, 2, 3)
        vector2 = self.new_vector(1, 2, 3)
        self.assertEqual(vector1, vector2)

    def test_two_vectors_are_not_equal_if_they_do_not_have_the_same_values(self):
        vector1 = self.new_vector(1, 2, 3)
        vector2 = self.new_vector(1, 5, 3)
        self.assertNotEqual(vector1, vector2)

    def test_it_can_be_added_to_another_vector(self):
        vector1 = self.new_vector(1, 2, 3)
        vector2 = self.new_vector(1, 2, 3)
        vector3 = vector1 + vector2
        self.assertEqual(vector3, self.new_vector(2, 4, 6))

    def test_it_has_a_norm(self):
        expected_norm = math.sqrt(3**2 + 4**2 + 5**2 + 6**2)
        self.assertEqual(self.vector.norm(), expected_norm)

    def test_it_can_be_multiplied_by_a_scalar(self):
        doubled_vector = self.new_vector(6, 8, 10, 12)
        self.assertEqual(self.vector * 2, doubled_vector)
        self.assertEqual(2 * self.vector, doubled_vector)

    def test_it_can_be_divided_by_a_scalar(self):
        doubled_vector = self.new_vector(6, 8, 10, 12)
        self.assertEqual(self.vector, doubled_vector / 2)

    def test_it_has_a_direction(self):
        vector = Vector(3, 4)
        direction = Vector(0.6, 0.8)
        self.assertEqual(vector.direction(), direction)

    def test_it_can_be_negated(self):
        negated_vector = self.new_vector(-3, -4, -5, -6)
        self.assertEqual(-self.vector, negated_vector)

    def test_dot_product_returns_correct_scalar(self):
        vector1 = self.new_vector(1,2,3,4,5)
        vector2 = self.new_vector(3,4,5,6,7)
        self.assertEqual(vector1.dot(vector2), 1*3 + 2*4 + 3*5 + 4*6 + 5*7)

    def test_cross_product_only_works_for_3_dimensional_vectors(self):
        vector2d = self.new_vector(1,2)
        vector3d = self.new_vector(1,2,3)
        vector4d = self.new_vector(1,2,3,4)
        with self.assertRaises(TypeError):
            vector3d.cross(vector2d)
        with self.assertRaises(TypeError):
            vector3d.cross(vector4d)
        with self.assertRaises(TypeError):
            vector4d.cross(vector3d)
        with self.assertRaises(TypeError):
            vector2d.cross(vector3d)

    def test_cross_product_returns_correct_vector(self):
        vector1 = Vector(2, 3, 4)
        vector2 = Vector(-5, 6, -7)
        cross_product = vector1.cross(vector2)
        self.assertEqual(cross_product, Vector(-45, -6, 27))
