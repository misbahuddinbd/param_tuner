
import pandas as pd


def print_data(data: pd.DataFrame, rows=1, context=""):
    print(f"{context} Shape: {data.shape}")
    print(data.head(rows))
