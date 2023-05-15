from flask import Flask, jsonify, redirect, request, url_for
from flask_cors import CORS, cross_origin
from flask_login import current_user, login_required, login_user, logout_user
from flask_login import LoginManager
import supabase_py as spb
from config.config import config
from models.userModel import User

app = Flask(__name__)
CORS(app)
supabase = (
    spb.create_client(config['development'].supabase_url,
                      config['development'].supabase_key))
login_manager = LoginManager()
login_manager.init_app(app)


@cross_origin
@app.route('/')
@login_required
def home():
    user_id = current_user.id
    return jsonify({'message': 'welcome home!',
                    'data': str(user_id)})


@login_manager.user_loader
def load_user(user_id):
    return User(user_id, "")


@cross_origin
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.json['email']
        password = request.json['password']

        response = supabase.auth.sign_in(email=email, password=password)
        if response['status_code'] == 200:
            user_data = response['user']
            user = User(user_data['id'], user_data['email'])
            login_user(user)
            return response
        else:
            error_message = response['error']['message']
            return jsonify({'mesage': str(error_message)})

    return jsonify({'message': 'HELLO!!'})


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
