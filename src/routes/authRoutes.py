from flask import Blueprint, jsonify, request, redirect, url_for
from flask_login import login_user, logout_user, login_required, LoginManager
from flask_cors import cross_origin


auth = Blueprint('auth', __name__)



