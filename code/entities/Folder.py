from entities.Entity import Entity


class Folder(Entity):
    name = None

    def __init__(self, name):
        super().__init__()
        self.name = name
