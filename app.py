# import numpy as np
from flask import Flask, request, jsonify, render_template
# import pickle
from model import data_prediction

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [x for x in request.form.values()]
    prediction = data_prediction(int_features)

    return render_template('index.html', prediction_text='Patient Has {} Cancer'.format(prediction))


if __name__ == "__main__":
    app.run(debug=True)