import math
from .vector import Vector
from .vertex import Vertex
from .rotation import Rotation

class ToothProfiler():
    _pinion_teeth = 8
    _z_axis = Vector(0, 0, 1)

    _addendum = 1
    _dedendum = -1

    def __init__(self, density, module):
        self.density = 4 * density
        self.module = module

    def create_profile(self, tooth_count):
        tooth_angle = 2 * math.pi / tooth_count
        section_builder = self.__tooth_section_builder(
            tooth_count,
            tooth_angle,
            self.module,
            self._pinion_teeth,
            self._z_axis
        )
        first_dedendum = section_builder(tooth_angle / 4, self._dedendum, -1)
        first_addendum = section_builder(tooth_angle / 4, self._addendum,  1)
        second_addendum = section_builder(3 * tooth_angle / 4, self._addendum, -1)
        second_dedendum = section_builder(3 * tooth_angle / 4, self._dedendum,  1)

        return list(reversed(first_dedendum)) + \
            first_addendum + \
            list(reversed(second_addendum)) + \
            second_dedendum


    def __tooth_section_builder(self, tooth_count, tooth_angle, module, pinion_teeth, axis):
        def builder(start_angle, section_type, direction):
            pitch_radius = module * tooth_count / 2
            circle_radius = module * pinion_teeth / 2

            initial_rotation = Rotation(start_angle, axis)
            generator = initial_rotation.apply(Vertex(pitch_radius, 0, 0))

            center_offset = pitch_radius + section_type * circle_radius
            circle_center = initial_rotation.apply(Vector(center_offset, 0, 0))

            gear_rotation_angle = direction * tooth_angle / self.density
            gear_rotation = Rotation(gear_rotation_angle, axis)

            circle_rotation_angle = tooth_angle * tooth_count / self._pinion_teeth
            circle_rotation_angle = circle_rotation_angle * section_type * direction
            circle_rotation = Rotation(circle_rotation_angle / self.density, axis)

            profile = [generator]

            end_angle = start_angle + tooth_angle * direction / 4

            while True:
                circle_center = gear_rotation.apply(circle_center)
                generator = gear_rotation.apply(generator)
                generator = circle_rotation.apply(generator, circle_center)
                if self.__between_angles(generator, start_angle, end_angle):
                    profile.append(generator)
                else:
                    break
            return profile

        return builder


    def __angle_of_vector(self, vector):
        return math.atan(vector.y / vector.x)

    def __between_angles(self, vector, start_angle, end_angle):
        angle = self.__angle_of_vector(vector)
        if start_angle > end_angle:
            return (angle >= end_angle and angle < start_angle)
        else:
            return (angle <= end_angle and angle > start_angle)
