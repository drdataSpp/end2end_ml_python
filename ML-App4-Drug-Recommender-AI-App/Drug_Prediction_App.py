import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import joblib

#Creating the flask app
app = Flask(__name__)

model = joblib.load("drug-recommender.pkl")

@app.route('/')
def home():
    return render_template('Drug_App_Template.html')

@app.route('/predict', methods=['POST'])
def predict():
  
     if request.method == 'POST':
            Male=request.form['genderBox']
            if(Male=='male'):
                Male=1
            else:
                Male=0

            Cholesterol_Status = request.form['cholesterolBox']
            if(Cholesterol_Status == 'cholesterolHigh'):
                Cholesterol_Status = 1
            else:
                Cholesterol_Status = 0	

            BP_Status = request.form['bpBox']
            if(BP_Status == 'bpHigh'):
                BP_HIGH = 1
                BP_LOW = 0
            elif(BP_Status == 'bpLow'):
                BP_HIGH = 0
                BP_LOW = 1
            else:
                BP_HIGH = 0
                BP_LOW=0

            Age = request.form['ageBox']
                
            NatoKBox = request.form['naToKBox']

            prediction = model.predict([[Age, Male, Cholesterol_Status, NatoKBox, BP_HIGH, BP_LOW]])

            return render_template('Drug_App_Template.html', prediction_text= 'Predicted Drug is ' + prediction[0])

if __name__ == "__main__":
    app.run(debug=True)