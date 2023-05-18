import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from sklearn import metrics
from flask import Blueprint, jsonify, request, send_file
from flask_cors import cross_origin
from flask_login import login_required
from utils.filestools import FilesTools
from utils.pdftools import PdfTools
import utils.varsTools as vars
from datetime import datetime
import os

plt.switch_backend('agg')

csv_report = Blueprint('csv_report', __name__)

_pdf = PdfTools(orientation='P', unit='mm', format='A4')
_filetools = FilesTools()
_path_img = './src/assets/img/'
_path_temp = './src/temp/'
category_cols = ['volatile acidity', 'citric acid', 'chlorides',
                 'free sulfur dioxide', 'sulphates', 'alcohol']


def save_img(name: str) -> str:
    file_name = ''+_filetools.generate_file_hash(name.replace(' ', ''))
    plt.savefig(_path_img+file_name)
    return str(_path_img+file_name+'.png')


def boxplot_graph(data_frame, column: str) -> str:
    sns.boxplot(data=data_frame[column], orient='h')
    plt.title(column)
    return save_img('boxplot-'+str(column))


def bar_diagram_graph(column: str, data_frame):
    plt.figure(figsize=(10, 6))
    sns.barplot(x='quality', y=column, data=data_frame)
    return save_img('bar_graph-'+str(column))


# learningmachine123
# ufvvcvghcvryxhpl


@cross_origin
@csv_report.route('/generate_report', methods=['POST'])
@login_required
def generate_report_csv():
    path_temp = './src/temp/'
    if request.method == 'POST':
        # try:
        file = request.files['wine_red']

        new_filename = _filetools.generate_file_hash(file.filename)
        save_temp = os.path.join(path_temp, new_filename)
        print(save_temp, '\n\n')
        file.save(save_temp)
        wine_data = pd.read_csv(save_temp,
                                sep=';', engine='python',
                                skiprows=0, index_col=False)

        boxplot_routes = []
        for col in category_cols:
            boxplot_routes.append(boxplot_graph(wine_data, col))

        wine_data.dropna(inplace=True)
        wine_data.drop_duplicates(inplace=True)

        bargraph_routes = []

        for col in category_cols:
            bargraph_routes.append(bar_diagram_graph(col, wine_data))

        wine_data['quality'] = wine_data['quality'].apply(
            lambda x: 1 if x > 6.5 else 0)

        X = wine_data.iloc[:, :-1].values
        y = wine_data.iloc[:, -1].values

        X_train, X_test, y_train, y_test = (
            train_test_split(X, y, test_size=0.2, random_state=42))

        sc = StandardScaler()

        # aplicar escalado estandar
        X_train = sc.fit_transform(X_train)
        X_test = sc.fit_transform(X_test)

        clf = DecisionTreeClassifier(
            criterion='entropy', max_depth=4, random_state=0)
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)

        conf_matrix = confusion_matrix(y_test, y_pred)
        precision = metrics.accuracy_score(y_test, y_pred)
        f1_score = metrics.f1_score(y_test, y_pred, average='weighted')
        roc_score = metrics.roc_auc_score(y_test, y_pred)
        recall_score = metrics.recall_score(
            y_test, y_pred, average='weighted')

        first_for_box = boxplot_routes[:4]
        second_for_box = boxplot_routes[4:6]

        first_for_bar = bargraph_routes[:2]
        second_for_bar = [bargraph_routes[2],
                          bargraph_routes[4], bargraph_routes[5]]

        _pdf.add_page()
        _pdf.img_grid_section(title='Diagramas de caja y bigote',
                              description=vars.desc,
                              image_paths=first_for_box,
                              ncols=2, nrows=2, image_width=100, spacing=1)

        _pdf.add_page()
        _pdf.img_grid_section(image_paths=second_for_box,
                              ncols=2, nrows=1, image_width=100, spacing=1)
        _pdf.img_grid_section(title='Diagramas de barras',
                              description=vars.desc_bar,
                              image_paths=first_for_bar,
                              ncols=2, nrows=2, image_width=100,
                              spacing=1)

        _pdf.add_page()
        _pdf.img_grid_section(description=vars.desc_bar2,
                              image_paths=second_for_bar,
                              ncols=2, nrows=2, image_width=100,
                              spacing=1, description2=vars.desc_bar3)

        _pdf.add_page()
        _pdf.text_section(title='Variables de importancia',
                          paragraph=vars.paragraph.format(
                                str(conf_matrix).replace('\n', ''),
                                precision,
                                f1_score,
                                roc_score,
                                recall_score))
        now = datetime.now()
        now = now.strftime("%d-%m-%Y")
        new_pdf_name = _filetools.generate_file_hash(f'report-{now}.pdf')
        _pdf.output(_path_temp+new_pdf_name)

        send_file('temp\\'+new_pdf_name, as_attachment=True)

        file = ''

        return jsonify({'message': 'Report generated successfully',
                        'data': {'conf_matrix': conf_matrix.tolist(),
                                 'precision': float(precision),
                                 'f1_score': float(f1_score),
                                 'roc_score': float(roc_score),
                                 'recall_score': float(recall_score),
                                 'boxplot_routes': list(boxplot_routes),
                                 'bargraph_routes': list(bargraph_routes)
                                 }})
        # except Exception as ex:
        #     return jsonify({'error': str(ex)})
