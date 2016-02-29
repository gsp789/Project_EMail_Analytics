from entities.Entity import Entity


class Person(Entity):
    name = None

    def __init__(self, name):
        super().__init__()
        self.name = name
