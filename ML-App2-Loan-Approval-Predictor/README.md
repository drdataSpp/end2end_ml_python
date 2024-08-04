# AI-Powered Loan Approval Predictor App

***An innovative AI-tool to predict loan application's outcome***

*Timely, high quality predictions about your loan application; Innovative use of your data, giving useful and predictive insights; Saves your time in emailing and getting qoutes*

## Table Of Contents
* App Preview
* App Link
* Business Problem
* Machine Learning based Solution
* Installation
* Languages Used
* Contact Me
* License
* Credits

## App Preview
![alt text](https://github.com/drdataSpp/ML-App2-Loan-Approval-Predictor/blob/main/Loan%20Predictor%20App.gif)

## App Link
[Cick Here](https://www.linkedin.com/feed/update/urn:li:activity:6761916487990165504/)

## Business Problem
Both the Banks and Loan applicants find the process of knowing or letting someone know their chances of getting a yes for a loan application is hard and time-consuming. Both the parties have to find a time to arrange a meeting and then analyze their application to know their outcome. 

In this project, we are going to see how to use data science and machine learning knowledge and skills to solve this problem.

## Machine Learning based solution
* **First Step:** We get the approved and rejected loan applicants data from the bank.
* **Second Step:** We analyzeed the data by checking its data quality: missing values, outliers, data format, etc. After this, we visualized the dataset to extract insights about the data.
* **Third Step:** After checking the data quality and visualizing the data set, we have performed feature engineering: filled missing values and encoded text data to numerical data.
* **Fourth Step:** We have then created three subsets from the orgincal data set called:
  * X_train: *Used to train the Machine Learning Models*
  * X_test: *Used to test the performance of the trained models*
  * X_Val: *This set of data is used in the cross validation test*
  
 *I have also created a scaled version of the above three sets which was used to train the **Logistic Regression** Model*.
 
 * **Fifth Step:** Trained 3 Classifier Models: Logistic Regression, Random Forest Classifier and XGBoost Classifier model with their best parameters. They best paramaters were found using RandomizedSearchCV. Checked the trained model's performance using the X_test set.
 
 * **Sixth Step:** Cross validated the trained models on the X_Val set and choosed the Random Forest Classifier model as the best one and saved it in the pickle format using joblib.
 
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
