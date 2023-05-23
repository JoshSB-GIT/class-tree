from routes.principalControlador import Controlador
from routes.modeloControlador import Modelo as CrearModelo
from routes.responseController import Response_controller
from flask import Blueprint, jsonify, make_response, request
from flask_cors import cross_origin
import numpy as np

neuro = Blueprint('neuro', __name__)
_path_img = './src/assets/img/'


@cross_origin
@neuro.route('/get_hypotenuse', methods=['POST'])
def hypotenuse():
    if request.method == 'POST':
        response = {}
        try:
            hick = request.json['hick']
            hick2 = request.json['hick2']
            np.array([(hick, hick2)])
            modelo = CrearModelo()
            response_controller = Response_controller(hick, hick2)
            controlador = Controlador(modelo, response_controller)
            response = {'data': str(controlador.ejecutar()),
                        'img': 'http://127.0.0.1:5000/img/graph_neuro.png'}

        except Exception as ex:
            return make_response({'data': str(ex)}, 400)

    return jsonify(response)
