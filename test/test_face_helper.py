import unittest
import math
from lib.rotation import Rotation
from lib.vector import Vector
from lib.face_helper import faces_between_vertex_groups

class FacesBetweenVertexGroupsTest(unittest.TestCase):
    def test_returns_one_face_by_default(self):
        vertex_group_1 = (2,3,4)
        vertex_group_2 = (12,13)
        faces = faces_between_vertex_groups(
            group_1 = vertex_group_1,
            group_2 = vertex_group_2
        )
        expected_faces = [(2,3,4,13,12)]
        self.assertEqual(faces, expected_faces)

    def test_can_return_loop_of_2_faces(self):
        vertex_group_1 = (2,3,4,5,6)
        vertex_group_2 = (12,13)
        faces = faces_between_vertex_groups(
            group_1 = vertex_group_1,
            group_2 = vertex_group_2,
            create_loop = True
        )
        expected_faces = [
            (2,3,4,5,13,12),
            (5,6,2,12,13)
        ]
        self.assertEqual(faces, expected_faces)

    def test_can_return_more_faces(self):
        vertex_group_1 = (2,3,4,5,6)
        vertex_group_2 = (12,13,14)
        faces = faces_between_vertex_groups(
            group_1 = vertex_group_1,
            group_2 = vertex_group_2,
            face_count = 3,
            create_loop = True
        )
        expected_faces = [
            (2,3,4,13,12),
            (4,5,6,14,13),
            (6,2,12,14)
        ]
        self.assertEqual(faces, expected_faces)
