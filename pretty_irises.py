import pandas as pd
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from io import StringIO, BytesIO
import random
import seaborn as sns
from sklearn.datasets import load_iris
from flask import Flask, make_response

app = Flask(__name__)

def get_iris_df():
    raw_iris_data = load_iris()
    target_names = raw_iris_data.target_names[raw_iris_data.target]
    iris_df = pd.DataFrame(raw_iris_data.data, columns=raw_iris_data.feature_names)
    iris_df['target'] = raw_iris_data.target
    iris_df['label'] = target_names
    return iris_df

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/iris.png')
def iris_png():
    iris_df = get_iris_df()
    fig = Figure()
    ax = fig.add_subplot(1, 1, 1)
    sns.set(style="darkgrid")
    setosa = iris_df.query("label == 'setosa'")
    virginica = iris_df.query("label == 'virginica'")
    versicolor = iris_df.query("label == 'versicolor'")
    ax.set_aspect("equal")
    ax = sns.kdeplot(setosa['sepal width (cm)'], setosa['sepal length (cm)'], cmap="Reds", shade=True, shade_lowest=False, ax=ax)
    ax = sns.kdeplot(virginica['sepal width (cm)'], virginica['sepal length (cm)'], cmap="Blues", shade=True, shade_lowest=False, ax=ax)
    # ax = sns.kdeplot(versicolor['sepal width (cm)'], versicolor['sepal length (cm)'], cmap="Greens", shade=True, shade_lowest=False, ax=ax)
    red = sns.color_palette("Reds")[-2]
    blue = sns.color_palette("Blues")[-2]
    green = sns.color_palette("Greens")[-2]
    ax.text(2.5, 8.2, "virginica", size=16, color=blue)
    ax.text(3.8, 4.5, "setosa", size=16, color=red)
    # ax.text(3.75, 6.2, "versicolor", size=16, color=green)
    canvas = FigureCanvas(fig)
    output = BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response


if __name__ == '__main__':
    app.run(debug=True)
