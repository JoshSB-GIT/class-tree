from flask import Blueprint, jsonify, request
from flask_cors import cross_origin
from flask_login import login_required

csv_report = Blueprint('csv_report', __name__)


@cross_origin
@csv_report.route('/generate_report', methods=['POST'])
@login_required
def generate_report_csv():
    return jsonify({'message': 'Hola!'})