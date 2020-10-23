from flask import Flask, render_template, jsonify, request, session, redirect, url_for, Blueprint

main = Blueprint('main', __name__)


@main.route('/')
def do_some_thing():
    return render_template('index.html')