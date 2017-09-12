import math
from .vector import Vector
from .vertex import Vertex
from .rotation import Rotation

class ToothProfiler():
    def __init__(self, density, module):
        self.density = density
        self.module = module

    def create_profile(self, tooth_count):
        pitch_radius = self.module * tooth_count / 2
        start_vector = Vertex(pitch_radius, 0, 0)
        tooth_angle = 2 * math.pi / tooth_count
        rotation = Rotation(tooth_angle / self.density, Vector(0, 0, 1))
        profile = [start_vector]
        for angle in range(0, self.density - 1):
            scaled_vertex = profile[-1] * (1 + (angle / (self.density * 20)))
            profile.append(rotation.apply(scaled_vertex))

        return profile
