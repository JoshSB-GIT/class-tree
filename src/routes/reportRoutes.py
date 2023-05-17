import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import (
    train_test_split)
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from sklearn import metrics
from flask import Blueprint, jsonify, request, abort
from flask_cors import cross_origin
from flask_login import login_required
from utils.csvtools import CsvTools
import os

def principal_graph(data_frame, category_cols):
    sns.boxplot(data=data_frame[category_cols])

    plt.savefig('./src/assets/img/imgcaja-bigote.png')
    return plt.show()


def sub_level_graph(data_frame, category_cols):
    fig, ax = plt.subplots(nrows=6, ncols=1, figsize=(10, 30))
    fig.subplots_adjust(hspace=1)

    for i, col in enumerate(category_cols):
        sns.countplot(x=col, data=data_frame, ax=ax[i])
        ax[i].set_title(col)
        ax[i].set_xticklabels(ax[i].get_xticklabels(), rotation=30)

    return plt.show()


def histo_graph(data_frame, category_cols):
    sns.histplot(data=data_frame, x=category_cols[5],
                 hue="quality", kde=True)

    return plt.show()


def bar_diagram_graph(vs_var: str, data_frame):
    plt.figure(figsize=(10, 6))
    sns.barplot(x='quality', y=vs_var, data=data_frame)
    print(data_frame[vs_var])
    return plt.show()


def bar_simple_graph(data_frame, column):
    plt.figure(figsize=(10, 6))
    sns.countplot(x=data_frame[column])

    return plt.show()

csv_report = Blueprint('csv_report', __name__)
# learningmachine123
# ufvvcvghcvryxhpl

@cross_origin
@csv_report.route('/generate_report', methods=['POST'])
@login_required
def generate_report_csv():
    csvtools = CsvTools()
    path_temp = './src/temp/'
    if request.method == 'POST':
        if 'wine_red' not in request.files:
            abort(400, jsonify({'message': 'Not file uploaded!'}))
            
        file = request.files['wine_red']
        
        if file.filename == '':
            abort(400, jsonify({'message': 'Invalid name file'}))

        new_filename = csvtools.generate_file_hash(file.filename)
        save_temp = os.path.join(path_temp, new_filename)
        file.save(save_temp)
        wine_data = pd.read_csv(save_temp,
                        sep=';', engine='python',
                        skiprows=0, index_col=False)
        wine_data.dropna(inplace=True)
        wine_data.drop_duplicates(inplace=True)
        
        principal_graph(wine_data, 'pH')
        print(wine_data)
    return jsonify({'message': 'Hola!'})
