from flask import request,jsonify
from flask_restful import Api, Resource, reqparse

from marshmallow import ValidationError

from flask_jwt_extended import (create_access_token,
                                jwt_refresh_token_required,
                                create_refresh_token, get_jwt_identity,
                                fresh_jwt_required,set_refresh_cookies)

from ...model import users
from ... import db
from . import api

api = Api(api)
users_schema = users.UserSchema()


class Signup(Resource):
    def post(self):
        try:
            # 資料驗證
            user_data = users_schema.load(request.json, partial=True)
            name = user_data['name']
            password = user_data['password']

            # 註冊帳戶
            U = users.User(name, password)
            U.save_to_db()
            return create_jwt(name), 200

        except ValidationError as error:
            return {'errors': '資料驗證失敗', 'msg': str(error)}, 400

        except Exception as e:
            print(e)
            return {'msg': '重複註冊'}, 400


class Login(Resource):
    def post(self):
        try:
            # 資料驗證
            user_data = users_schema.load(request.form)
            name = user_data['name']
            password = user_data['password']

            # 登入
            query = users.User.get_user(name=name)
            if query != None and query.verify_password(password):
                return create_jwt(name)
            else:
                return {'msg': '帳密錯誤'}, 400

        except ValidationError as error:
            return {'errors': '資料驗證失敗', 'msg': str(error)}, 400


class JWT_refresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user)
        return {'access_token': new_token}


def create_jwt(name):
    refresh_token = create_refresh_token(identity=name)
    access_token = create_access_token(identity=name)

    # recommend frontend save access_token in memery
    response = jsonify({
        'msg': 'ok',
        'access_token': access_token,
    })
    # Set refresh_token in cookie & remember use httponly
    set_refresh_cookies(response,refresh_token)
    return response


api.add_resource(Signup, '/signup')
api.add_resource(Login, '/login')
api.add_resource(JWT_refresh, '/refresh')
