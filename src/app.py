from routes.reportRoutes import csv_report
from routes.emailRoutes import mail
from routes.neuronaRoutes import neuro
from routes.crudRoutes import crud
from flask import Flask, jsonify, make_response, request, send_from_directory
from flask_cors import CORS, cross_origin
from flask_login import current_user, login_required, login_user, logout_user
from flask_login import LoginManager
from supabase import create_client, Client
from config.config import config
from utils.validations import Validations
from models.userModel import User
import os

app = Flask(__name__)
CORS(app)

app.register_blueprint(csv_report)
app.register_blueprint(mail)
app.register_blueprint(neuro)
app.register_blueprint(crud)

supabase: Client = (
    create_client(config['development'].supabase_url,
                  config['development'].supabase_key))
login_manager = LoginManager()
login_manager.init_app(app)

val = Validations()


@cross_origin
@app.route('/')
@login_required
def home():
    return jsonify({'message': 'welcome home!'})


@login_manager.user_loader
def load_user(user_id):
    return User(user_id, "")


@cross_origin
@app.route('/login', methods=['GET', 'POST'])
def login():
    response = {}
    if request.method == 'POST':
        email = request.json['email']
        password = request.json['password']

        if type(email) != str or type(password) != str:
            return make_response(
                jsonify(
                    {'message': 'Password and email must be text'}), 400)

        if not val.valide_email(email):
            return make_response(
                jsonify(
                    {'message': 'Bad email strucure'}), 400)

        if len(password) < 8 and not len(password) > 20:
            return make_response(
                jsonify(
                    {'message': 'The password must be between 8 and 20 '
                     + 'characters.'}), 400)

        try:
            account = supabase.auth.sign_in_with_password({
                'email': str(email),
                'password': str(password)})
            account_dict = account.dict()
            user = User(id=account_dict['user']['id'],
                        email=account_dict['user']['email'])
            login_user(user)
            response = {'message': 'User Found!',
                        'email': str(user.email),
                        'id': str(user.id),
                        'status_code': 200}
        except Exception as ex:
            response = {'error': str(ex),
                        'status_code': 400}

    return jsonify(response)


@app.route('/create_user', methods=['POST'])
@login_required
def create_user():
    response = {}
    email = request.json['email']
    password = request.json['password']

    if type(email) != str or type(password) != str:
        return make_response(
            jsonify(
                {'message': 'Password and email must be text'}), 400)

    if not val.valide_email(email):
        return make_response(
            jsonify(
                {'message': 'Bad email strucure'}), 400)

    if not val.valide_password(password):
        return make_response(
            jsonify(
                {'message': 'The password must be between 8 and 20 '
                 + 'characters and must not contain special characters'}), 400)

    try:
        user = User(email=email, password=password)

        supabase.auth.sign_up({'email': str(user.email),
                               'password': str(user.password)})
        response = {'message': 'User Created!',
                    'email': str(user.email),
                    'status_code': 200}
    except Exception as ex:
        response = {'error': str(ex),
                    'status_code': 400}

    return jsonify(response)


@app.route('/logout')
@login_required
def logout():
    response = {}
    try:
        logout_user()
        supabase.auth.sign_out()
        response = {'message': 'you have successfully logged out!',
                    'status_code': 200}
    except Exception as ex:
        response = {'error': str(ex),
                    'status_code': 400}
        make_response(response, 400)

    return jsonify(response)


@app.route('/is_auth')
def id_user_auth():
    response = {}
    try:
        if current_user.is_authenticated:
            user_info = supabase.auth.get_session().dict()
            response = {'message': 'user is in session',
                        'user': {
                            'id': str(user_info['user']['id']),
                            'email': str(user_info['user']['email'])
                        },
                        'status_code': 200,
                        'status': True}
        else:
            response = {'message': 'user not in session',
                        'status_code': 200,
                        'status': False}
    except Exception as ex:
        response = {
            'message': (
                'An error occurred while trying to extract user information'),
            'exception': str(ex),
            'status_code': 400,
            'status': False}
        make_response(response, 400)

    return jsonify(response)


@app.route('/img/<filename>')
def serve_image(filename):
    try:
        img_folder = os.path.join(app.root_path, 'assets/img')
    except Exception as ex:
        make_response({'error': str(ex),
                       'status': 400}, 400)
    return send_from_directory(img_folder, filename)
