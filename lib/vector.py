import math

class Vector():
    def __init__(self, *args):
        self.values = args
        self.x = args[0]
        if len(args) > 1:
            self.y = args[1]
        if len(args) > 2:
            self.z = args[2]

    def dimension(self):
        return len(self)

    def norm(self):
        return math.sqrt(sum(value**2 for value in self.values))

    def direction(self):
        return self / self.norm()

    def dot(self, other):
        return sum(v1 * v2 for v1, v2 in zip(self.values, other.values))

    def cross(self, other):
        if self.dimension() != 3:
            raise TypeError("{} is not 3-dimensional".format(self))
        if other.dimension() != 3:
            raise TypeError("{} is not 3-dimensional".format(other))
        return Vector(
            (self.y * other.z) - (self.z * other.y),
            (self.z * other.x) - (self.x * other.z),
            (self.x * other.y) - (self.y * other.x)
        )

    def __str__(self):
        rounded_values = (str(round(value, 5)) for value in self.values)
        return 'Vector({})'.format(", ".join(rounded_values))

    def __repr__(self):
        return str(self)

    def __getitem__(self, index):
        return self.values.__getitem__(index)

    def __add__(self, other):
        new_values = (v1 + v2 for v1, v2 in zip(self.values, other.values))
        return Vector(*new_values)

    def __sub__(self, other):
        return self + (-other)

    def __len__(self):
        return self.values.__len__()

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return false

        def rounded_values(values):
            return [round(value, 10) for value in values]

        rounded_self_values = rounded_values(self.values)
        rounded_other_values = rounded_values(other.values)

        return rounded_self_values == rounded_other_values

    def __mul__(self, other):
        return Vector(*(value * other for value in self.values))

    def __rmul__(self, other):
        return Vector(*(other * value for value in self.values))

    def __truediv__(self, other):
        return Vector(*(value / other for value in self.values))

    def __neg__(self):
        return Vector(*(value.__neg__() for value in self.values))
