# Vehicle Insurance Response Predictor AI App by ***Soorya Parthiban***

***An innovative AI-tool to predict whether a customer would be interested in Vehicle Insurance.***

## Table Of Contents
* App Preview
* Dataset Link
* Business Problem
* Machine Learning based Solution
* Installation
* Languages Used
* Contact Me
* License
* Credits

## App Preview
![Cick Here](https://github.com/drdataSpp/ML-App5-Insurance-Response-Predictor-AI-App/blob/master/Vehicle%20Ins%20Response%20Predictor%20App.gif)

## Dataset Link
[Please click here](https://www.kaggle.com/anmolkumar/health-insurance-cross-sell-prediction)

## Business Problem
* Just like medical insurance, there is vehicle insurance where every year customer needs to pay a premium of certain amount to insurance provider company so that in case of  unfortunate accident by the vehicle, the insurance provider company will provide a compensation (called ‘sum assured’) to the customer.
* Building a model to predict whether a customer would be interested in Vehicle Insurance is extremely helpful for the company because it can then accordingly plan its communication strategy to reach out to those customers and optimise its business model and revenue.
* Now, in order to predict, whether the customer would be interested in Vehicle insurance, you have information about demographics (gender, age, region code type), Vehicles (Vehicle Age, Damage), Policy (Premium, sourcing channel) etc.

## Machine Learning based solution
* **First Step:** I've imported the vehicle insurance customer data set that has attributes about the customer, customer attributes and their response.
* **Second Step:** I've analyzed the data by checking its data quality: missing values, outliers, data format, etc. After this, I've visualized the dataset to extract insights about the data.
* **Third Step:** After checking the data quality and visualizing the data set, I've have pre-processed the data set: converted categorical values to numerical values.
* **Fourth Step:** I performed oversampling as the dataset was an **imbalanced dataset** and then I created two subsets from the orginal data set called:
  * X_train: *Used to train the Machine Learning Models*
  * X_test: *Used to test the performance of the trained models*
  
 * **Fifth Step:** Trained multiple Classifier Models: LGBM Classifier, Bagging Classifier and Decision Tree Classifier model. Checked the trained model's performance using the X_test set.
 
 * **Sixth Step:** I chose Bagging classifier model as the best performing model based on its accuracy and ROC AUC scores and saved it in the pickle format using joblib.
 
 * **Seventh Step:** Created a front-end app using **HTML and CSS** and integrated the pickle file with the app using the **flask framework**.
 
## Installation
The application is written in Python 3.7. If you don't have Python installed you can find it [here](https://www.python.org/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after cloning the repository :-

```
pip install -r requirements.txt
```
## Languages Used
* [Python](https://www.python.org/)
  * [PyCharm](https://www.jetbrains.com/pycharm/)
  * [Google Colab](https://colab.research.google.com/notebooks/intro.ipynb)
  
* HTML & CSS 

* [Flask Web Framework](https://flask.palletsprojects.com/en/1.1.x/)

## Contact Me
* [Soorya's LinkedIn](https://www.linkedin.com/in/sooryaprakashparthiban/)
* [Soorya's Twitter](https://twitter.com/Drdataspp)

## License
**Copyright 2021 Soorya Prakash Parthiban**

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

## Credits
Thanks to kaggle for providing this dataset.
