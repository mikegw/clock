import unittest
from unittest.mock import Mock
from lib import gear
from itertools import count

class GearTest(unittest.TestCase):
    def test_teeth(self):
        test_gear = gear.Gear(teeth=12)
        self.assertEqual(test_gear.teeth, 12)

    def test_string(self):
        gear.Gear._count = count(1)
        test_gear = gear.Gear(teeth=3)
        self.assertEqual(str(test_gear), "Gear 1")

        test_gear_2 = gear.Gear(teeth=4)
        self.assertEqual(str(test_gear_2), "Gear 2")


class GearDrawingTest(unittest.TestCase):
    def setUp(self):
        gear.Gear._count = count(1)
        self.blender_mock = Mock()

        self.mesh = Mock()
        self.blender_mock.data.meshes.new = Mock(return_value = self.mesh)

        self.object = Mock()
        self.blender_mock.data.objects.new = Mock(return_value = self.object)

        self.test_gear = gear.Gear(teeth=12)
        self.test_gear.draw((0,0,0), self.blender_mock)

    def test_mesh_creation(self):
        self.blender_mock.data.meshes.new.assert_called_with("Gear 1")

    def test_object_creation(self):
        self.blender_mock.data.objects.new.assert_called_with("Gear 1", self.mesh)

    def test_object_linked_to_scene(self):
        self.blender_mock.context.scene.objects.link.assert_called_with(self.object)
        
