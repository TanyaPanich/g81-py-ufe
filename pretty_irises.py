import pandas as pd
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from io import StringIO, BytesIO
import random
import seaborn as sns
from sklearn.datasets import load_iris

from flask import Flask, make_response
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)
