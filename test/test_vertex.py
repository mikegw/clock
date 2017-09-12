import unittest
from lib.vertex import *

class VertexTest(unittest.TestCase):
    def test_can_set_vertex_id(self):
        vertex = Vertex(1,2,3)
        vertex.id = 54
        self.assertEqual(vertex.id, 54)
