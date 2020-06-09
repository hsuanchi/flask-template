from .. import db


class Person(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)

    def __init__(self, username):
        self.username = username