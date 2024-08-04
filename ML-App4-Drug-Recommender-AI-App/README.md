# Drug Recommender AI App by ***Soorya Parthiban***

***An innovative AI-tool to recommend drugs based on one's attributes***

## Table Of Contents
* App Preview
* Dataset Link
* How the decisions are made?
* Business Problem
* Machine Learning based Solution
* Installation
* Languages Used
* Contact Me
* License
* Credits

## App Preview
![Cick Here](https://github.com/drdataSpp/ML-App4-Drug-Recommender-AI-App/blob/master/Drug%20Recommender%20App.gif)

## Dataset Link
[Please click here](https://www.kaggle.com/pablomgomez21/drugs-a-b-c-x-y-for-decision-trees)

## How the decisions are made?
![alt text](https://github.com/drdataSpp/ML-App4-Drug-Recommender-AI-App/blob/master/How%20the%20model%20works.PNG)

## Business Problem
I have collected data about a set of patients, all of whom suffered from the same **illness**. During their course of treatment, each patient responded to one of 5 medications, Drug A, Drug B, Drug c, Drug x and y. I will build a model to find out which drug might be appropriate for a future patient with the same illness. The features of this dataset are ***Age, Sex, Blood Pressure, and the Cholesterol of the patients, and the target is the drug that each patient responded to.***

In this project, I'm going to show how to use data science and machine learning knowledge and skills to solve this problem.

## Machine Learning based solution
* **First Step:** I've imported the patient's data set that has attributes about the patient and the most appropriate drug for them.
* **Second Step:** I've analyzed the data by checking its data quality: missing values, outliers, data format, etc. After this, I've visualized the dataset to extract insights about the data.
* **Third Step:** After checking the data quality and visualizing the data set, I've have pre-processed the data set: converted categorical values to numerical values.
* **Fourth Step:** I've have then created two subsets from the orginal data set called:
  * X_train: *Used to train the Machine Learning Models*
  * X_test: *Used to test the performance of the trained models*
  
 * **Fifth Step:** Trained 3 Classifier Models: LGBM Classifier, Bagging Classifier and Decision Tree Classifier model. Checked the trained model's performance using the X_test set.
 
 * **Sixth Step:** Since all the models performed really well and achieved an accuracy score of ***100%***, I chose LGBM classifier model and saved it in the pickle format using joblib.
 
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
