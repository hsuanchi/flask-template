from flask import Flask, render_template, jsonify, request, session, redirect, Blueprint

from ..model import user
from .. import db

auth = Blueprint('auth', __name__)


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']

        try:
            U = user.User(email, password)
            U.save_to_db()
            U.save_user_session()

            return jsonify({'msg': 'registration success'}), 200
        except Exception as e:
            print(e)
            return jsonify({'msg': 'Repeat registration'}), 400

    else:
        return render_template('signup.html')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']

        query = user.User.get_user(email)
        if query != None and query.verify_password(password):
            query.save_user_session()
            return jsonify({'msg': 'ok'}), 200
        else:
            return jsonify({'msg': 'incorrect username or password'}), 400

    else:
        return render_template('login.html')


@auth.route('/logout', methods=['POST'])
def logout():
    user.User.remove_user_session()
    return jsonify({'msg': 'logout'}), 200
