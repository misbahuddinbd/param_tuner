
import mlflow

from param_tuner.display.pandas import print_data
from param_tuner.src.data.make_dataset import get_train_data


def basic_lgbm():
    X_train, y_train = get_train_data()



if __name__ == "__main__":
    mlflow.start_run()
    basic_lgbm()
