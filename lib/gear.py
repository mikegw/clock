from itertools import count
from .vector import Vector

class Gear():
    _count = count(1)

    def __init__(self, teeth=None):
        self.teeth = teeth
        self.id = next(self._count)

    def __str__(self):
        return "Gear %s" % self.id

    def draw(self, center_position, blender):
        mesh = blender.data.meshes.new(str(self))
        obj = blender.data.objects.new(str(self), mesh)
        blender.context.scene.objects.link(obj)
        mesh.from_pydata(
            self.vertices(),
            [],
            self.faces()
        )

    def vertices(self):
        vertices = [
            Vector(0, 0, 0),
            Vector(0, 0, 1),
            Vector(0, 1, 0),
            Vector(1, 0, 0)
        ]

        return vertices

    def faces(self):
        return [
            (0, 1, 2),
            (0, 1, 3),
            (0, 2, 3)
        ]
