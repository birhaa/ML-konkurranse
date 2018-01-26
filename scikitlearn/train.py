from sklearn import tree
import csv
import numpy as np
from sklearn.metrics import mean_squared_error as MSE
from math import sqrt
import pandas as pd

TRAIN_PATH = '../data/Treningsdata/train_dataset.csv'
TEST_PATH = '../data/Testdata/validate_dataset_without_labels.csv'

GROUP_NAME = 'ash'.lower()

def readDataSet():
    train_data = pd.read_csv(TRAIN_PATH, index_col=0, usecols=["1HP","1Attack","1Defence","1Sp.Attack","1Sp.Def","1Speed","1Generation","1Legendary","2HP","2Attack","2Defence","2Sp.Attack","2Sp.Def","2Speed","2Generation","2Legendary","Winner"])
    X = train_data.get_values()[:,:-1]
    y = train_data.get_values()[:,-1]
    return (X, y)

(X, y) = readDataSet()

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, y)

print("Training set score: %f" % clf.score(X, y))


# Root mean squeare error
p = clf.predict(X);

#-------------------------------------------------------
# Skriv resultat til fil

def readTestSet():
    train_data = pd.read_csv(TEST_PATH, index_col=0, usecols=["1HP","1Attack","1Defence","1Sp.Attack","1Sp.Def","1Speed","1Generation","1Legendary","2HP","2Attack","2Defence","2Sp.Attack","2Sp.Def","2Speed","2Generation","2Legendary"])
    return train_data.get_values()

X_test = readTestSet()

p = clf.predict(X_test);

fileOut = open("../output/{}.txt".format(GROUP_NAME), "w")

for prediction in p:
    fileOut.write("{0}\n".format(prediction))
