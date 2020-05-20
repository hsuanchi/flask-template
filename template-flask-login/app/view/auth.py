from flask import Flask, render_template, request, session, Blueprint, make_response
from flask_restful import Api, Resource, reqparse

from marshmallow import ValidationError

from ..model import user
from .. import db

auth = Blueprint('auth', __name__)
api = Api(auth)

users_schema = user.UserSchema()


class Signup(Resource):
    def post(self):
        try:
            # 資料驗證
            user_data = users_schema.load(request.form, partial=True)
            name = user_data['name']
            password = user_data['password']

            # 註冊
            U = user.User(name, password)
            U.save_to_db()
            U.save_user_session()

            return {'msg': 'registration success'}, 200

        except ValidationError as error:
            return {'errors': '資料驗證失敗', 'msg': str(error)}, 400

        except Exception as e:
            print(e)
            return {'msg': 'Repeat registration'}, 400

    def get(self):
        return make_response(render_template('signup.html'))


class Login(Resource):
    def post(self):
        try:
            # 資料驗證
            user_data = users_schema.load(request.form)
            name = user_data['name']
            password = user_data['password']

            # 登入
            query = user.User.get_user(name)
            if query != None and query.verify_password(password):
                query.save_user_session()
                return {'msg': 'ok'}, 200
            else:
                return {'msg': 'incorrect username or password'}, 400

        except ValidationError as error:
            return {'errors': '資料驗證失敗', 'msg': str(error)}, 400

    def get(self):
        return make_response(render_template('login.html'))


class Logout(Resource):
    def post(self):
        user.User.remove_user_session()
        return {'msg': 'logout'}, 200


api.add_resource(Signup, '/signup')
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')
