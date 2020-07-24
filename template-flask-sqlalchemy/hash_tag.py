from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os
basedir = os.path.abspath(os.path.dirname(__file__))

#TODO: 第二篇增加欄位選項
#TODO: 第二篇增加讀取全部選項

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(
    basedir, 'hashtag.db')
db = SQLAlchemy(app)

# 多
relations = db.Table(
    'relations', db.Column('tid', db.Integer,
                           db.ForeignKey('hashtag_table.id')),
    db.Column('pid', db.Integer, db.ForeignKey('post_table.id')))


# 一
class Hashtag(db.Model):
    __tablename__ = 'hashtag_table'
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(20), nullable=False)
    tag_post_rel = db.relationship("Post",
                                   secondary=relations,
                                   backref="hashtag")

    # backref='post', # ref 可以讓我們使用 Post.tags 進行對 tags 操作
    # lazy='dynamic' # 有使用才載入，提昇效能


# ㄧ
class Post(db.Model):
    __tablename__ = 'post_table'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    # tag_id = db.Column(db.Integer, db.ForeignKey('hashtag_table.id'))


@app.route('/create_db')
def index():
    # db.create_all()

    # t1 = Hashtag(tag='Max')
    # t2 = Hashtag(tag='Ben')

    # db.session.add_all([t1, t2])
    # db.session.commit()

    # p1 = Post(title='Post_1')
    # p2 = Post(title='Post_2')
    # p3 = Post(title='Post_3')

    # db.session.add_all([p1, p2, p3])
    # db.session.commit()

    tag1 = Hashtag.query.filter_by(tag='Max').first()
    print(tag1.id)

    tags = Hashtag.query.all()
    print(tags)

    for tag in tags:
        print(tag.id)
        print(tag.tag)

    return 'ok'


@app.route('/show')
def show():

    # u = Hashtag(tag='Max')
    # db.session.add(u)
    # db.session.commit()

    a = Hashtag(tag='Max')
    print(a.id)
    # # p = Post(title='0703', tag_id=1)
    # p = Post(title='070301', tag_id='')
    # # p = Pet('dog', u.id)
    # db.session.add(p)
    # db.session.commit()
    return 'ok'


# @app.route('/one_to_many')
# def db_relation():
#     u = Person.query.filter_by(username='Max').first()
#     print('==========', u.pets)
#     print('==========', u.pets[0].petname)

#     p = Pet.query.filter_by(petname='dog').first()
#     print('---------', p.owner.username)
#     print('---------', p.owner_id)
#     return 'ok'

if __name__ == "__main__":
    app.run(debug=True)
