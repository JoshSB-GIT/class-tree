from flask import Blueprint, jsonify, request
from flask_cors import cross_origin
import yagmail
from models.emailModel import emailModel

from models.userModel import User

mail = Blueprint('mail', __name__)
# learningmachine123
# ufvvcvghcvryxhpl


@cross_origin
@mail.route('/send_email', methods=['POST'])
def send_email_to():
    response = {}
    email = request.json['email']
    password = request.json['password']
    email_to = request.json['email_to']
    subject = request.json['subject']
    text = request.json['text']
    try:
        user = User(password=password,
                    email=email)
        mail = emailModel(email_to=email_to, subject=subject,
                          text=text)
        yag = yagmail.SMTP(user=user.email, password=user.password)
        response = {'message': 'Email send',
                    'status_code': 200,
                    'data': {
                        'email': user.email,
                        'password': user.password,
                        'email_to': mail.email_to,
                        'subject': mail.subject,
                        'text': mail.text}
                    }
        yag.send(email_to, subject, text)
    except Exception as ex:
        response = {'error': 'check your credentials',
                    'exception': str(ex),
                    'status_code': 400}

    return jsonify(response)
