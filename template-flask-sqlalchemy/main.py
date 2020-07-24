from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(
    basedir, 'test.db')
db = SQLAlchemy(app)

# 一
class Person(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    pets = db.relationship('Pet', backref='owner')

    def __init__(self, username):
        self.username = username

# 多
class Pet(db.Model):
    __tablename__ = 'pet'
    id = db.Column(db.Integer, primary_key=True)
    petname = db.Column(db.String(80), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('person.id'))

    def __init__(self, petname, owner_id):
        self.petname = petname
        self.owner_id = owner_id


@app.route('/create_db')
def index():
    db.create_all()

    u = Person('Max')
    db.session.add(u)
    db.session.commit()

    p = Pet('dog', u.id)
    db.session.add(p)
    db.session.commit()

    return 'ok'


@app.route('/one_to_many')
def db_relation():
    u = Person.query.filter_by(username='Max').first()
    print('==========', u.pets)
    print('==========', u.pets[0].petname)

    p = Pet.query.filter_by(petname='dog').first()
    print('---------', p.owner.username)
    print('---------', p.owner_id)
    return 'ok'


if __name__ == "__main__":
    app.run(debug=True)
