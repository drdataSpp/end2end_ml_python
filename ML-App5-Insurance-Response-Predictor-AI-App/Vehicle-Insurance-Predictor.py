import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import joblib

#Creating the flask app
app = Flask(__name__)

model = joblib.load("insurance-response-predictor.pkl")

@app.route('/')
def home():
    return render_template('Vehicle_Insurance_App_Template.html')

@app.route('/predict', methods=['POST'])
def predict():
  
     if request.method == 'POST':
            Male=request.form['genderBox']
            if(Male=='male'):
                Male=1
            else:
                Male=0

            Age=request.form['ageBox']

            DL = request.form['DLBox']
            if(DL == 'yesDL'):
                DL = 1
            else:
                DL = 0	

            RegCode=request.form['regCodeBox']

            PrevIns = request.form['prevInsBox']
            if(PrevIns == 'yesPrevIns'):
                PrevIns = 1
            else:
                PrevIns = 0

            VehDam = request.form['damageBox']
            if(VehDam == 'yesDam'):
                VehDam = 1
            else:
                VehDam = 0

            AnnualPrem=request.form['annualPremBox']

            SalesChannel=request.form['salesChnBox']

            Vintage=request.form['vintageBox']

            VehicleAge = request.form['vehicleAgeBox']
            if(VehicleAge == 'lessThanOne'):
                lessThanOne = 1
                moreThanTwo = 0
            elif(VehicleAge == 'MoreThanTwo'):
                lessThanOne = 0
                moreThanTwo = 1 
            else:
                lessThanOne = 0
                moreThanTwo = 0

            prediction = model.predict([[Male, Age, DL, RegCode, PrevIns, VehDam, AnnualPrem, SalesChannel, Vintage, lessThanOne, moreThanTwo]])

            if ( prediction[0] == 1):
                return render_template('Vehicle_Insurance_App_Template.html', prediction_text= 'The customer will buy the insurance')
            else:
                return render_template('Vehicle_Insurance_App_Template.html', prediction_text= 'The customer will not buy the insurance')

if __name__ == "__main__":
    app.run(debug=True)