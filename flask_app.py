import pandas as pd
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from io import StringIO, BytesIO
import random
import seaborn as sns

from flask import Flask, make_response
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/white')
def white():
    df = pd.read_csv('data/winequality-white.csv', delimiter=';')
    return str(df['pH'].mean())

@app.route('/pretty.png')
def pretty():
    df = pd.read_csv('data/winequality-white.csv', delimiter=';')
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    x_attribute = 'quality'
    y_attribute = 'pH'
    sns.stripplot(data=df, x=x_attribute, y=y_attribute, ax=axis, jitter=True)
    axis.set_xlabel(x_attribute)
    axis.set_ylabel(y_attribute)
    canvas = FigureCanvas(fig)
    output = BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response

if __name__ == '__main__':
    app.run(debug=True)
