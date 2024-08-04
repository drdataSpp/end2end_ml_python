import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import joblib

#Creating the flask app
app = Flask(__name__)

model = joblib.load("breast-cancer-model.pkl")

@app.route('/')
def home():
    return render_template('Breast_Canc_Template.html')

@app.route('/predict', methods=['POST'])
def predict():
  
     if request.method == 'POST':
            
            bThickness=request.form['thicknessBox']

            bSize=request.form['sizeBox']

            bShape=request.form['shapeBox']

            bAdhesion=request.form['adhesionBox']

            bSingle=request.form['singleBox']

            bNuclei=request.form['nucleiBox']

            bChromatin=request.form['chromatinBox']

            bNucleoli=request.form['nucleoliBox']

            bMitoses=request.form['mitosesBox']


            prediction = model.predict([[bThickness, bSize, bShape, bAdhesion, bSingle, bNuclei, bChromatin, bNucleoli, bMitoses]])

            if ( prediction[0] == 1):
                return render_template('Breast_Canc_Template.html', prediction_text= 'Result: Malignant')
            else:
                return render_template('Breast_Canc_Template.html', prediction_text= 'Result: Benign')

if __name__ == "__main__":
    app.run(debug=True)