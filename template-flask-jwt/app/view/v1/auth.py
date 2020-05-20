from flask import request
from flask_restful import Api, Resource, reqparse

from marshmallow import ValidationError

from flask_jwt_extended import (create_access_token,
                                jwt_refresh_token_required,
                                create_refresh_token, get_jwt_identity,
                                fresh_jwt_required)

from ...model import users
from ... import db
from . import api

api = Api(api)
users_schema = users.UserSchema()


class Signup(Resource):
    def post(self):
        # 資料驗證
        try:
            user_data = users_schema.load(request.json, partial=True)
            name = user_data['name']
            password = user_data['password']
        except ValidationError as error:
            return {'errors': '資料驗證失敗', 'msg': str(error)}, 400

        # 註冊帳戶
        try:
            U = users.User(name, password)
            U.save_to_db()
            return create_jwt(name), 200
        except Exception as e:
            print(e)
            return {'msg': '重複註冊'}, 400


class Login(Resource):
    def post(self):
        # 資料驗證
        try:
            user_data = users_schema.load(request.json)
            name = user_data['name']
            password = user_data['password']
        except ValidationError as error:
            return {'errors': '資料驗證失敗', 'msg': str(error)}, 400

        # 登入
        query = users.User.get_user(name=name)
        if query != None and query.verify_password(password):
            return create_jwt(name), 200
        else:
            return {'msg': '帳密錯誤'}, 400


class JWT_refresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user)
        return {'access_token': new_token}


def create_jwt(name):
    response = {
        'msg': 'ok',
        'access_token': create_access_token(identity=name),
        'refresh_token': create_refresh_token(identity=name)
    }
    return response


api.add_resource(Signup, '/signup')
api.add_resource(Login, '/login')
api.add_resource(JWT_refresh, '/refresh')
