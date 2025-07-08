import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib

def train():
    data = load_iris()
    X, y = data.data, data.target
    clf = RandomForestClassifier()
    clf.fit(X, y)
    joblib.dump(clf, 'model.pkl')

if __name__ == "__main__":
    train()
