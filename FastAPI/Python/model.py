import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import joblib, pickle
import os
import yaml


# folder to load config file
CONFIG_PATH = "../Configs"

# Function to load yaml configuration file
def load_config(config_name):
    """[The function takes the yaml config file as input and loads the the config]

    Args:
        config_name ([yaml]): [The function takes yaml config as input]

    Returns:
        [string]: [Returns the config]
    """
    with open(os.path.join(CONFIG_PATH, config_name)) as file:
        config = yaml.safe_load(file)

    return config


config = load_config("config.yaml")

#path to the dataset
filename = "../../Data/breast-cancer-wisconsin.csv"


#load data 
data = pd.read_csv(filename)

#replace "?" with -99999
data = data.replace('?', -99999)

# drop id column
data = data.drop(config["drop_columns"], axis=1)

# Define X (independent variables) and y (target variable)
X = np.array(data.drop(config["target_name"], 1))
y = np.array(data[config["target_name"]])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=config["test_size"], random_state= config["random_state"]
)

# call our classifier and fit to our data
classifier = KNeighborsClassifier(
    n_neighbors=config["n_neighbors"],
    weights=config["weights"],
    algorithm=config["algorithm"],
    leaf_size=config["leaf_size"],
    p=config["p"],
    metric=config["metric"],
    n_jobs=config["n_jobs"],
)
# training the classifier
classifier.fit(X_train, y_train)

# test our classifier
result = classifier.score(X_test, y_test)
print("Accuracy score is. {:.1f}".format(result))

# Saving model to disk
pickle.dump(classifier, open('../../FastAPI//Models/KNN_model.pkl','wb'))

# Loading model to compare the results
#model = pickle.load(open('../../Flask/Models/KNN_model.pkl','rb'))
#print(model.predict([[17,20,100,115]]))



#################### using pickle #####################
# saved_model = pickle.dumps(classifier)
# load_model = pickle.loads(saved_model)
# result = load_model.predict(X_test)
# print(result)

#################### using joblib #####################

# model_name = "KNN_classifier"
# joblib.dump(classifier, './Models/{}.pkl'.format(model_name))

# Load the model from the file
# knn_from_joblib = joblib.load('./Models//KNN_classifier.pkl') 

# Use the loaded model to make predictions
# knn_from_joblib.predict(X_test)

#type([[np.array(data[['radius_mean','texture_mean']])]])

