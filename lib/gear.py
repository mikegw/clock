from itertools import count
from .vector import Vector
from .gear_profile import GearProfile
from . import face_helper

class Gear():
    _count = count(1)
    _depth = 0.2

    def __init__(self, teeth=None):
        self.__teeth = teeth
        self.__gear_profile = GearProfile(teeth)
        self.__id = next(self._count)

    def __str__(self):
        return "Gear %s" % self.id

    @property
    def teeth(self):
        return self.__teeth

    @property
    def id(self):
        return self.__id

    def draw(self, blender, center_position = Vector(0,0,0), rotation = None):
        mesh = blender.data.meshes.new(str(self))
        obj = blender.data.objects.new(str(self), mesh)
        blender.context.scene.objects.link(obj)

        vertices = self.vertices()
        for vertex_id in range(len(vertices)):
            vertex = vertices[vertex_id]
            if rotation:
                vertex.rotate(rotation, Vector(0,0,0))
            vertex.translate(center_position)
            vertex.id = vertex_id

        faces = self.faces()
        faces_as_ints = [tuple(vertex.id for vertex in face) for face in faces]

        mesh.from_pydata(vertices, [], faces_as_ints)
        mesh.update(calc_edges = True)

    def vertices(self):
        vertices = list(
            self.__inner_bottom_vertices() + \
            self.__outer_bottom_vertices() + \
            self.__outer_top_vertices()    + \
            self.__inner_top_vertices()
        )
        return vertices

    def faces(self):
        faces = []
        faces += face_helper.faces_between_vertex_groups(
            self.__outer_top_vertices(),
            self.__inner_top_vertices(),
            create_loop = True,
            face_count = self.teeth
        )
        faces += face_helper.faces_between_vertex_groups(
            self.__inner_top_vertices(),
            self.__inner_bottom_vertices(),
            create_loop = True,
            face_count = self.teeth
        )
        faces += face_helper.faces_between_vertex_groups(
            self.__inner_bottom_vertices(),
            self.__outer_bottom_vertices(),
            create_loop = True,
            face_count = self.teeth
        )
        faces += face_helper.faces_between_vertex_groups(
            self.__outer_bottom_vertices(),
            self.__outer_top_vertices(),
            create_loop = True,
            face_count = len(self.__outer_bottom_vertices())
        )
        return faces

    def __inner_bottom_vertices(self):
        try:
            return self.__inner_bottom
        except AttributeError:
            self.__inner_bottom = self.__gear_profile.inner_vertices()
            return self.__inner_bottom

    def __outer_bottom_vertices(self):
        try:
            return self.__outer_bottom
        except AttributeError:
            self.__outer_bottom = self.__gear_profile.outer_vertices()
            return self.__outer_bottom

    def __inner_top_vertices(self):
        try:
            return self.__inner_top
        except AttributeError:
            depth = Vector(0, 0, self._depth)
            vectors = tuple(v + depth for v in self.__inner_bottom_vertices())
            self.__inner_top = vectors
            return self.__inner_top

    def __outer_top_vertices(self):
        try:
            return self.__outer_top
        except AttributeError:
            depth = Vector(0, 0, self._depth)
            vectors = tuple(v + depth for v in self.__outer_bottom_vertices())
            self.__outer_top = vectors
            return self.__outer_top
