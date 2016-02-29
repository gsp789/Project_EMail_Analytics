from entities.Entity import Entity

import settings


class EmailAddress(Entity):
    address = None

    def __init__(self, address):
        super().__init__()
        db_object = settings.GRAPH.find_one(self.__class__.__name__, property_key="address", property_value=address)
        if db_object is not None:
            self.id = db_object.properties['id']
            self.address = db_object.properties['address']
        else:
            self.address = address

    def __str__(self):
        return str(self.address)
