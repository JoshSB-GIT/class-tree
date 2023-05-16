from routes.reportRoutes import csv_report
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from flask_login import current_user, login_required, login_user, logout_user
from flask_login import LoginManager
from supabase import create_client, Client
from config.config import config
from models.userModel import User

app = Flask(__name__)
CORS(app)

app.register_blueprint(csv_report)

supabase: Client = (
    create_client(config['development'].supabase_url,
                      config['development'].supabase_key))
login_manager = LoginManager()
login_manager.init_app(app)

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

        try:
            account = supabase.auth.sign_in_with_password({
                'email':str(email),
                'password':str(password)})
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
                    'status_code': 200}

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
    except:
        response = {
            'message': (
                'An error occurred while trying to extract user information'),
            'status_code': 400,
            'status': False}
        
    return jsonify(response)
