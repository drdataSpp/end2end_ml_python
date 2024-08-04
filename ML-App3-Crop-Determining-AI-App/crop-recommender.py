# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 13:34:59 2021

@author: soory
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


##-----------------------------------------------------------------------------
##Importing & Checking the dataset

crop_df = pd.read_csv("https://raw.githubusercontent.com/dphi-official/Datasets/master/crop_recommendation/train_set_label.csv")

crop_df.head()
crop_df.tail()
crop_df.info()
crop_df.describe()
crop_df.shape
crop_df.dtypes
crop_df.isnull().sum()
crop_df["crop"].sort_values().unique()


##-----------------------------------------------------------------------------
##Data Visualization

# Plot 1
plt.figure(figsize=(15,10))
plt.hist(crop_df["N"], bins=75, color='pink', edgecolor='black', linewidth=1.2)
plt.title("Distribution of the Nitrogen")
plt.xlabel("Ratio of Nitrogen content in soil")
plt.ylabel("Count")

# Plot 2
plt.figure(figsize=(15,10))
plt.hist(crop_df["P"], bins=75, color='pink', edgecolor='black', linewidth=1.2)
plt.title("Distribution of the Phosphorus")
plt.xlabel("Ratio of Phosphorus content in soil")
plt.ylabel("Count")

# Plot 3
plt.figure(figsize=(15,10))
plt.hist(crop_df["K"], bins=75, color='pink', edgecolor='black', linewidth=1.2)
plt.title("Distribution of the Potassium")
plt.xlabel("Ratio of Potassium content in soil")
plt.ylabel("Count")

# Plot 4
plt.figure(figsize=(15,10))
plt.hist(crop_df["temperature"], bins=75, color='pink', edgecolor='black', linewidth=1.2)
plt.title("Distribution of the Temperature")
plt.xlabel("Temperature in degree Celsius")
plt.ylabel("Count")

# Plot 5
plt.figure(figsize=(15,10))
plt.hist(crop_df["humidity"], bins=75, color='pink', edgecolor='black', linewidth=1.2)
plt.title("Distribution of the Relative Humidity")
plt.xlabel("Temperature in relative humidity in %")
plt.ylabel("Count")

# Plot 6 
plt.figure(figsize=(15,10))
plt.hist(crop_df["ph"], bins=75, color='pink', edgecolor='black', linewidth=1.2)
plt.title("Distribution of the ph Value")
plt.xlabel("ph value of the soil")
plt.ylabel("Count")

# Plot 7 
plt.figure(figsize=(15,10))
plt.hist(crop_df["rainfall"], bins=75, color='pink', edgecolor='black', linewidth=1.2)
plt.title("Distribution of the Rainfall")
plt.xlabel("Rainfall in mm")
plt.ylabel("Count")

# Plot 8.1 
plt.figure(figsize=(20,10))
sns.barplot(x="crop", y="N", data=crop_df)
plt.title("Barplot to show how Nitrogen effects different kinds of crop")
plt.xlabel("CROPS")
plt.ylabel("NITROGEN")

# Plot 8.2
plt.figure(figsize=(20,10))
sns.boxplot(x="crop", y="N", data=crop_df)
plt.title("Boxplot to show how Nitrogen effects different kinds of crop")
plt.xlabel("CROPS")
plt.ylabel("NITROGEN")

# Plot 9.1 
plt.figure(figsize=(20,10))
sns.barplot(x="crop", y="P", data=crop_df)
plt.title("Barplot to show how Phosphorus effects different kinds of crop")
plt.xlabel("CROPS")
plt.ylabel("PHOSPHORUS") 

# Plot 9.2
plt.figure(figsize=(20,10))
sns.boxplot(x="crop", y="P", data=crop_df)
plt.title("Boxplot to show how Phosphorus effects different kinds of crop")
plt.xlabel("CROPS")
plt.ylabel("PHOSPHORUS")

# Plot 10.1 
plt.figure(figsize=(20,10))
sns.barplot(x="crop", y="K", data=crop_df)
plt.title("Barplot to show how Potassium effects different kinds of crop")
plt.xlabel("CROPS")
plt.ylabel("POTASSIUM") 

# Plot 10.2
plt.figure(figsize=(20,10))
sns.boxplot(x="crop", y="P", data=crop_df)
plt.title("Boxplot to show how Potassium effects different kinds of crop")
plt.xlabel("CROPS")
plt.ylabel("POTASSIUM")

# Plot 11.1 
plt.figure(figsize=(20,10))
sns.barplot(x="crop", y="temperature", data=crop_df)
plt.title("Barplot to show how temperature effects different kinds of crop")
plt.xlabel("CROPS")
plt.ylabel("TEMPERATURE") 

# Plot 11.2
plt.figure(figsize=(20,10))
sns.boxplot(x="crop", y="P", data=crop_df)
plt.title("Boxplot to show how temperature effects different kinds of crop")
plt.xlabel("CROPS")
plt.ylabel("TEMPERATURE")

# Plot 11.1 
plt.figure(figsize=(20,10))
sns.barplot(x="crop", y="temperature", data=crop_df)
plt.title("Barplot to show how temperature effects different kinds of crop")
plt.xlabel("CROPS")
plt.ylabel("TEMPERATURE") 

# Plot 11.2
plt.figure(figsize=(20,10))
sns.boxplot(x="crop", y="P", data=crop_df)
plt.title("Boxplot to show how temperature effects different kinds of crop")
plt.xlabel("CROPS")
plt.ylabel("TEMPERATURE")

# Plot 12.1 
plt.figure(figsize=(20,10))
sns.barplot(x="crop", y="humidity", data=crop_df)
plt.title("Barplot to show how humidity effects different kinds of crop")
plt.xlabel("CROPS")
plt.ylabel("HUMIDITY") 

# Plot 12.2
plt.figure(figsize=(20,10))
sns.boxplot(x="crop", y="humidity", data=crop_df)
plt.title("Boxplot to show how humidity effects different kinds of crop")
plt.xlabel("CROPS")
plt.ylabel("HUMIDITY")

# Plot 13.1 
plt.figure(figsize=(20,10))
sns.barplot(x="crop", y="ph", data=crop_df)
plt.title("Barplot to show how ph effects different kinds of crop")
plt.xlabel("CROPS")
plt.ylabel("ph VALUE") 

# Plot 13.2
plt.figure(figsize=(20,10))
sns.boxplot(x="crop", y="ph", data=crop_df)
plt.title("Boxplot to show how ph effects different kinds of crop")
plt.xlabel("CROPS")
plt.ylabel("ph VALUE")

# Plot 14.1 
plt.figure(figsize=(20,10))
sns.barplot(x="crop", y="rainfall", data=crop_df)
plt.title("Barplot to show how rainfall effects different kinds of crop")
plt.xlabel("CROPS")
plt.ylabel("RAINFALL") 

# Plot 14.2
plt.figure(figsize=(20,10))
sns.boxplot(x="crop", y="rainfall", data=crop_df)
plt.title("Boxplot to show how rainfall effects different kinds of crop")
plt.xlabel("CROPS")
plt.ylabel("RAINFALL")


##-----------------------------------------------------------------------------
##Partitioning the dataset

from sklearn.model_selection import train_test_split

X = crop_df.drop("crop", axis=1)
y = crop_df["crop"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

##-----------------------------------------------------------------------------
##Building the machine learning model

from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

##Hyperparameter tuning for the random forest classifier
##-------------------------------------------

# Number of trees in random forest
n_estimators = [int(x) for x in np.linspace(start = 200, stop = 2000, num = 10)]
# Number of features to consider at every split
max_features = ['auto', 'sqrt']
# Maximum number of levels in tree
max_depth = [int(x) for x in np.linspace(10, 110, num = 11)]
max_depth.append(None)
# Minimum number of samples required to split a node
min_samples_split = [2, 5, 10]
# Minimum number of samples required at each leaf node
min_samples_leaf = [1, 2, 4]
# Method of selecting samples for training each tree
bootstrap = [True, False]
# Create the random grid
random_grid = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf,
               'bootstrap': bootstrap}

print(random_grid)

rf = RandomForestClassifier()

rf_randomSearch = RandomizedSearchCV(estimator = rf,
param_distributions = random_grid, n_iter = 100, cv = 3, verbose=2, 
random_state=42, n_jobs = -1)

rf_randomSearch.fit(X_train, y_train)

rf_randomSearch.best_params_
rf_randomSearch.best_estimator_

hyperTunedRFC = RandomForestClassifier(max_depth=110, max_features='sqrt', min_samples_split=10,
                       n_estimators=600)

hyperTunedRFC.fit(X_train, y_train)

preds_1 = hyperTunedRFC.predict(X_test)

print("Accuracy of the hyperparameter tuned Random Forest Classifier: ",
      accuracy_score(y_test, preds_1))

##-----------------------------------------------------------------------------
##Hyperparameter tuning for the XGBoost Classifier

random_grid2 = {"learning_rate"    : [0.05, 0.10, 0.15, 0.20, 0.25, 0.30 ] ,
 "max_depth"        : [ 3, 4, 5, 6, 8, 10, 12, 15],
 "min_child_weight" : [ 1, 3, 5, 7 ],
 "gamma"            : [ 0.0, 0.1, 0.2 , 0.3, 0.4 ],
 "colsample_bytree" : [ 0.3, 0.4, 0.5 , 0.7 ] }

print(random_grid2)

import xgboost as xgb

xgb_1 = xgb.XGBClassifier()

xgb_randomSearch = RandomizedSearchCV(estimator = xgb_1,
param_distributions = random_grid2, n_iter = 100, cv = 3, verbose=2, 
random_state=42, n_jobs = -1)

xgb_randomSearch.fit(X_train, y_train)

xgb_randomSearch.best_params_
xgb_randomSearch.best_estimator_

hyperTunedXGB = xgb.XGBClassifier(base_score=0.5, booster='gbtree', colsample_bylevel=1,
              colsample_bynode=1, colsample_bytree=0.5, gamma=0.2, gpu_id=-1,
              importance_type='gain', interaction_constraints='',
              learning_rate=0.05, max_delta_step=0, max_depth=12,
              min_child_weight=1, missing=np.NaN, monotone_constraints='()',
              n_estimators=100, n_jobs=8, num_parallel_tree=1,
              objective='multi:softprob', random_state=0, reg_alpha=0,
              reg_lambda=1, scale_pos_weight=None, subsample=1,
              tree_method='exact', validate_parameters=1, verbosity=None)

hyperTunedXGB.fit(X_train, y_train)

preds_2 = hyperTunedXGB.predict(X_test)

print("Accuracy of the hyperparameter tuned XG Classifier: ",
      accuracy_score(y_test, preds_2))

##-----------------------------------------------------------------------------
##Saving the best model

from joblib import dump
MODEL_NAME = "Crop-Recommender.pkl"
dump(hyperTunedRFC, MODEL_NAME)

##-----------------------------------------------------------------------------
##Inputting custom values
randomGuess1_rfc = hyperTunedRFC.predict([[22.0,51.0,16.0,27.96583691,61.34900107,
                                 8.639586199, 70.10472076]])

print(randomGuess1_rfc)

randomGuess2_rfc = hyperTunedRFC.predict([[31.6514200472117,
77.1866467768273, 21.5352267296156, 23.762152326372615, 62.330380487058285,
6.937717041963898, 53.415702712829976]])

print(randomGuess2_rfc)

## THE END

##-----------------------------------------------------------------------------
