from .vector import Vector

class Vertex(Vector):
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, new_id):
        self.__id = new_id

    def __str__(self):
        rounded_values = (str(round(value, 5)) for value in self.values)
        try:
            id = str(self.id)
        except AttributeError:
            id = "?"
        return '{}[{}]({})'.format(
            type(self).__name__,
            id,
            ", ".join(rounded_values)
        )
