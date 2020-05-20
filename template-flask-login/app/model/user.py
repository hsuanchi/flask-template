from .. import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask import session


class User(db.Model):
    __tablename__ = 'user'
    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    password_hash = db.Column(db.String(255))
    role = db.Column(db.String(10))
    insert_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime,
                            onupdate=datetime.now,
                            default=datetime.now)

    def __init__(self, name, passowrd, role='normal'):
        self.name = name
        self.password = passowrd
        self.role = role

    @property
    def password(self):
        raise AttributeError('passowrd is not readabilty attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    @classmethod
    def get_user(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def save_user_session(self):
        session['username'] = self.name
        session['role'] = self.role
        session['uid'] = self.uid

    @staticmethod
    def remove_user_session():
        session['username'] = ''
        session['role'] = ''
        session['uid'] = ''