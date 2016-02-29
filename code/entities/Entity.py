from uuid import uuid4

from py2neo import Node, Relationship

import settings


class Entity(object):
    id = None
    __relationships = None
    __node = None

    def __init__(self):
        self.__relationships = []

    def _get_node(self):
        if self.__node is None:
            self.__node = settings.GRAPH.find_one(self.__class__.__name__, property_key="id", property_value=self.id)
        return self.__node

    def save(self):
        if self.id is None:
            self.id = str(uuid4())

            values = self.__dict__
            self.__node = Node(self.__class__.__name__, **values)

            if len(self.__relationships) > 0:
                self.__node, = settings.GRAPH.create(self.__node, *self.__relationships)
            else:
                self.__node, = settings.GRAPH.create(self.__node)

        else:
            obj = self._get_node()
            for (name, value) in self.__dict__.items():
                if name == "_Entity__relationships" or name == "_Entity__node":
                    continue
                obj[name] = value
            obj.push()

            if len(self.__relationships) > 0:
                settings.GRAPH.create(*self.__relationships)

    def add_relationship(self, relationship_type, other_node):
        relationship = Relationship(self._get_node(), relationship_type, other_node._get_node())
        self.__relationships.append(relationship)

    @classmethod
    def get_entities(cls, property_key=None, property_value=None):
        nodes = settings.GRAPH.find(cls.__name__, property_key=property_key, property_value=property_value)

        return_values = []
        for node in nodes:
            obj = cls()
            for (key, value) in node.properties.items():
                obj.key = value
            return_values.append(obj)

        return return_values
