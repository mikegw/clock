import math
from math import pi
from .vector import Vector

class Quaternion():
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __mul__(self, other):
        real = self.real * other.real - self.imaginary.dot(other.imaginary)
        imaginary = (self.real * other.imaginary) + \
            (self.imaginary * other.real) + \
            (self.imaginary.cross(other.imaginary))
        return Quaternion(real, imaginary)


class Rotation():
    def __init__(self, angle, axis):
        self.angle = angle % (2 * pi)
        self.axis = axis.direction()

    def reciprocal(self):
        return Rotation(self.angle, -self.axis)

    def apply(self, vector, origin = Vector(0, 0, 0)):
        quaternion = self._to_quaternion_()
        reciprocal_quaternion = self.reciprocal()._to_quaternion_()
        conjugated = quaternion * Quaternion(0, vector - origin) * reciprocal_quaternion
        return conjugated.imaginary + origin

    def _to_quaternion_(self):
        return Quaternion(
            math.cos(self.angle / 2),
            math.sin(self.angle / 2) * self.axis
        )

    def __mul__(self, other):
        self_quaternion = self._to_quaternion_()
        other_quaternion = other._to_quaternion_()

        new_quaternion = self_quaternion * other_quaternion
        return Rotation(
            2 * math.acos(new_quaternion.real),
            new_quaternion.imaginary
        )

    def __str__(self):
        return "Rotation(angle: {}, axis: {})".format(
            round(self.angle, 5),
            self.axis
        )

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        rounded_self_angle = round(self.angle, 10)
        rounded_other_angle = round(other.angle, 10)

        same_angle = rounded_self_angle == rounded_other_angle
        same_axis = self.axis == other.axis

        opposite_angle = round(self.angle + other.angle - 2*pi) == 0
        opposite_axis = self.axis == -(other.axis)
        return (same_angle and same_axis) or \
            (opposite_angle and opposite_axis) or \
            (rounded_self_angle == 0 and rounded_other_angle == 0)
