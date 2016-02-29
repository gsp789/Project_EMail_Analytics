from hashlib import md5

from entities.Entity import Entity


class Email(Entity):
    date = None
    subject = None
    body = None
    body_hash = None

    def __init__(self, date=None, subject=None, body=None):
        super().__init__()
        self.body = body
        self.subject = subject
        self.date = date

    def __str__(self):
        return "'This is a fuckin' Email' -- Ryan Hornik"

    def save(self):
        self.body_hash = md5(self.body.encode('utf-8')).hexdigest()
        super(Email, self).save()
