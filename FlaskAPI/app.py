import numpy as np

import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.p', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    a = request.form.values()
    int_features = pd.DataFrame(data=a).T
    int_features = int_features.set_axis(['flat_type', 'city_area', 'layout', 'status', 'premises_area', 'floor', 'floor_tot'], axis=1, inplace=False)
    prediction = model.predict(int_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Prediction: "{}"'.format(output))

@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
