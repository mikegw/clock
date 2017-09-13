from .gear import Gear
from .rotation import Rotation
from .vector import Vector
from math import pi

import bpy

class Clock():
    def render():
        initial_position = Vector(0,0,0)
        initial_rotation = Rotation(pi/2, Vector(1, 0, 0))
        gear = Gear(20)
        gear.draw(bpy, initial_position, initial_rotation)
