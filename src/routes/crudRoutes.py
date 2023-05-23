from flask import Blueprint, jsonify, make_response, request
from flask_cors import cross_origin
from flask_login import login_required
from supabase import create_client, Client
from config.config import config
from utils.validations import Validations

crud = Blueprint('crud', __name__)

supabase: Client = create_client(config['development'].supabase_url,
                                 config['development'].supabase_key)

val = Validations()


@cross_origin
@crud.route('/list_data', methods=['GET'])
@login_required
def list_data():
    try:
        data = supabase.table('data').select('*').execute()
    except Exception as ex:
        data = {'error': str(ex)}
        return make_response(
            jsonify(
                data), 400)

    return data.dict()


@cross_origin
@crud.route('/list_data/for_id/<id>', methods=['GET'])
@login_required
def list_data_id(id):

    if not id:
        return make_response(
            jsonify(
                {'message': 'Bad id recived'}), 400)

    try:
        data = supabase.table('data').select(
            '*').eq('id', id).execute()
        data = data.dict()
    except Exception as ex:
        data = {'error': (ex)}
        make_response(
            jsonify(
                data, 400))

    return data


@cross_origin
@crud.route('/list_data/for_id', methods=['POST'])
@login_required
def list_data_id_post():
    if request.method == 'POST':
        try:
            id = request.json['id']
            if not id:
                return make_response(
                    jsonify(
                        {'message': 'Bad id recived'}), 400)
            data = supabase.table('data').select(
                '*').eq('id', id).execute()
            data = data.dict()
        except Exception as ex:
            data = {'error': str(ex)}
            return make_response(
                jsonify(
                    data), 400)

        return data


@cross_origin
@crud.route('/list_csv', methods=['GET'])
@login_required
def list_csv():
    try:
        data = supabase.table('csv').select(
            '*').execute()
        data = data.dict()
    except Exception as ex:
        data = {'error': str(ex)}
        return make_response(
            jsonify(
                data), 400)
    return data


@cross_origin
@crud.route('/list_csv/for_id/<id>', methods=['GET'])
@login_required
def list_csv_id(id):
    if not id:
        return make_response(
            jsonify(
                {'message': 'Bad id recived'}), 400)
    try:
        data = supabase.table('csv').select(
            '*').eq('id', id).execute()
        data = data.dict()
    except Exception as ex:
        data = {'error': str(ex)}
        return make_response(
            jsonify(
                data), 400)
    return data


@cross_origin
@crud.route('/list_csv/for_id', methods=['POST'])
@login_required
def list_csv_id_post():
    if request.method == 'POST':
        try:
            id = request.json['id']
            if not id:
                return make_response(
                    jsonify(
                        {'message': 'Bad id recived'}), 400)
            data = supabase.table('csv').select(
                '*').eq('id', id).execute()
            data = data.dict()
        except Exception as ex:
            data = {'error': str(ex)}
            return make_response(
                jsonify(
                    data), 400)
        return data


@cross_origin
@crud.route('/list_contact', methods=['GET'])
@login_required
def list_contact():
    try:
        data = supabase.table('contact').select(
            '*').eq('state', False).execute()
        data = data.dict()
    except Exception as ex:
        data = {'error': str(ex)}
        return make_response(
            jsonify(
                data), 400)
    return data


@cross_origin
@crud.route('/list_contact/for_id/<id>', methods=['GET'])
@login_required
def list_contact_id(id):
    if not id:
        return make_response(
            jsonify(
                {'message': 'Bad id recived'}), 400)
    try:
        data = supabase.table('contact').select(
            '*').eq('id', id).eq('state', False).execute()
        data = data.dict()
    except Exception as ex:
        data = {'error': str(ex)}
        return make_response(
            jsonify(
                data), 400)
    return data


@cross_origin
@crud.route('/list_contact/for_id', methods=['POST'])
@login_required
def list_contact_id_post():
    if request.method == 'POST':
        try:
            id = request.json['id']
            if not id:
                return make_response(
                    jsonify(
                        {'message': 'Bad id recived'}), 400)
            data = supabase.table('contact').select(
                '*').eq('id', id).eq('state', False).execute()
            data = data.dict()
        except Exception as ex:
            data = {'error': str(ex)}
            make_response(
                jsonify(
                    data, 400))
        return data


@cross_origin
@crud.route('/list_dataset', methods=['GET'])
@login_required
def list_dataset():
    try:
        data = supabase.table('dataset').select(
            '*').execute()
        data = data.dict()
    except Exception as ex:
        data = {'error': str(ex)}
        make_response(
            jsonify(
                data, 400))
    return data


@cross_origin
@crud.route('/list_dataset/for_id/<id>', methods=['GET'])
@login_required
def list_dataset_id(id):
    if not id:
        return make_response(
            jsonify(
                {'message': 'Bad id recived'}), 400)
    try:
        data = supabase.table('dataset').select(
            '*').eq('id', id).execute()
        data = data.dict()
    except Exception as ex:
        data = {'error': str(ex)}
        make_response(
            jsonify(
                data, 400))
    return data


@cross_origin
@crud.route('/list_dataset/for_id', methods=['POST'])
@login_required
def list_dataset_id_post():
    if request.method == 'POST':
        try:
            id = request.json['id']
            if not id:
                return make_response(
                    jsonify(
                        {'message': 'Bad id recived'}), 400)
            data = supabase.table('dataset').select(
                '*').eq('id', id).execute()
            data = data.dict()
        except Exception as ex:
            data = {'error': str(ex)}
            make_response(
                jsonify(
                    data, 400))
        return data


@cross_origin
@crud.route('/delete_dataset_id/for_id', methods=['POST'])
@login_required
def delete_dataset_id():
    if request.method == 'POST':
        try:
            id = request.json['id']
            if not id:
                return make_response(
                    jsonify(
                        {'message': 'Bad id recived'}), 400)
            data = supabase.table("dataset").delete().eq("id", id).execute()
            data = data.dict()
        except Exception as ex:
            data = {'error': str(ex)}
            make_response(
                jsonify(
                    data, 400))
        return data


@cross_origin
@crud.route('/delete_csv_id/for_id', methods=['POST'])
@login_required
def delete_csv_id():
    if request.method == 'POST':
        try:
            id = request.json['id']
            if not id:
                return make_response(
                    jsonify(
                        {'message': 'Bad id recived'}), 400)
            data = supabase.table("csv").delete().eq("id", id).execute()
            data = data.dict()
        except Exception as ex:
            data = {'error': str(ex)}
            make_response(
                jsonify(
                    data, 400))
        return data


@cross_origin
@crud.route('/delete_data_id/for_id', methods=['POST'])
@login_required
def delete_data_id():
    if request.method == 'POST':
        try:
            id = request.json['id']
            if not id:
                return make_response(
                    jsonify(
                        {'message': 'Bad id recived'}), 400)
            data = supabase.table("data").delete().eq("id", id).execute()
            data = data.dict()
        except Exception as ex:
            data = {'error': str(ex)}
            make_response(
                jsonify(
                    data, 400))
        return data


@cross_origin
@crud.route('/delete_contact_id/for_id', methods=['POST'])
@login_required
def delete_contact_id():
    if request.method == 'POST':
        try:
            id = request.json['id']
            if not id:
                return make_response(
                    jsonify(
                        {'message': 'Bad id recived'}), 400)
            data = supabase.table("contact").delete().eq("id", id).execute()
            data = data.dict()
        except Exception as ex:
            data = {'error': str(ex)}
            make_response(
                jsonify(
                    data, 400))
        return data


@cross_origin
@crud.route('/delete_dataset_id/for_id/<id>', methods=['GET'])
@login_required
def delete_dataset_id_get(id):
    try:
        if not id:
            return make_response(
                jsonify(
                    {'message': 'Bad id recived'}), 400)
        data = supabase.table("dataset").delete().eq("id", id).execute()
        data = data.dict()
    except Exception as ex:
        data = {'error': str(ex)}
        make_response(
            jsonify(
                data, 400))
    return data


@cross_origin
@crud.route('/delete_data_id/for_id/<id>', methods=['GET'])
@login_required
def delete_data_id_get(id):
    try:
        if not id:
            return make_response(
                jsonify(
                    {'message': 'Bad id recived'}), 400)
        data = supabase.table("data").delete().eq("id", id).execute()
        data = data.dict()
    except Exception as ex:
        data = {'error': str(ex)}
        make_response(
            jsonify(
                data, 400))
    return data


@cross_origin
@crud.route('/delete_csv_id/for_id/<id>', methods=['GET'])
@login_required
def delete_csv_id_get(id):
    try:
        if not id:
            return make_response(
                jsonify(
                    {'message': 'Bad id recived'}), 400)
        data = supabase.table("csv").delete().eq("id", id).execute()
        data = data.dict()
    except Exception as ex:
        data = {'error': str(ex)}
        make_response(
            jsonify(
                data, 400))
    return data


@cross_origin
@crud.route('/delete_contact_id/for_id/<id>', methods=['GET'])
@login_required
def delete_contact_id_get(id):
    try:
        if not id:
            return make_response(
                jsonify(
                    {'message': 'Bad id recived'}), 400)
        data = supabase.table("contact").delete().eq("id", id).execute()
        data = data.dict()
    except Exception as ex:
        data = {'error': str(ex)}
        make_response(
            jsonify(
                data, 400))
    return data


@cross_origin
@crud.route('/delete_dataset_id/for_csv_id/<csv_id>', methods=['GET'])
@login_required
def delete_dataset_csv_id_get(csv_id):
    try:
        if not csv_id:
            return make_response(
                jsonify(
                    {'message': 'Bad id recived'}), 400)
        data = supabase.table("dataset").delete().eq(
            "csv_id", csv_id).execute()
        data = data.dict()
    except Exception as ex:
        data = {'error': str(ex)}
        make_response(
            jsonify(
                data, 400))
    return data


@cross_origin
@crud.route('/delete_data_id/for_csv_id/<csv_id>', methods=['GET'])
@login_required
def delete_data_csv_id_get(csv_id):
    try:
        if not csv_id:
            return make_response(
                jsonify(
                    {'message': 'Bad id recived'}), 400)
        data = supabase.table("data").delete().eq("csv_id", csv_id).execute()
        data = data.dict()
    except Exception as ex:
        data = {'error': str(ex)}
        make_response(
            jsonify(
                data, 400))
    return data


@cross_origin
@crud.route('/delete_data_id/for_csv_id', methods=['POST'])
@login_required
def delete_data_csv_id():
    if request.method == 'POST':
        try:
            csv_id = request.json['csv_id']
            if not csv_id:
                return make_response(
                    jsonify(
                        {'message': 'Bad id recived'}), 400)
            data = supabase.table("data").delete().eq(
                "csv_id", csv_id).execute()
            data = data.dict()
        except Exception as ex:
            data = {'error': str(ex)}
            make_response(
                jsonify(
                    data, 400))
        return data


@cross_origin
@crud.route('/delete_dataset_id/for_csv_id', methods=['POST'])
@login_required
def delete_dataset_csv_id():
    if request.method == 'POST':
        try:
            csv_id = request.json['csv_id']
            if not csv_id:
                return make_response(
                    jsonify(
                        {'message': 'Bad id recived'}), 400)
            data = supabase.table("dataset").delete().eq(
                "csv_id", csv_id).execute()
            data = data.dict()
        except Exception as ex:
            data = {'error': str(ex)}
            make_response(
                jsonify(
                    data, 400))
        return data
