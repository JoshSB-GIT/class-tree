from flask import Blueprint, jsonify, request
from flask_cors import cross_origin

mail = Blueprint('mail', __name__)
# learningmachine123
# ufvvcvghcvryxhpl

@cross_origin
@mail.route('/send_email', methods=['POST'])
def send_email_to():
    return jsonify({'message': 'Hola!'})