from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)


@cross_origin
@app.route('/')
def home():
    return jsonify({'message': '¡Welcome!'})
