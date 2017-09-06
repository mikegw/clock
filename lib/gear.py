from itertools import count
from .vector import Vector
from .rotation import Rotation
from .tooth_profiler import ToothProfiler
from . import face_helper
import math

class Gear():
    _count = count(1)
    _density = 10
    _axle_vertices = 24
    _axle_radius = 0.2
    _module = 0.2

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
        mesh.update(calc_edges = True)

    def vertices(self):
        return list(
            self.__outer_profile_vertices() + self.__inner_profile_vertices()
        )

    def faces(self):
        outer_profile_id_min = 0
        outer_profile_id_max = len(self.__outer_profile_vertices())
        inner_profile_id_min = outer_profile_id_max
        inner_profile_id_max = \
            outer_profile_id_max + len(self.__inner_profile_vertices())
        faces = face_helper.faces_between_vertex_groups(
            tuple(range(outer_profile_id_min, outer_profile_id_max)),
            tuple(range(inner_profile_id_min, inner_profile_id_max)),
            create_loop = True,
            face_count = self.teeth
        )
        print(faces)
        return faces

    def __outer_profile_vertices(self):
        if not hasattr(self, '__outer'):
            self.__outer = self.__calculate_outer_profile_vertices()
        return self.__outer

    def __inner_profile_vertices(self):
        if not hasattr(self, '__inner'):
            self.__inner = self.__calculate_inner_profile_vertices()
        return self.__inner

    def __calculate_outer_profile_vertices(self):
        profiler = ToothProfiler(density = self._density, module = self._module)
        outer_profile = profiler.create_profile(tooth_count = self.teeth)
        return self.__rotations_of_profile(outer_profile)

    def __calculate_inner_profile_vertices(self):
        inner_profile = []
        inner_density = self._axle_vertices // self.teeth
        for i in range(inner_density):
            rotation = Rotation(
                angle = (i / inner_density) * (2 * math.pi / self.teeth),
                axis = Vector(0,0,1)
            )
            inner_profile.append(rotation.apply(Vector(self._axle_radius,0,0)))
        return self.__rotations_of_profile(inner_profile)

    def __rotations_of_profile(self, profile):
        vertices = []
        for i in range(self.teeth):
            rotation = Rotation(
                angle = i * (2 * math.pi / self.teeth),
                axis = Vector(0, 0, 1)
            )
            rotated_profile = [rotation.apply(v) for v in profile]
            vertices += rotated_profile
        return vertices
