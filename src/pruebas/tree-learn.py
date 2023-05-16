import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import (
    train_test_split)
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from sklearn import metrics


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


path_file = "./src/pruebas/winequality-red.csv"
wine_data = pd.read_csv(path_file,
                        sep=';', engine='python',
                        skiprows=0, index_col=False)
# Limpiza de datos
wine_data.shape
wine_data.dropna(inplace=True)  # <- Elimina las filas con datos vacíos

# Columnas relevantes
category_cols = ['fixed acidity', 'citric acid', 'residual sugar',
                 'free sulfur dioxide', 'pH', 'alcohol']

# mostrar subniveles de variables o con valores únicos
print(
    '\n------------------- valores unicos -------------------')
for col in category_cols:
    print(f"Column {col}: {wine_data[col].nunique()} sublevels")
print(
    '------------------------------------------------------')

# Mostrar columnas numéricas o descripción
print(
    '\n------------------- Columnas numéricas -------------------')
print(wine_data.describe())
print(
    '------------------------------------------------------')

# Eliminar filas repetidas
wine_data.drop_duplicates(inplace=True)
# GRAFICO para variables
principal_graph(wine_data, 'pH')

# Graficar subniveles de cada variable
# sub_level_graph(wine_data, category_cols)

# Histograma
# histo_graph(wine_data, category_cols)

# Barras calidad vs variable
bar_diagram_graph('fixed acidity', data_frame=wine_data)
# bar_diagram_graph('volatile acidity', data_frame=wine_data)
# bar_diagram_graph('citric acid', data_frame=wine_data)
# bar_diagram_graph('residual sugar', data_frame=wine_data)
# bar_diagram_graph('chlorides', data_frame=wine_data)
# bar_diagram_graph('free sulfur dioxide', data_frame=wine_data)
# bar_diagram_graph('total sulfur dioxide', data_frame=wine_data)
# bar_diagram_graph('density', data_frame=wine_data)
# bar_diagram_graph('pH', data_frame=wine_data)
# bar_diagram_graph('sulphates', data_frame=wine_data)
# bar_diagram_graph('alcohol', data_frame=wine_data)

# Clasificar por bueno o mal
# wine_data['quality'].value_counts()

wine_data['quality'].value_counts()

wine_data['quality'] = wine_data['quality'].apply(
    lambda x: 1 if x > 6.5 else 0)
print(
    '\n------------------- head() -------------------')
print(wine_data.head())
print(
    '------------------------------------------------------')

print(
    '\n------------------- value_counts() -------------------')
print(wine_data['quality'].value_counts())
print(
    '------------------------------------------------------')

# graficar los nuevos valores para quality
bar_simple_graph(wine_data, 'quality')

X = wine_data.iloc[:, :-1].values
y = wine_data.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.2,
                                                    random_state=42)

sc = StandardScaler()

# aplicar escalado estandar
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)


# Mostrar info
print(
    '\n------------------- INFORMACIÓN -------------------')
wine_data.info()
print(
    '------------------------X------------------------------')
print(X)
print(
    '------------------------y------------------------------')
print(y)
print(
    '----------------------sshape--------------------------------')
print("X-train shape:", X_train.shape, "\n",
      "X-test shape:", X_test.shape, "\n",
      "y-train shape:", y_train.shape, "\n",
      "y-test shape:", y_test.shape)

#
clf = DecisionTreeClassifier(criterion='entropy', max_depth=4, random_state=0)
print(clf.fit(X_train, y_train))
print(
    '------------------------------------------------------')
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print(
    '------------------------ypred-------------------------')
print(y_pred)
print(
    '------------------------ytest-------------------------')
print(y_test)

cm = confusion_matrix(y_test, y_pred)
print(
    '--------------------confusion_matrix------------------')
print(cm)

print(
    '------------------------------------------------------')
print("Precisión: ", metrics.accuracy_score(y_test, y_pred))
print("F1 Record: ", metrics.f1_score(y_test, y_pred, average='weighted'))
print("Rendimiento: ", metrics.roc_auc_score(y_test, y_pred))
print("Recall: ", metrics.recall_score(y_test, y_pred, average='weighted'))
