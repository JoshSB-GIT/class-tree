import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from config.config import config
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from sklearn import metrics
from flask import Blueprint, jsonify, make_response, request, send_file
from flask_cors import cross_origin
from flask_login import login_required
from utils.filestools import FilesTools
from utils.pdftools import PdfTools
import utils.varsTools as vars
from datetime import datetime
from supabase import create_client, Client
import os

plt.switch_backend('agg')

csv_report = Blueprint('csv_report', __name__)

_filetools = FilesTools()
_path_img = './src/assets/img/'
_path_temp = './src/temp/'
category_cols = ['volatile acidity', 'citric acid', 'chlorides',
                 'free sulfur dioxide', 'sulphates', 'alcohol']

supabase: Client = create_client(config['development'].supabase_url,
                                 config['development'].supabase_key)


def save_img(name: str) -> str:
    file_name = ''+_filetools.generate_file_hash(name.replace(' ', ''))
    plt.savefig(_path_img+file_name)
    return str(_path_img+file_name+'.png')


def save_csv_fbase(data_frame: pd.DataFrame, id_csv: int = 0):
    datos = data_frame.to_dict(orient='records')

    for dct in datos:
        dct['csv_id'] = id_csv

    supabase.table('dataset').insert(datos).execute()

# learningmachine123
# ufvvcvghcvryxhpl


@cross_origin
@csv_report.route('/generate_pdf', methods=['POST'])
@login_required
def generate_pdf_report():
    if request.method == 'POST':
        path_temp = './src/temp/'
        try:
            if 'wine_red' not in request.files:
                return make_response(
                    jsonify(
                        {'message': 'Not file uploaded'}), 400)
            file = request.files['wine_red']

            if file.filename == '':
                return make_response(
                    jsonify(
                        {'message': 'Empty file name'}), 400)

            if len(file.filename) > 20:
                return make_response(jsonify(
                    {'message': 'Empty file name'}), 400)

            new_filename = _filetools.generate_file_hash(file.filename)
            save_temp = os.path.join(path_temp, new_filename)
            file.save(save_temp)
            wine_data = pd.read_csv(save_temp,
                                    sep=';', engine='python',
                                    skiprows=0, index_col=False)

            wine_data.dropna(inplace=True)

            csv_id = supabase.table('csv').insert(
                {'name': str(new_filename)}).execute()
            save_csv_fbase(wine_data, csv_id.dict()['data'][0]['id'])

            unique_vals_list = []
            for col in category_cols:
                unique_vals_list.append(
                    f"{col}: {wine_data[col].nunique()} sublevels")

            wine_data.drop_duplicates(inplace=True)

            boxplot_routes = []
            for col in category_cols:
                plt.clf()
                sns.boxplot(data=wine_data[col], orient='h')
                plt.title(col)
                boxplot_routes.append(save_img('boxplot-'+str(col)))

            bargraph_routes = []

            for col in category_cols:
                plt.clf()
                plt.figure(figsize=(10, 6))
                sns.barplot(x='quality', y=col, data=wine_data)
                bargraph_routes.append(save_img('bar_graph-'+str(col)))

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

            _pdf = PdfTools(orientation='P', unit='mm', format='A4')

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
                                  precision, f1_score, roc_score,
                                  recall_score,
                                  str(wine_data['quality'].value_counts()[1]),
                                  str(wine_data['quality'].value_counts()[0]),
                                  str(unique_vals_list[0]),
                                  str(unique_vals_list[1]),
                                  str(unique_vals_list[2]),
                                  str(unique_vals_list[3]),
                                  str(unique_vals_list[4]),
                                  str(unique_vals_list[5])))
            now = datetime.now()
            now = now.strftime("%d-%m-%Y")
            new_pdf_name = _filetools.generate_file_hash(f'report-{now}.pdf')
            _pdf.output(_path_temp+new_pdf_name)

            data = {
                'precision': float(precision),
                'f1score': float(f1_score),
                'performance': float(roc_score),
                'recall': float(recall_score),
                'confusion_matrix': str(conf_matrix.tolist()),
                'ypred': str(y_pred),
                'ytest': str(y_test),
                'goodwine': str(wine_data['quality'].value_counts()[1]),
                'badwine': str(wine_data['quality'].value_counts()[0]),
                'csv_id': int(csv_id.dict()['data'][0]['id'])
            }

            supabase.table("data").insert(data).execute()

            return send_file('temp\\'+new_pdf_name, as_attachment=True)

        except Exception as ex:
            return make_response(jsonify({'error': str(ex)}), 400)


@cross_origin
@csv_report.route('/generate_report', methods=['POST'])
@login_required
def generate_report_csv():
    if request.method == 'POST':
        path_temp = './src/temp/'
        try:
            if 'wine_red' not in request.files:
                return make_response(
                    jsonify(
                        {'message': 'Not file uploaded'}), 400)
            file = request.files['wine_red']

            if file.filename == '':
                return make_response(
                    jsonify(
                        {'message': 'Empty file name'}), 400)

            if len(file.filename) > 20:
                return make_response(jsonify(
                    {'message': 'Empty file name'}), 400)

            new_filename = _filetools.generate_file_hash(file.filename)
            save_temp = os.path.join(path_temp, new_filename)
            file.save(save_temp)
            wine_data = pd.read_csv(save_temp,
                                    sep=';', engine='python',
                                    skiprows=0, index_col=False)
            cantidad_datos = wine_data.count()
            promedios_datos = wine_data.mean()
            valores_unicos = wine_data.nunique()
            advanced_pie_chart = []
            pie_chart = []
            bar_unique_graph = []
            for columna, cantidad in cantidad_datos.items():
                advanced_pie_chart.append({'name': columna,
                                           'value': cantidad})

            for columna, promedio in zip(wine_data.columns, promedios_datos):
                pie_chart.append({'name': columna,
                                  'value': promedio})

            for columna, valores in zip(wine_data.columns, valores_unicos):
                bar_unique_graph.append({'name': columna,
                                        'value': valores})

            wine_data.dropna(inplace=True)

            unique_vals_list = []
            for col in category_cols:
                unique_vals_list.append(
                    f"{col}: {wine_data[col].nunique()} sublevels")

            wine_data.drop_duplicates(inplace=True)

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

            return jsonify({'message': 'Report generated successfully',
                            'data': {
                                'conf_matrix': conf_matrix.tolist(),
                                'precision': float(precision),
                                'f1_score': float(f1_score),
                                'roc_score': float(roc_score),
                                'recall_score': float(recall_score),
                                'unique_vals': unique_vals_list,
                                'good_wines': str(
                                    wine_data['quality'].value_counts()[1]),
                                'bad_wines': str(
                                    wine_data['quality'].value_counts()[0])
                            },
                            'graphs': {
                                'advanced_pie_chart': advanced_pie_chart,
                                'pie_chart': pie_chart,
                                'bar_unique_graph': bar_unique_graph
                            }})

        except Exception as ex:
            return make_response(jsonify({'error': str(ex)}), 400)
