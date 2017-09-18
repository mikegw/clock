from .gear import Gear
from .rotation import Rotation
from .vector import Vector
from math import pi
import math

import bpy

class Clock():
    def render():
        gear_position = Vector(0,0,0)
        gear_rotation = Rotation(pi / 2, Vector(1, 0, 0))

        pinion_position = Vector(0,0,0)
        pinion_rotation = Rotation(pi / 2, Vector(1, 0, 0)) * Rotation(pi/8, Vector(0,0,1))

        gear = Gear(24).draw(bpy, gear_position, gear_rotation)
        pinion = Gear(8).draw(bpy, gear_position, pinion_rotation)

        gear.location[0] = -2.4
        pinion.location[0] = 0.81

        scene = bpy.data.scenes["Scene"]
        scene.frame_start = 0
        scene.frame_end = 359

        gear.keyframe_insert('rotation_euler', index=1 ,frame=0)
        gear.rotation_euler[1] = math.radians(30)
        gear.keyframe_insert('rotation_euler', index=1 ,frame=359)

        pinion.keyframe_insert('rotation_euler', index=1 ,frame=0)
        pinion.rotation_euler[1] = math.radians(-90)
        pinion.keyframe_insert('rotation_euler', index=1 ,frame=359)


        # gear_position += Vector(0,1,0)
        # pinion_position += Vector(0,1,0)
        # gear_rotation *= Rotation(pi / 100, Vector(0, 0, 1))
        # pinion_rotation *= Rotation(-3*pi / 100, Vector(0, 0, 1))
        #
        # Gear(24).draw(bpy, gear_position, gear_rotation)
        # Gear(8).draw(bpy, pinion_position, pinion_rotation)
