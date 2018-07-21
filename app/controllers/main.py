from flask import Blueprint, render_template, flash, request, redirect, url_for, jsonify
from flask_login import login_user, logout_user, login_required

from app.extensions import cache
from app.models import User

main = Blueprint('main', __name__)


@main.route('/')
@cache.cached(timeout=1000)
def home():
    return jsonify('home')


@main.route("/login", methods=["GET", "POST"])
def login():
    form = request.get_json()
    user = User.query.filter_by(username=form['username']).one()
    if user.check_password(form['password']):
        login_user(user)
        return jsonify(status=True, message='Logged in successfully.')
    else:
        return jsonify(status=False, message='Invalid username or password.')


@main.route("/logout")
def logout():
    logout_user()
    return jsonify(status=True, message='You have been logged out.')


@main.route("/restricted")
@login_required
def restricted():
    return jsonify(status=True, message='"You can only see this if you are logged in!"')
