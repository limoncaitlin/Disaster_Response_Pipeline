# Disaster_Response_Pipeline

## Description
This project was completed as a requirement for the Data Science Nanodegree Program from Udacity, in collaboration with Figure Eight. The goal of the project was to create a machine learning model that can classify text messages and tweets from a real-life disaster. The machine learning model was implemented into a webapp which could predict the category of any text entered into the text box. 

The Project contains 3 components:
1. An ETL Pipeline to read in csv files, clean and merge the data, and store them in a sql database.
2. A machine learning pipeline that trains a model to classify text messages by the category of disaster-aid needed.
3. A webapp to show some data visualizations and classify text entered into the text box.

## Getting Started
### Required Packages
- Python 3.5+ (I used python 3.7)
- Data science libraries: Numpy, pandas, scikit-learn
- Natural language processing library: NLTK
- SQL library: SQLAlchemy

### Installing and executing the program
1. Clone this repository
2. Run the following commands in the root directory to create the database and setup the model:
  - ETL Pipeline
  ```
  python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db
  ```
  - ML Pipeline
  ```
  python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl
  ```
3. In the app folder, run the following command:
  ```
  python run.py
  ```
4. Go to http://0.0.0.0.3001/

## Additional Materials
There are 2 jupyter notebooks available to help understand the setup of both the ETL pipeline (ETL Pipeline Preparation.ipynb), and the ML Pipeline (ML Pipeline Preparation.ipynb). The notebook showcases the grid search parameter selection process, and contains code to create two different classifiers. One based on a RandomForest classifier with GridSearch, and the other based on an AdaBoost Classifier. Both models perform fairly similarly and the RandomForest classifier was included in the train_classifier.py file and is implemented in the web app. 

## Some notes about model performance
The model implemented here has a very high accuracy score (0.946). However, when you use the web app, you will notice that the vast majority of things written in the text box are categorized as "related". This is the result of the training data being very unbalanced. The web app displays the number of messages in each category in the training set, and the vast majority are in the "related" category. There are methods to account for an unbalanced training set such as oversampling minority categories and undersampling majority categories, and in the future I would like to implement such methods to improve this model. You can view the precision and recall for each category in the ML Pipeline notebook and see that precision and recall vary widely based on category.

## Acknowledgements
- [Udacity](www.udacity.com)
    for creating the project and providing materials needed to implement the webapp and set up the notebooks.
- [Figure Eight](www.appen.com) 
    for providing the training data.


  
