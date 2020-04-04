
import pandas as pd
from sklearn.datasets import load_diabetes


def get_train_data() -> (pd.DataFrame, pd.DataFrame):
    diabetes = load_diabetes()
    X_train = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
    y_train = pd.DataFrame(diabetes.target, columns=["target"])
    return X_train, y_train
