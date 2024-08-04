import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import joblib

#Creating the flask app
app = Flask(__name__)

model = joblib.load(r"D:\001_Data\END 2 END ML\Spotify Music Recommender\spotify-recommender.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    prediction = prediction[0]
    print(prediction)

    if prediction < 0.5:
        return render_template('index.html', prediction_text='Prediction: DISLIKED')
    else:
        return render_template('index.html', prediction_text='Prediction: LIKED')


if __name__ == "__main__":
    app.run(debug=True)
