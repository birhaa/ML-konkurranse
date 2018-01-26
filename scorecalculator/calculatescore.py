from sklearn.metrics import accuracy_score
import csv
import numpy as np
from math import sqrt
import pandas as pd

TEST_LABELS = '../data/Testdata/validate_dataset_only_labels.csv'

def readDataSet(groupname):
    with open(groupname, 'rb') as f:
        return map(int, f.readlines())


def readTarget():
    return pd.read_csv(TEST_LABELS, index_col=0).get_values()

def score(groupname):
    input_file = "../output/{}.txt".format(groupname)

    y_pred = readDataSet(input_file)
    y_true = readTarget()

    accuracy = accuracy_score(y_true, y_pred)

    print("group: {},  score: {}".format(groupname, accuracy))

# list all group names here
groups = ["ash"]

for g in groups:
    score(g)
