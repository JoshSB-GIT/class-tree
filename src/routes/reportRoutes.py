import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from sklearn import metrics
from flask import Blueprint, jsonify, request, abort
from flask_cors import cross_origin
from flask_login import login_required
from utils.filestools import FilesTools
import os

_filetools = FilesTools()
_path_img = './src/assets/img/'
category_cols = ['fixed acidity', 'citric acid', 'residual sugar',
                 'free sulfur dioxide', 'pH', 'alcohol']

def save_img(name: str):
    file_name = ''+_filetools.generate_file_hash(name)
    plt.savefig(_path_img+file_name)


def boxplot_graph(data_frame, category_cols):
    sns.boxplot(data=data_frame[category_cols])
    save_img('boxplot')


def bar_graph(column: str, data_frame):
    plt.figure(figsize=(10, 6))
    sns.barplot(x='quality', y=column, data=data_frame)
    save_img('bar_graph')

csv_report = Blueprint('csv_report', __name__)
# learningmachine123
# ufvvcvghcvryxhpl

@cross_origin
@csv_report.route('/generate_report', methods=['POST'])
@login_required
def generate_report_csv():
    path_temp = './src/temp/'
    if request.method == 'POST':
        if 'wine_red' not in request.files:
            abort(400, jsonify({'message': 'Not file uploaded!'}))
            
        file = request.files['wine_red']
        
        if file.filename == '':
            abort(400, jsonify({'message': 'Invalid name file'}))

        new_filename = _filetools.generate_file_hash(file.filename)
        save_temp = os.path.join(path_temp, new_filename)
        file.save(save_temp)
        wine_data = pd.read_csv(save_temp,
                        sep=';', engine='python',
                        skiprows=0, index_col=False)
        wine_data.dropna(inplace=True)
        wine_data.drop_duplicates(inplace=True)

    return jsonify({'message': 'Hola!'})
