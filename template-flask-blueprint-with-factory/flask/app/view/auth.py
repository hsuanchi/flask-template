from flask import jsonify, request, Blueprint, url_for, redirect, abort, make_response

auth = Blueprint('autha', __name__)


@auth.route('/')
def index():
    return 'welcome'