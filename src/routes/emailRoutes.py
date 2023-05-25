from flask import Blueprint, jsonify, make_response, request
from flask_cors import cross_origin
from datetime import datetime
from config.config import config
from models.emailModel import emailModel
from supabase import create_client, Client
from models.userModel import User
import utils.varsTools as vars
from utils.validations import Validations
import yagmail


mail = Blueprint('mail', __name__)

supabase: Client = create_client(config['development'].supabase_url,
                                 config['development'].supabase_key)

val = Validations()


@cross_origin
@mail.route('/send_email', methods=['POST'])
def send_email_to():
    response = {}
    data = {}
    email_user = request.json['email_user']
    email_to = request.json['email_to']
    subject = request.json['subject']
    email_content = request.json['email_content']
    user_send_contact = request.json['user_send_contact']

    if (type(email_user) != str or type(email_to) != str
            or type(subject) != str or type(email_content) != str
            or type(user_send_contact) != bool):
        return make_response(
            jsonify(
                {'message': 'Invalid type data in variables'}), 400)

    if not val.valide_email(email_user) or not val.valide_email(email_to):
        return make_response(
            jsonify(
                {'message': 'Bad email strucure'}), 400)

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
                            'text': mail.text
                        }}

            data = {
                'msg': str(email_content),
                'user_email': str(email_user),
                'email_to': str(config['development'].USER_EMAIL),
                'subject': str(subject),
                'user_send_contact': True
            }

            supabase.table('contact').insert(data).execute()

        else:
            mail = emailModel(email_to=email_to, subject=subject,
                              text=email_content)
            yag = yagmail.SMTP(user=user.email, password=user.password)
            yag.send(email_to, subject, email_content)

            data = {
                'msg': str(email_content),
                'user_email': str(email_user),
                'email_to': str(email_user),
                'subject': str(subject),
                'state': True,
                'user_send_contact': False
            }

            supabase.table('contact').insert(data).execute()

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


@cross_origin
@mail.route('/update_status/<id>')
def update_status(id):

    if not id:
        return make_response(
            jsonify(
                {'message': 'Bad id recived'}), 400)

    try:
        data = supabase.table('contact').select(
            '*').eq('id', id).execute()
        data = data.dict()
        status = data['data'][0]['state']
        if status:
            supabase.table('contact').update(
                {'state': False}).eq('id', id).execute()
        else:
            supabase.table('contact').update(
                {'state': True}).eq('id', id).execute()

        return make_response(
            jsonify({'message': 'status updated'}), 200)
    except Exception as ex:
        return make_response(
            jsonify({'error': str(ex)}), 400)
