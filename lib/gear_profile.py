from .vector import Vector
from .vertex import Vertex
from .rotation import Rotation
from .tooth_profiler import ToothProfiler
import math


class GearProfile():
    _density = 8
    _axle_vertices = 24
    _axle_radius = 0.2
    _module = 0.2

    def __init__(self, teeth):
        self.__teeth = teeth

    def outer_vertices(self):
        try:
            return self.__outer
        except AttributeError:
            self.__outer = self.__calculate_outer_vertices()
            return self.__outer

    def inner_vertices(self):
        try:
            return self.__inner
        except AttributeError:
            self.__inner = self.__calculate_inner_vertices()
            return self.__inner


    def __calculate_outer_vertices(self):
        profiler = ToothProfiler(density = self._density, module = self._module)
        outer_profile = profiler.create_profile(tooth_count = self.__teeth)
        return self.__rotations_of_profile(outer_profile)

    def __calculate_inner_vertices(self):
        inner_profile = []
        inner_density = self._axle_vertices // self.__teeth
        for i in range(inner_density):
            rotation = Rotation(
                angle = (i / inner_density) * (2 * math.pi / self.__teeth),
                axis = Vector(0,0,1)
            )
            inner_profile.append(rotation.apply(Vertex(self._axle_radius,0,0)))
        return self.__rotations_of_profile(inner_profile)

    def __rotations_of_profile(self, profile):
        vertices = tuple()
        for i in range(self.__teeth):
            rotation = Rotation(
                angle = i * (2 * math.pi / self.__teeth),
                axis = Vector(0, 0, 1)
            )
            rotated_profile = tuple(rotation.apply(v) for v in profile)
            vertices += rotated_profile
        return vertices
