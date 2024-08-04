# Spotify Music Recommandation AI App by ***Soorya Parthiban***

***An innovative AI-App to predict whether one likes or dislikes a song using Spotify's Music API Data***

## Table Of Contents
* App Preview
* Dataset Link
* Data Definition
* Machine Learning based Solution
* Installation
* Languages Used
* Contact Me
* License
* Credits

## App Preview
![Cick Here](https://github.com/drdataSpp/ML-App7-Spotify-Music-Recommender-API/blob/master/Music-Recommender-App.gif)

## Dataset Link
[Please click here](https://www.kaggle.com/bricevergnou/spotify-recommendation)

## Data Definition

### Independent Variable
- Acousticness : A confidence measure from 0.0 to 1.0 of whether the track is acoustic. 1.0 represents high confidence the track is acoustic.
- Danceability : Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable.
- Duration_ms : The duration of the track in milliseconds.
- Energy : Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy. For example, death metal has high energy, while a Bach prelude scores low on the scale. Perceptual features contributing to this attribute include dynamic range, perceived loudness, timbre, onset rate, and general entropy.
- Instrumentalness : Predicts whether a track contains no vocals. “Ooh” and “aah” sounds are treated as instrumental in this context. Rap or spoken word tracks are clearly “vocal”. The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content. Values above 0.5 are intended to represent instrumental tracks, but confidence is higher as the value approaches 1.0.
- Key : The key the track is in. Integers map to pitches using standard Pitch Class notation . E.g. 0 = C, 1 = C♯/D♭, 2 = D, and so on.
- Liveness : Detects the presence of an audience in the recording. Higher liveness values represent an increased probability that the track was performed live. A value above 0.8 provides strong likelihood that the track is live.
- Loudness : The overall loudness of a track in decibels (dB). Loudness values are averaged across the entire track and are useful for comparing relative loudness of tracks. Loudness is the quality of a sound that is the primary psychological correlate of physical strength (amplitude). Values typical range between -60 and 0 db.
- Mode : Mode indicates the modality (major or minor) of a track, the type of scale from which its melodic content is derived. Major is represented by 1 and minor is 0.
speechiness : Speechiness detects the presence of spoken words in a track. The more exclusively speech-like the recording (e.g. talk show, audio book, poetry), the closer to 1.0 the attribute value. Values above 0.66 describe tracks that are probably made entirely of spoken words. Values between 0.33 and 0.66 describe tracks that may contain both music and speech, either in sections or layered, including such cases as rap music. Values below 0.33 most likely represent music and other non-speech-like tracks.
- Tempo : The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is the speed or pace of a given piece and derives directly from the average beat duration.
- Time_signature : An estimated overall time signature of a track. The time signature (meter) is a notational convention to specify how many beats are in each bar (or measure).
- Valence : A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry).

### Dependent Variable
- Liked : 1 for liked songs , 0 for disliked songs

## Machine Learning based solution
* **First Step:** Importing the Data.
* **Second Step:** Data Analysis and Data quality check by checking its data quality: missing values, outliers, data format, etc. 
* **Third Step:** Data Pre-Processing.
* **Fourth Step:** Creating train and test sets:
  * X_train: *Used to train the Machine Learning Models*
  * X_test: *Used to test the performance of the trained models*
  
 * **Fifth Step:** Trained multiple Classifier Models. Checked the trained model's performance using the X_test set.
 
 * **Sixth Step:** Chose Extra Tree Classifier as the best model based on its accuracy score and saved it in the pickle format.
 
 * **Seventh Step:** Created a front-end app using **HTML and CSS** and integrated the pickle file with the app using the **flask framework**.
 
## Installation & running
The application is written in Python 3.7. If you don't have Python installed you can find it [here](https://www.python.org/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after cloning the repository :-

```
pip install -r requirements.txt
```

```
python app.py
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
