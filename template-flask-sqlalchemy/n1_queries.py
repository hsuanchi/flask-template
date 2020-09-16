from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import get_debug_queries

from sqlalchemy.orm import joinedload

import os
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(
    basedir, 'n1.db')

app.config['SQLALCHEMY_RECORD_QUERIES'] = True

# app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

relations = db.Table(
    'relations',
    db.Column('tid', db.Integer, db.ForeignKey('hashtag_table.id'),
              index=True),
    db.Column('pid', db.Integer, db.ForeignKey('post_table.id'), index=True),
    db.Index("ix_tid_pid", "tid", "pid", unique=True))


class Hashtag(db.Model):
    __tablename__ = 'hashtag_table'
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(20), nullable=False)


class Post(db.Model):
    __tablename__ = 'post_table'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    post_tag_rel = db.relationship("Hashtag",
                                   secondary=relations,
                                   lazy='joined',
                                   backref=db.backref("post", lazy='joined'))


@app.after_request
def after_request(reponse):
    for query in get_debug_queries():
        query_time = query.duration
        query_param = query.parameters
        query_statement = query.statement
        print(f'------------------------------------------\
            \n花費時間：{query_time},\
            \n傳入參數：{query_param},\
            \n查詢語法：{query_statement}\
            \n------------------------------------------')
    return reponse


@app.route('/create_db')
def index():
    db.create_all()

    t1 = Hashtag(tag='Max')
    t2 = Hashtag(tag='Ben')
    t3 = Hashtag(tag='Andy')

    db.session.add_all([t1, t2])
    db.session.commit()

    p1 = Post(title='Post_1')
    p2 = Post(title='Post_2')
    p3 = Post(title='Post_3')

    p1.post_tag_rel = [t1, t2, t3]
    p2.post_tag_rel = [t1, t2]
    p3.post_tag_rel = [t1]

    db.session.add_all([p1, p2, p3])
    db.session.commit()

    return 'ok'


@app.route('/posts', methods=['GET'])
def get_all_post():

    post_datas = []

    querys = Post.query.all()
    # querys = Post.query.options(joinedload("post_tag_rel")).all()

    for query in querys:
        post_dict = {
            'id': query.id,
            'title': query.title,
            'tags': [tags.tag for tags in query.post_tag_rel]
        }
        post_datas.append(post_dict)

    return jsonify(post_datas), 200


@app.route('/post/<int:id>', methods=['GET'])
def get_post_by_id(id):
    query = Post.query.filter_by(id=id).first()

    return jsonify({
        'id': query.id,
        'title': query.title,
        'tags': [tags.tag for tags in query.post_tag_rel]
    })


if __name__ == "__main__":
    app.run(debug=True)
