import math
from lib.vector import Vector
from lib.rotation import Rotation

class ToothProfiler():
    def __init__(self, density, module):
        self.density = density
        self.module = module

    def create_profile(self, tooth_count):
        start_vector = Vector(self.module, 0, 0)
        return (start_vector,) * self.density
