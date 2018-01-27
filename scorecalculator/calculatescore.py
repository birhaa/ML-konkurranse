from sklearn.metrics import accuracy_score
import csv
import numpy as np
from math import sqrt
import pandas as pd
import math

TEST_LABELS = '../test_data.csv'

def readDataSet(groupname):
    with open(groupname, 'rb') as f:
        return map(int, f.readlines())


def readTarget():
    return pd.read_csv(TEST_LABELS, index_col=0)["Winner"].get_values()

def score(groupname):
    input_file = "../output/{}.txt".format(groupname)

    y_pred = readDataSet(input_file)
    y_true = readTarget()


    true_or_false = map(lambda (a, b): a == b, zip(y_pred, y_true))

    print("group: {:10},  score: {} / {}".format(groupname, sum(true_or_false), len(true_or_false)))

# list all group names here
groups = ["ash", "bulbasar"]

for g in groups:
    score(g)
