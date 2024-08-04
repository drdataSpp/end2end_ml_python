# Crop Recommender AI App by ***Soorya Parthiban***

***An innovative AI-tool to recommend crop based on farm's attributes***

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
![Cick Here](https://github.com/drdataSpp/ML-App3-Crop-Determining-AI-App/blob/master/Crop%20Recommender%20App.gif)

## Dataset Link
[Please click here](https://www.kaggle.com/atharvaingle/crop-recommendation-dataset)

## Business Problem
Precision agriculture is in trend nowadays. It helps the farmers to get informed decision about the farming strategy. Here, I present you a dataset which would allow the users to build a predictive model to recommend the most suitable crops to grow in a particular farm based on various parameters.

In this project, I'm going to show how to use data science and machine learning knowledge and skills to solve this problem.

## Machine Learning based solution
* **First Step:** I've imported the crop data set that has attributes about the farm/ soil and the most suitable crop for that particular sand or farm.
* **Second Step:** I've analyzed the data by checking its data quality: missing values, outliers, data format, etc. After this, I've visualized the dataset to extract insights about the data.
* **Third Step:** Data Pre-Processing.
* **Fourth Step:** I've have then created two subsets from the orginal data set called:
  * X_train: *Used to train the Machine Learning Models*
  * X_test: *Used to test the performance of the trained models*
  
 * **Fifth Step:** Trained 2 Classifier Models using the best *hyperparameters*: Random Forest Classifier & XGBoost Classifier model. Checked the trained model's performance using the X_test set.
 
 * **Sixth Step:** Chose Random Forest Classifier as the best model based on its accuracy score and saved it in the pickle format using joblib.
 
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
