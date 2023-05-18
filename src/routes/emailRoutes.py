from flask import Blueprint, jsonify, request
from flask_cors import cross_origin
from datetime import datetime
from config.config import config
from models.emailModel import emailModel
from models.userModel import User
import utils.varsTools as vars
import yagmail


mail = Blueprint('mail', __name__)
# learningmachine123
# ufvvcvghcvryxhpl


@cross_origin
@mail.route('/send_email', methods=['POST'])
def send_email_to():
    response = {}
    email_user = request.json['email_user']
    email_to = request.json['email_to']
    subject = request.json['subject']
    email_content = request.json['email_content']
    user_send_contact = request.json['user_send_contact']
    try:
        user = User(password=config['development'].PASS_EMAIL,
                    email=config['development'].USER_EMAIL)
        if user_send_contact:
            email_to = config['development'].USER_EMAIL
            mail = emailModel(email_to=email_to, subject=subject,
                              text=email_content)
            yag = yagmail.SMTP(user=user.email, password=user.password)

            yag.send(
                email_user, 'Lo hemos recibido...',
                str(vars.email_we_to_user).format(
                    str(datetime.now().date()), str(datetime.now().time())))
            response = {'message': 'Email received',
                        'status_code': 200,
                        'data': {
                            'email': email_user,
                            'email_to': mail.email_to,
                            'subject': mail.subject,
                            'text': mail.text}
                        }
        else:
            mail = emailModel(email_to=email_to, subject=subject,
                              text=email_content)
            yag = yagmail.SMTP(user=user.email, password=user.password)
            yag.send(email_to, subject, email_content)

            response = {'message': 'Email send.',
                        'status_code': 200,
                        'data': {
                            'email': user.email,
                            'password': user.password,
                            'email_to': mail.email_to,
                            'subject': mail.subject,
                            'text': mail.text}
                        }
    except Exception as ex:
        response = {'error': 'An error occurred while submitting the request.',
                    'exception': str(ex),
                    'status_code': 400}

    return jsonify(response)
