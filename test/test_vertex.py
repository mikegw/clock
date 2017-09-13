import unittest
from lib.vertex import *
from lib.vector import *
from lib.rotation import *

class VertexTest(unittest.TestCase):
    def setUp(self):
        self.vertex = Vertex(1,2,3)
        self.vertex.id = 54

    def test_can_set_vertex_id(self):
        self.assertEqual(self.vertex.id, 54)

    def test_can_translate_a_vertex(self):
        self.vertex.translate(Vector(1,1,1))
        self.assertEqual(self.vertex, Vertex(2,3,4))

    def test_translation_mutates_object(self):
        face = [self.vertex]
        self.vertex.translate(Vector(1,1,1))
        self.assertEqual(self.vertex, face[0])

    def test_can_rotate_a_vertex(self):
        rotation = Rotation(math.pi, Vector(2, 1, 0))
        self.vertex.rotate(rotation, Vector(1, 1, 1))
        self.assertEqual(self.vertex, Vector(1.8, 0.4, -1))

    def test_rotation_mutates_object(self):
        face = [self.vertex]
        rotation = Rotation(math.pi, Vector(2, 1, 0))
        self.vertex.rotate(rotation, Vector(1, 1, 1))
        self.assertEqual(self.vertex, face[0])
